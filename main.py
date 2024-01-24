import json
import requests
import csv
import hashlib
import sys
from web3 import Web3
from helpers import make_rpc_call, get_token_decimals, encode_uint256, get_token_symbol
from config.timeData import times, month_timestamps
from config.config import arbitrum, aurora, avax, base, boba, bsc, canto, cronos, dfk, dogechain, ethereum, fantom, harmony, metis, moonbeam, moonriver, optimism, polygon, klaytn
from datetime import datetime

current_datetime = datetime.now()

current_month = current_datetime.month

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
current_month_name = month_names[current_month - 1]

# Print the current month
print("Current Month (number):", current_month)
print("Current Month (name):", current_month_name)

print(month_timestamps)
print(len(month_timestamps))
chains = [klaytn]
    #arbitrum, aurora, avax, base, boba, bsc, canto, cronos, dfk, dogechain, ethereum, fantom, harmony, metis, moonbeam, moonriver, optimism, polygon, klaytn]
# Getting the balance of whats claimed in the multisig
def get_balance(chain, contract_address, decimals, blocknumber="latest"):
    #print(f"Entering get_balance. Chain: {chain.name}, Contract Address: {contract_address}, Decimals: {decimals}, Blocknumber: {blocknumber}")
    print(f" Blocknumber: {blocknumber}")
    data = "0x70a08231" + chain.multisig[2:].zfill(64)
    balance_hex = make_rpc_call(chain, contract_address, data, blocknumber)
    print(f"Balance hex: {balance_hex}")
    if balance_hex == '0x' or balance_hex == 0:
        balance = 0
    else:
        balance = int(balance_hex, 16)
    print(f"Exiting get_balance. Balance: {balance}")
    return balance / (10 ** decimals)

# Getting the balance of whats unclaimed in bridge contracts. 
def get_fee_balance(chain, contract_address, decimals, blocknumber="latest"):
    data = "0xc78f6803" + contract_address[2:].zfill(64)
    balance_hex = make_rpc_call(chain, chain.bridge_address, data, blocknumber)
    if balance_hex == '0x' or balance_hex == 0:
        balance = 0
    else:
        balance = int(balance_hex, 16)
    return (balance / 10 ** decimals)

# Getting the balance of whats unclaimed in swap contracts
def get_swap_fee_balance(chain, pool, index, blocknumber="latest"):
    #print(f"Entering get_swap_fee_balance. Chain: {chain.name}, Pool: {pool}, Index: {index}, Blocknumber: {blocknumber}")
    print(f"Blocknumber: {blocknumber}")

    # Get the entire function hash, and then truncate it to get the function hash
    admin_function_selector = Web3.keccak(text='getAdminBalance(uint256)').hex()[0:10]
    token_function_selector = Web3.keccak(text='getToken(uint8)').hex()[0:10]

    #Setup the data
    get_token_amount = admin_function_selector + encode_uint256(index)
    get_token_address = token_function_selector + encode_uint256(index)

    # Make an RPC call to get the token Amount (Nominal)
    result = make_rpc_call(chain, pool,  get_token_amount, blocknumber)
    if not isinstance(result, str):
        result = str(result)
    amount = int(result,16)
    # Make an RPC call to get the token Address (hex string)
    address = "0x" + make_rpc_call(chain, pool, get_token_address, blocknumber)[-40:]

    # Get the proper amount of token decimals
    amount = amount/ 10**get_token_decimals(chain, address)
    token_symbol = get_token_symbol(chain, address)

    # Use this to get the proper balance
    balance = get_defillama_price(chain.name, address) * amount
    
    # print(f"\n The token {token_symbol} at index {index} has \n amount: {amount} \n balance: {balance} \n \n ")
    #print(f"Exiting get_swap_fee_balance. Token Symbol: {token_symbol}, Balance: {balance}")
    return token_symbol, balance

def get_cctp_balance(chain, blocknumber="latest"):
    fees_function_selector = Web3.keccak(text='accumulatedFees(address,address)').hex()[0:10]
    amount = 0
    if chain.cctp:
        usdc_address = next((token[1] for token in chain.tokens if token[0] == "USDC"), None)
        if usdc_address:
            usdc_address = usdc_address[2:].zfill(64)
            protocol_fees = '0x0000000000000000000000000000000000000000'[2:].zfill(64)
            get_cctp_fees = fees_function_selector + protocol_fees + usdc_address
            result = make_rpc_call(chain, chain.cctp, get_cctp_fees, blocknumber)
            if not isinstance(result, str):
                result = str(result)
            amount = int(result, 16) / 10**6
            return amount

    return amount


