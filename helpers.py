import hashlib
import sys
import json
import requests
import csv
import re

def encode_uint256(integer):
    return format(integer, '064x')

def get_token_decimals(chain, token_address):
    # The function selector for decimals() in ERC20 contracts
    function_selector = "0x313ce567"  # keccak256("decimals()")
    response = make_rpc_call(chain, token_address, function_selector, "latest")
    return int(response, 16)  # Convert hexadecimal to integer

def get_token_symbol(chain, token_address):
    # The function selector for symbol() in ERC20 contracts
    function_selector = "0x95d89b41"  # keccak256("symbol()")
    response = make_rpc_call(chain, token_address, function_selector, "latest")
    
    # Remove the '0x' prefix
    response = response[2:]
    
    # Convert the Hex String to Bytes
    byte_string = bytes.fromhex(response)

    # Decode the byte string into utf-8
    decoded = byte_string.decode('utf-8').strip()

    # Clean the string of anything around it
    clean_string = re.sub('[^a-zA-Z]', '', decoded)

    return clean_string

def make_rpc_request(url, method, params=None):
    print(f"Making RPC request to: {url} with method: {method} and params: {params}")
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": 1
    }

    response = requests.post(url, json=payload)
    # print("Response status code:", response.status_code)
    # print("Response text:", response.text)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"RPC request failed with status code: {response.status_code}")

def make_rpc_call(chain, contract_address, data, blocknumber, method="eth_call"):
    url = chain.rpc_url
    if blocknumber != "latest" and blocknumber is not None:
        blocknumber = hex(blocknumber)
    params = [{
        "to": contract_address,
        "data": data
    }, blocknumber]

    try:
        response = make_rpc_request(url, method, params)
        result = response['result']
        if result == '0x':
            return result
        else:
            return result
        return data
    except Exception as e:
        return 0