def get_defillama_price(chain_name, token_address, timestamp = None):
    if timestamp == None:
        # Define the URL (Current)
        url = f"https://coins.llama.fi/prices/current/{chain_name}:{token_address}?searchWidth=4h"
    else:
        # Define the URL (historical)
        url = f"https://coins.llama.fi/prices/historical/{timestamp}/{chain_name}:{token_address}?searchWidth=4h"
    
    try:
        # Make the GET request
        response = requests.get(url)

        # Check the status code
        if response.status_code == 200:
            #print("Response status code:", response.status_code)
            #print("Response text:", response.text)
            # Parse the JSON response
            data = response.json()
            # Extract the price
            price = data['coins'][f'{chain_name}:{token_address}']['price']
            return price
        else:
            raise Exception()
    except Exception as e:
        return 0
    

# First thing is to call get_balance of each of these tokens on the multisig and then run it through the DL price API 
def get_token_balances_and_values(timestamp = None, month = "Current", specific_chain=None):
    # Initialize a dictionary to store the sums
    sums = {}

    with open(f'treasuryHoldings_{month}_2023.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the headers
        writer.writerow(["Chain", "Token Symbol", "Value", "Type", "Contract Address"])

        # 1. Iterate over each chain in the chains dictionary
        for chain in chains:
            # Initialize the sums for this chain
            sums[chain.name] = {"Claimed Fees": 0, "Unclaimed Fees": 0, "Swap Unclaimed Fees": 0, "CCTP Unclaimed Fees":0}


            if specific_chain and chain.name != specific_chain:
                continue
            if month == "Current": 
                block = "latest"
            else: 
                block = times[chain.name][month-1]


            # 2. For each chain, iterate over the tokens supported by that chain
            for token in chain.tokens:

                # 3. Call the getBalance method on the multisig contract for each token
                balance = get_balance(chain, token[1], token[2], block )
                # Call the getFeeBalance method on the bridge contract for each token
                fee_balance = get_fee_balance(chain, token[1], token[2], block)
                # 4. Call the DeFiLlama API to get the price of the token
                if timestamp == None:
                    price = get_defillama_price(chain.name, token[1])
                else: 
                    price = get_defillama_price(chain.name, token[1], timestamp)
                # 5. Multiply the balance by the price to get the value
                claimed_value = balance * price
                unclaimed_value = fee_balance * price

                # Add the values to the sums
                sums[chain.name]["Claimed Fees"] += claimed_value
                sums[chain.name]["Unclaimed Fees"] += unclaimed_value

                # 6. Store the chain, token address, token symbol, balance, and value
                writer.writerow([chain.name, token[0], claimed_value, "Claimed Fees", chain.multisig])
                writer.writerow([chain.name, token[0], unclaimed_value, "Unclaimed Fees", chain.bridge_address])
            # Finish figuring out amount in each pool
            for pool in chain.swap_addresses:
                i = 0
                swap_unclaimed_value = 0
                while True: 
                    try:
                        symbol, token_value = get_swap_fee_balance(chain, pool, i, block)
                        swap_unclaimed_value += token_value
                        sums[chain.name]["Swap Unclaimed Fees"] += token_value
                        writer.writerow([chain.name, symbol, token_value, "Swap Unclaimed Fees", pool])
                        i +=1
                    except Exception as e: 
                        print(f"Exception occured: {e}")
                        break   
            # Find and add CCTP addresses
            for address in chain.cctp:
                cctp_fees = get_cctp_balance(chain, block)
                sums[chain.name]["CCTP Unclaimed Fees"] += cctp_fees
                writer.writerow([chain.name,"USDC", cctp_fees, "CCTP Unclaimed Fees", address])
            

    # Write the sums to a new CSV file
    with open(f'treasurySums_{month}_2023.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the headers
        writer.writerow(["Chain", "Claimed Fees", "Unclaimed Fees", "Swap Unclaimed Fees", "CCTP Unclaimed Fees"])
        # print(f'\n \n \n \n \n \n Hello, here is {sums} \n \n \n \n \n \n')
        # Write the sums
        for chain_name, values in sums.items():
            writer.writerow([chain_name, values["Claimed Fees"], values["Unclaimed Fees"], values["Swap Unclaimed Fees"], values["CCTP Unclaimed Fees"]])



# Call this to redo the backfill
def backfill_treasury_balances():
    """
    Backfills treasury balances for the available months in the month_timestamps list.
    """
    # Get the current year's available months based on the length of month_timestamps
    available_months = len(month_timestamps)

    for month_index in range(available_months):
        time = month_timestamps[month_index]
        month = month_index + 1  # Adjusting month number (since index starts at 0)
        try:
            print(f"Backfilling for month {month} with timestamp {time}")
            get_token_balances_and_values(time, month)
        except Exception as e:
            print(f"Error occurred during backfilling for month {month}: {e}")

# Call this to get the current balances 
def get_current_balances():
    # Can specify a specific_chain value to restrict the program to only those chains.
    get_token_balances_and_values()

if __name__ == "__main__":
    #get_current_balances()
    backfill_treasury_balances()