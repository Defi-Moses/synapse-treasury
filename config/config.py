import os
from dotenv import load_dotenv
load_dotenv()

# Chain Class
class Chain:
    def __init__(self,name, rpc_url, bridge_address, multisig, swap_addresses, tokens, cctp):
        self.name = name
        self.rpc_url = rpc_url
        self.bridge_address = bridge_address
        self.multisig = multisig
        self.swap_addresses = swap_addresses
        self.tokens = tokens
        self.cctp = cctp


arbitrum = Chain(
    name= 'arbitrum',
    rpc_url=os.getenv('ARBITRUM_RPC'),
    bridge_address='0x6F4e8eBa4D337f874Ab57478AcC2Cb5BACdc19c9',
    multisig='0x1d9Bfc24d9e7EeDa4119Ceca11EaF4c24E622E62',
    swap_addresses=[
        '0x3Ca625F5896e725840cCAb1Bbe2d62623eff865a',
        '0x84cd82204c07c67dF1C2C372d8Fd11B3266F76a3',
        '0x0Db3FE3B770c95A0B99D1Ed6F2627933466c0Dd8',
        '0x9Dd329F5411466d9e0C488fF72519CA9fEf0cb40',
        '0xa067668661C84476aFcDc6fA5D758C4c01C34352'
    ],
    tokens=[
        ("ETH", "0x0000000000000000000000000000000000000000", 18),
        ("USDC", "0xaf88d065e77c8cc2239327c5edb3a432268e5831", 6),
        ("USDT", "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9", 6),
        ("DAI", "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1", 18),
        ("GMX", "0xfc5a1a6eb076a2c7ad06ed22c90d7e710e35ad0a", 18),
        ("FRAX", "0x17FC002b466eEc40DaE837Fc4bE5c67993ddBd6F", 18),
        ("NETH", "0x3ea9b0ab55f34fb188824ee288ceaefc63cf908e", 18),
        ("ARB", "0x912ce59144191c1204e64559fe8253a0e49e6548", 18),
        ("USDC.e", "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8", 6),
        ("GOHM", "0x8D9bA570D6cb60C7e3e0F31343Efe75AB8E65FB1", 18),
        ("WETH", "0x82af49447d8a07e3bd95bd0d56f35241523fbab1", 18),
        # ("SDT", "0x087d18A77465c34CDFd3a081a2504b7E86CE4EF8", 18),
        # ("PEPE", "0xA54B8e178A49F8e5405A4d44Bb31F496e5564A05", 18),
        # ("VSTA", "0xa684cd057951541187f288294a1e1c2646aa2d24", 18),
        # ("H20", "0xD1c6f989e9552DB523aBAE2378227fBb059a3976", 18),
        # ("L2DAO", "0x2CaB3abfC1670D1a452dF502e216a66883cDf079", 18),
        # ("PLS", "0x51318b7d00db7acc4026c88c3952b66278b6a67f", 18),
        ("UNIDX", "0x5429706887FCb58a595677B73E9B0441C25d993D", 18),
        ("SYN", "0x080f6aed32fc474dd5717105dba5ea57268f46eb", 18),
        ("NUSD", "0x2913E812Cf0dcCA30FB28E6Cac3d2DCFF4497688", 18),
    ],
    cctp= ['0xfb2bfc368a7edfd51aa2cbec513ad50edea74e84','0x12715a66773BD9C54534a01aBF01d05F6B4Bd35E']
)


aurora = Chain(
    name= 'aurora',
    rpc_url=os.getenv('AURORA_RPC'),
    bridge_address='0xaeD5b25BE1c3163c907a471082640450F928DDFE',
    multisig='0xbb227Fcf45F9Dc5deF87208C534EAB1006d8Cc8d',
    swap_addresses=['0xcEf6C2e20898C2604886b888552CA6CcF66933B0'],
    tokens=[
        ("NUSD", "0x07379565cD8B0CaE7c60Dc78e7f601b34AF2A21c", 18),
        ("USDC.e", "0xB12BFcA5A55806AaF64E99521918A4bf0fC40802", 6),
        ("USDT.e", "0x4988a896B1227218e4A686fdE5EabdcAbd91571f", 6),
    ],
    cctp=['']
)

avax = Chain(
    name= 'avax',
    rpc_url=os.getenv('AVAX_RPC'),
    bridge_address='0xC05e61d0E7a63D27546389B7aD62FdFf5A91aACE',
    multisig='0xE9530411510c4D6CF699712904bECA2849488176',
    swap_addresses=[
        '0xE55e19Fb4F2D85af758950957714292DAC1e25B2',
        '0xF44938b0125A6662f9536281aD2CD6c499F22004',
        '0xED2a7edd7413021d440b09D654f3b87712abAB66',
        '0xA196a03653f6cc5cA0282A8BD7Ec60e93f620afc',
        '0x77a7e60555bC18B4Be44C181b2575eee46212d44'
    ],
    tokens=[
        #something is wrong with finding the price of AVAX
        ("AVAX", "0x0000000000000000000000000000000000000000", 18),
        ("AVAX","0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7", 18),
        ("USDT.e", "0xc7198437980c041c805A1EDCbA50c1ce5db95118", 6),  
        ("USDC.e", "0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664", 6),
        ("DAI.e", "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70", 18),
        ("WETH.e", "0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB", 18),
        ("GOHM", "0x321E7092a180BB43555132ec53AaA65a5bF84251", 18),
        ("SYN", "0x1f1e7c893855525b303f99bdf5c3c05be09ca251", 18),
        ("GMX", "0x62edc0692bd897d2295872a9ffcac5425011c661", 18),
        ("NETH", "0x19e1ae0ee35c0404f835521146206595d37981ae", 18),
        ("NUSD", "0xcfc37a6ab183dd4aed08c204d1c2773c0b1bdf46", 18),
        ("USDC", "0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e", 6),
        ("USDT", "0x9702230a8ea53601f5cd2dc00fdbc13d4df4a8c7", 6),
        ("JEWEL", "0x997Ddaa07d716995DE90577C123Db411584E5E46", 18),
        ("JEWEL", "0x4f60a160D8C2DDdaAfe16FCC57566dB84D674BD6", 18),
        ("BTCB", "0x152b9d0FdC40C096757F570A51E494bd4b943E50", 18),
        ("AVWETH", "0x53f7c5869a859f0aec3d334ee8b4cf01e3492f21", 18),
        # ("SFI", "0xc2Bf0A1f7D8Da50D608bc96CF701110d4A438312", 18),
        # ("NFD", "0xf1293574ee43950e7a8c9f1005ff097a9a713959", 18),
        # ("SDT", "0xCCBf7c451F81752F7d2237F2c18C371E6e089E69", 18),
        # ("NEWO", "0x4Bfc90322dD638F81F034517359BD447f8E0235a", 18),
        # ("H20", "0xC6b11a4Fd833d1117E9D312c02865647cd961107", 18),
    ],
    cctp=['0xfB2Bfc368a7edfD51aa2cbEC513ad50edEa74E84','0x12715a66773BD9C54534a01aBF01d05F6B4Bd35E']
)

base = Chain(
    name= 'base',
    rpc_url=os.getenv('BASE_RPC'),
    bridge_address='0xf07d1C752fAb503E47FEF309bf14fbDD3E867089',
    multisig='0xE48de7c3A9094b2CbA88D4f72E3cbc2E60Fad8cF',
    swap_addresses=[
        '0x6223bD82010E2fB69F329933De20897e7a4C225f',
    ],
    tokens=[
        ("ETH", "0x0000000000000000000000000000000000000000", 18),
        ("SYN", "0x432036208d2717394d2614d6697c46DF3Ed69540", 18),
        ("NETH", "0xb554A55358fF0382Fb21F0a478C3546d1106Be8c", 18),
        ("WETH", "0x4200000000000000000000000000000000000006", 18),
        ("UNIDX", "0x6B4712AE9797C199edd44F897cA09BC57628a1CF", 18),
        ("USDC", "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913", 6), 
    ],
    cctp=['0xfB2Bfc368a7edfD51aa2cbEC513ad50edEa74E84']
)

blast = Chain(
    name= 'blast',
    rpc_url=os.getenv('BLAST_RPC'),
    bridge_address='0x55769baf6ec39b3bf4aae948eb890ea33307ef3c',
    multisig='0x11EB5B6C45fB7E70aDf6a639E6C9CF58F0073aa9',
    swap_addresses=[
        '0xa4bd1AAD7cF04567c10f38FC4355E91bba32aC9c',
        '0x999fcd13C54B26E02a6Ccd185f71550b3a4641c0',
    ],
    tokens=[
        ("SYN", "0x9592f08387134e218327E6E8423400eb845EdE0E", 18),
        ("NETH", "0xce971282faac9fabcf121944956da7142cccc855", 18),
        ("WETH", "0x4300000000000000000000000000000000000004", 18),
        ("USDB", "0x4300000000000000000000000000000000000003", 18),
        ("NUSD", "0x3194B0A295D87fDAA54DF852c248F7a6BAF6c6e0", 18), 
    ],
    cctp=['']
)

boba = Chain(
    name= 'boba',
    rpc_url=os.getenv('BOBA_RPC'),
    bridge_address='0x432036208d2717394d2614d6697c46DF3Ed69540',
    multisig='0xbb227Fcf45F9Dc5deF87208C534EAB1006d8Cc8d',
    swap_addresses=[
        '0x75FF037256b36F15919369AC58695550bE72fead',
        '0x753bb855c8fe814233d26Bb23aF61cb3d2022bE5',
    ],
    tokens=[
        ("WETH", "0xd203De32170130082896b4111eDF825a4774c18E", 18),
        ("ETH", "0x0000000000000000000000000000000000000000", 18),
        ("USDC", "0x66a2A913e447d6b4BF33EFbec43aAeF87890FBbc", 6),
        ("USDT", "0x5DE1677344D3Cb0D7D465c10b72A8f60699C062d", 6),
        ("DAI", "0xf74195Bb8a5cf652411867c5C2C5b8C2a402be35", 18),
        # ("WBTC", "0x499d11E0b6eAC7c0593d8Fb292DCBbF815Fb29Ae", 8), 
        # ("SYN", "0xb554A55358fF0382Fb21F0a478C3546d1106Be8c", 18),
        ("NUSD", "0x6B4712AE9797C199edd44F897cA09BC57628a1CF", 18),
        ("NETH", "0x96419929d7949D6A801A6909c145C8EEf6A40431", 18),
    ],
    cctp=['']
)

bsc = Chain(
    name= 'bsc',
    rpc_url=os.getenv('BSC_RPC'),
    bridge_address='0xd123f70AE324d34A9E76b67a27bf77593bA8749f',
    multisig='0x0056580B0E8136c482b03760295F912279170D46',
    swap_addresses=[
        '0x938aFAFB36E8B1AB3347427eb44537f543475cF9',
        '0x930d001b7efb225613aC7F35911c52Ac9E111Fa9',
        '0x28ec0B36F0819ecB5005cAB836F4ED5a2eCa4D13',
        '0x740B36494A5Ebe0F18f3e05f3a951ae292080d33',
    ],
    tokens=[
        ("BUSD", "0xe9e7cea3dedca5984780bafc599bd69add087d56", 18), 
        ("USDC", "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d", 18),
        ("NUSD", "0x23b891e5c62e0955ae2bd185990103928ab817b3", 18),
        ("HIGH", "0x5f4bde007dc06b867f86ebfe4802e34a1ffeed63", 18),
        #Looks weird on explorer?
        ("BSC-USD", "0x55d398326f99059ff775485246999027b3197955", 18),
        # ("JUMP", "0x130025ee738a66e691e6a7a62381cb33c6d9ae83", 18),
        # ("DOG", "0xaa88c603d142c371ea0eac8756123c5805edee03", 18),
        # ("NFD", "0x0fe9778c005a5a6115cbe12b0568a2d50b765a51", 18),
        # ("H20", "0x03eFca7CEb108734D3777684F3C0A0d8ad652f79", 18),
        ("USDT", "0x55d398326f99059ff775485246999027b3197955", 18),
        ("SYN", "0xa4080f1778e69467e905b8d6f72f6e441f9e9484", 18),
    ],
    cctp=['']
)

canto = Chain(
    name= 'canto',
    rpc_url=os.getenv('CANTO_RPC'),
    bridge_address='0xDde5BEC4815E1CeCf336fb973Ca578e8D83606E0',
    multisig='0x02BA7A3Cd181a103Ba5702e708cF22de4Fa70254',
    swap_addresses=[
        '0xF60F88bA0CB381b8D8A662744fF93486273c22F9',
    ],
    tokens=[
        ("NETH", "0x09fEC30669d63A13c666d2129230dD5588E2e240", 18), 
        ("NUSD", "0xD8836aF2e565D3Befce7D906Af63ee45a57E8f80", 18),
        ("USDC", "0x80b5a32E4F032B2a058b4F29EC95EEfEEB87aDcd", 6),
        ("NOTE", "0x4e71a2e537b7f9d9413d3991d37958c0b5e1e503", 18),
        ("ETH", "0x5FD55A1B9FC24967C4dB09C513C3BA0DFa7FF687", 18),
        ("USDT", "0xd567B3d7B8FE3C79a1AD8dA978812cfC4Fa05e75", 6),
        #broke DL API 
        # ("SYN", "0x555982d2E211745b96736665e19D9308B615F78e", 18),
    ],
    cctp=['']
)

cronos = Chain(
    name= 'cronos',
    rpc_url=os.getenv('CRONOS_RPC'),
    bridge_address='0xE27BFf97CE92C3e1Ff7AA9f86781FDd6D48F5eE9',
    multisig='0x7f91f3111b2009eC7c079Be213570330a37e8aeC',
    swap_addresses=[
        '0xCb6674548586F20ca39C97A52A0ded86f48814De',
    ],
    tokens=[
        ("USDC", "0xc21223249ca28397b4b6541dffaecc539bff0c59", 6),
        # ("SYN", "0xFD0F80899983b8D46152aa1717D76cba71a31616", 18), 
        ("NUSD", "0x396c9c192dd323995346632581BEF92a31AC623b", 18),
        # ("GOHM", "0x88918495892BAF4536611E38E75D771Dc6Ec0863", 18),
    ],
    cctp=['']
)

dfk = Chain(
    name= 'dfk',
    rpc_url=os.getenv('DFK_RPC'),
    bridge_address='0xE05c976d3f045D0E6E7A6f61083d98A15603cF6A',
    multisig='0x2e62c47f502f512c75bd5ecd70799efb0fe7baa3',
    swap_addresses=['address1', 'address2', 'address3'],
    tokens=[
        ("USDC", "0x3AD9DFE640E1A9Cc1D9B0948620820D975c3803a", 18),
        ("ETH", "0xfBDF0E31808d0aa7b9509AA6aBC9754E48C58852", 18),
        ("FTM", "0x2Df041186C844F8a2e2b63F16145Bc6Ff7d23E25", 18),
        ("MATIC", "0xD17a41Cd199edF1093A9Be4404EaDe52Ec19698e", 18),
        ("BTCB","0x7516EB8B8Edfa420f540a162335eACF3ea05a247", 8),
        ("KLAY", "0x97855Ba65aa7ed2F65Ed832a776537268158B78a", 18),
        ("AVAX", "0xB57B60DeBDB0b8172bb6316a9164bd3C695F133a", 18),
        ("JEWEL", "0x0000000000000000000000000000000000000000", 18),
        ("WJEWEL", "0xCCb93dABD71c8Dad03Fc4CE5559dC3D89F67a260", 18),
        ("XJEWEL", "0x77f2656d04E158f915bC22f07B779D94c1DC47Ff", 18),
    ],
    cctp=['']
)

dogechain = Chain(
    name= 'dogechain',
    rpc_url=os.getenv('DOGECHAIN_RPC'),
    bridge_address='0x9508BF380c1e6f751D97604732eF1Bae6673f299',
    multisig='0x8f17b483982d1cc09296aed8f1b09ad830358a8d',
    swap_addresses=[],
    tokens=[
        # ("BUSD", "0x1555C68Be3b22cdcCa934Ae88Cb929Db40aB311d", 18),
        ("USDC", "0x85C2D3bEBffD83025910985389aB8aD655aBC946", 6),
        ("USDT", "0x7f8e71DD5A7e445725F0EF94c7F01806299e877A", 6),
        ("DAI", "0xB3306f03595490e5cC3a1b1704a5a158D3436ffC", 18),
        ("WBTC", "0xD0c6179c43C00221915f1a61f8eC06A5Aa32F9EC", 8),
        # ("SYN", "0xDfA53EeBA61D69E1D2b56b36d78449368F0265c1", 18),
        ("FRAX", "0x10D70831f9C3c11c5fe683b2f1Be334503880DB6", 18),
        ("WETH", "0x9F4614E4Ea4A0D7c4B1F946057eC030beE416cbB", 18),
    ],
    cctp=['']
)

ethereum = Chain(
    name= 'ethereum',
    rpc_url=os.getenv('ETHEREUM_RPC'),
    bridge_address='0x2796317b0fF8538F253012862c06787Adfb8cEb6',
    multisig='0x67F60b0891EBD842Ebe55E4CCcA1098d7Aac1A55',
    swap_addresses=['0x1116898DdA4015eD8dDefb84b6e8Bc24528Af2d8'],
    tokens=[
        ("ETH", "0x0000000000000000000000000000000000000000", 18),
        ("USDC", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 6),
        ("DAI", "0x6b175474e89094c44da98b954eedeac495271d0f", 18),
        ("WBTC", "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599", 8),
        ("LINK", "0x514910771af9ca656af840dff83e8264ecf986ca", 18),
        ("HIGH", "0x71ab77b7dbb4fa7e017bc15090b2163221420282", 18),
        # ("DOG", "0xBAac2B4491727D78D2b78815144570b9f2Fe8899", 18),
        # ("SFI", "0xb753428af26e81097e7fd17f40c88aaa3e04902c", 18),
        # ("PEPE", "0x6982508145454ce325ddbe47a25d4ec3d2311933", 18),
        # ("VSTA", "0xA8d7F5e7C78ed0Fa097Cc5Ec66C1DC3104c9bbeb", 18),
        # ("H2O", "0x0642026e7f0b6ccac5925b4e7fa61384250e1701", 18),
        ("UNIDX", "0xf0655dcee37e5c0b70fffd70d85f88f8edf0aff6", 18), 
        ("FRAX", "0x853d955acef822db058eb8505911ed77f175b99e", 18),
        ("NUSD", "0x1B84765dE8B7566e4cEAF4D0fD3c5aF52D3DdE4F", 18),
        ("GOHM", "0x0ab87046fBb341D058F17CBC4c1133F25a20a52f", 18),
        ("OHM", "0x64aa3364F17a4D01c6f1751Fd97C2BD3D7e7f1D5", 9),
        ("SYN", "0x0f2d719407fdbeff09d87557abb7232601fd9f29", 18),
        ("USDT", "0xdac17f958d2ee523a2206206994597c13d831ec7", 6),
        # ("SDT", "0x73968b9a57c6e53d41345fd57a6e6ae27d6cdb2f", 18),
        ("SYN-ETH Sushi LP", "0x4a86c01d67965f8cb3d0aaa2c655705e64097c31", 18),
        ("WETH", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", 18),     
    ],
    cctp=['']
)

fantom = Chain(
    name= 'fantom',
    rpc_url=os.getenv('FANTOM_RPC'),
    bridge_address='0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b',
    multisig='0x224002428cF0BA45590e0022DF4b06653058F22F',
    swap_addresses=[
        '0x080F6AEd32Fc474DD5717105Dba5ea57268F46eb',
        '0x1f6A0656Ff5061930076bf0386b02091e0839F9f',
        '0x2913E812Cf0dcCA30FB28E6Cac3d2DCFF4497688',
        '0x85662fd123280827e11C59973Ac9fcBE838dC3B4',
        '0x8D9bA570D6cb60C7e3e0F31343Efe75AB8E65FB1'
    ],
    tokens=[
        ("FTM", "0x0000000000000000000000000000000000000000", 18),
        ("WFTM", "0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83", 18),
        # ("JUMP", "0x78DE9326792ce1d6eCA0c978753c6953Cdeedd73", 18),
        # ("SDT", "0xE3c82A836Ec85311a433fBd9486EfAF4b1AFbF48", 18),
        ("SYN", "0xE55e19Fb4F2D85af758950957714292DAC1e25B2", 18),
        ("NUSD", "0xED2a7edd7413021d440b09D654f3b87712abAB66", 18),
        ("NETH", "0x67c10c397dd0ba417329543c1a40eb48aaa7cd00", 18),
        ("GOHM", "0x91fa20244Fb509e8289CA630E5db3E9166233FDc", 18),
        ("UNIDX", "0x0483a76D80D0aFEC6bd2afd12C1AD865b9DF1471", 18),
        # ("SYNFRAX", "0x1852F70512298d56e9c8FDd905e02581E04ddb2a", 18),
        # ("WETH", "0x74b23882a30290451A17c44f4F05243b6b58C76d", 18),
        # ("USDC", "0x04068DA6C83AFCFA0e13ba15A6696662335D5B75", 6),
    ],
    cctp=['']
)

harmony = Chain(
    name= 'harmony',
    rpc_url=os.getenv('HARMONY_RPC'),
    bridge_address='0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b',
    multisig='0x0172e7190Bbc0C2Aa98E4d1281d41D0c07178605',
    swap_addresses=[
        '0x080F6AEd32Fc474DD5717105Dba5ea57268F46eb',
        '0x555982d2E211745b96736665e19D9308B615F78e',
        '0x3ea9B0ab55F34Fb188824Ee288CeaEfC63cf908e',
        '0x2913E812Cf0dcCA30FB28E6Cac3d2DCFF4497688',
    ],
    tokens=[
        # Need to double check
        ("NUSD", "0xed2a7edd7413021d440b09d654f3b87712abab66", 18), 
        ("NETH", "0x0b5740c6b4a97f90eF2F0220651Cca420B868FfB", 18), 
    ],
    cctp=['']
)

metis = Chain(
    name= 'metis',
    rpc_url=os.getenv('METIS_RPC'),
    bridge_address='0x06Fea8513FF03a0d3f61324da709D4cf06F42A5c',
    multisig='0xEAEC50eBe1c2A981ED8be02C36b0863Fae322975',
    swap_addresses=[
        '0x555982d2E211745b96736665e19D9308B615F78e',
        '0x09fEC30669d63A13c666d2129230dD5588E2e240',
    ],
    tokens=[
        ("METIS", "0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000", 18),
        ("m.USDC", "0xEA32A96608495e54156Ae48931A7c20f0dcc1a21", 6),
        ("WETH", "0x420000000000000000000000000000000000000A", 18),
        # ("WBTC", "0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6", 8),
        # ("USDT", "0x44cED87b9F1492Bf2DCf5c16004832569f7f8C10", 6),
        # ("JUMP", "0xE3c82A836Ec85311a433fBd9486EfAF4b1AFbF48", 18),
        # ("UNIDX", "0x6B4712AE9797C199edd44F897cA09BC57628a1CF", 18),
        ("SYN", "0x67C10C397dD0Ba417329543c1a40eb48AAa7cd00", 18),
        # ("GOHM", "0xFB21B70922B9f6e3C6274BcD6CB1aa8A0fe20B80", 18),
        ("NUSD", "0x961318Fc85475E125B99Cc9215f62679aE5200aB", 18),
        ("NETH", "0x931B8f17764362A3325D30681009f0eDd6211231", 18),
    ],
    cctp=['']
)

moonriver = Chain(
    name= 'moonriver',
    rpc_url=os.getenv('MOONRIVER_RPC'),
    bridge_address='0xaeD5b25BE1c3163c907a471082640450F928DDFE',
    multisig='0x4bA30618fDcb184eC01a9B3CAe258CFc5786E70E',
    swap_addresses=[],
    tokens=[
        ("MOVR", "0x98878B06940aE243284CA214F92Bb71a2B032B8A", 18), 
        # ("SOLAR", "0x76906411D07815491A5E577022757aD941fb5066", 18),
        ("USDC", "0xE3F5a90F9cb311505cd691a46596599aA1A0AD7D", 6),
        ("WETH", "0x639a647fbe20b6c8ac19e48e2de44ea792c62c5c", 18),
        # ("MOON", "0x81d51E71B8A74D4C682b4C83fa1c1DC68f299091", 18),
        # ("H2O", "0x9c0a820bb01e2807aCcd1c682d359e92DDd41403", 18),
        # ("SYNFRAX", "0xE96AC70907ffF3Efee79f502C985A7A21Bce407d", 18),
    ],
    cctp=['']
)

moonbeam = Chain(
    name= 'moonbeam',
    rpc_url=os.getenv('MOONBEAM_RPC'),
    bridge_address='0x84A420459cd31C3c34583F67E0f0fB191067D32f',
    multisig='0xbb227Fcf45F9Dc5deF87208C534EAB1006d8Cc8d',
    swap_addresses=[],
    tokens=[
        ("MOVR", "0x1d4C2a246311bB9f827F4C768e277FF5787B7D7E", 18),
        # ("SOLAR", "0x0DB6729C03C85B0708166cA92801BcB5CAc781fC", 18),
        # ("USDC", "0x0F69F8Bef173b5543B11B117B426f7985caf05D2", 6),
        ("WETH", "0x3192Ae73315c3634Ffa217f71CF6CBc30FeE349A", 18),
        # ("MOON", "0xF119076756E8F5972c959e9Bb43a4A9cf346fc6E", 18),
        # ("ETH", "0x639D10EC273EB31fD8Bd667bE7cc2386F70cf6f6", 18),
    ],
    cctp=['']
)

optimism = Chain(
    name= 'optimism',
    rpc_url=os.getenv('OPTIMISM_RPC'),
    bridge_address='0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b',
    multisig='0x2431CBdc0792F5485c4cb0a9bEf06C4f21541D52',
    swap_addresses=[
        '0xF44938b0125A6662f9536281aD2CD6c499F22004',
        '0xE27BFf97CE92C3e1Ff7AA9f86781FDd6D48F5eE9',
    ],
    tokens=[
        ("ETH", "0x0000000000000000000000000000000000000000", 18),
        ("USDC", "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85", 6),
        ("DAI", "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1", 18),
        ("NETH", "0x809DC529f07651bD43A172e8dB6f4a7a0d771036", 18),
        # ("L2DAO", "0xd52f94DF742a6F4B4C8b033369fE13A41782Bf44", 18),
        # ("PLS", "0xD9eAA386cCD65F30b77FF175F6b52115FE454fD6", 18),
        # ("H2O", "0xE3c82A836Ec85311a433fBd9486EfAF4b1AFbF48", 18),
        # ("AGEUR", "0xa0554607e477cdC9d0EE2A6b087F4b2DC2815C22", 18),
        ("UNIDX", "0x28b42698Caf46B4B012CF38b6C75867E0762186D", 18),
        ("OP", "0x4200000000000000000000000000000000000042", 18),
        ("GOHM", "0x0b5740c6b4a97f90eF2F0220651Cca420B868FfB", 18),
        ("USDT", "0x94b008aA00579c1307B0EF2c499aD98a8ce58e58", 6),
        ("SYN", "0x5A5fFf6F753d7C11A56A52FE47a177a87e431655", 18),
        ("NUSD", "0x67C10C397dD0Ba417329543c1a40eb48AAa7cd00", 18),
        ("USDC.e", "0x7F5c764cBc14f9669B88837ca1490cCa17c31607", 6),
        ("SUSD", "0x8c6f28f2F1A3C87F0f938b96d27520d9751ec8d9", 18),
        ("WETH", "0x121ab82b49B2BC4c7901CA46B8277962b4350204", 18),
    ],
    cctp=['0x5e69c336661dde70404e3345ba61f9c01ddb4c36','0x12715a66773BD9C54534a01aBF01d05F6B4Bd35E']
)

polygon = Chain(
    name= 'polygon',
    rpc_url=os.getenv('POLYGON_RPC'),
    bridge_address='0x8F5BBB2BB8c2Ee94639E55d5F41de9b4839C1280',
    multisig='0xBdD38B2eaae34C9FCe187909e81e75CBec0dAA7A',
    swap_addresses=[
        '0x3f52E42783064bEba9C1CFcD2E130D156264ca77',
        '0x96cf323E477Ec1E17A4197Bdcc6f72Bb2502756a',
        '0x85fCD7Dd0a1e1A9FCD5FD886ED522dE8221C3EE5'
    ],
    tokens=[
        ("MATIC", "0x0000000000000000000000000000000000001010", 18), 
        ("WMATIC", "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270", 18),
        ("USDC.e", "0x2791bca1f2de4661ed88a30c99a7a9449aa84174", 6), 
        ("WETH", "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619", 18),
        ("USDT", "0xc2132d05d31c914a87c6611c10748aeb04b58e8f", 6),
        # ("DOG", "0xeEe3371B89FC43Ea970E908536Fcddd975135D8a", 18),
        # ("H20", "0x32ba7cF7d681357529013de6a2CDF93933C0dF3f", 18),
        # ("NFD", "0x0a5926027d407222f8fe20f24cb16e103f617046", 18),
        ("DAI", "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063", 18),
        ("SYN", "0xf8f9efc0db77d8881500bb06ff5d6abc3070e695", 18),
        ("GOHM", "0xd8cA34fd379d9ca3C6Ee3b3905678320F5b45195", 18),
        ("NUSD", "0xb6c473756050de474286bed418b77aeac39b02af", 18),
    ],
    cctp=['0x12715a66773BD9C54534a01aBF01d05F6B4Bd35E']
)

klaytn = Chain(
    name= 'klaytn',
    rpc_url=os.getenv('KLAYTN_RPC'),
    bridge_address='0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b',
    multisig='0x8f17B483982d1CC09296Aed8F1b09Ad830358A8D',
    swap_addresses=[],
    tokens=[
        ("KLAY", "0x0000000000000000000000000000000000000000", 18),
        ("WKLAY", "0x5819b6af194a78511c79c85eA68d2377a7e9335F", 18),
        ("WBTC", "0xDCbacF3f7a069922E677912998c8d57423C37dfA", 8), 
        ("LINK", "0xfbed1abb3ad0f8c467068de9fde905887e8c9118", 18),
        ("USDC_DFK", "0xa55BDAf93FE8F085d5496e2846F9CA721De86574", 6),
        ("USDT", "0xd6dAb4CfF47dF175349e6e7eE2BF7c40Bb8C05A3", 6),
        ("WETH", "0xCD6f29dC9Ca217d0973d3D21bF58eDd3CA871a86", 18),
        ("JEWEL", "0x30C103f8f5A3A732DFe2dCE1Cc9446f545527b43", 18),
        ("AVAX", "0xCd8fE44A29Db9159dB36f96570d7A4d91986f528", 18),
        ("USDC", "0x6270B58BE569a7c0b8f47594F191631Ae5b2C86C", 6),
        ("DAI", "0x078dB7827a5531359f6CB63f62CFA20183c4F10c", 18),
        ("BTCB", "0xe82f87ba4E97b2796aA0Fa4eFB06e8f0d2EB4FE1", 8),
    ],
    cctp=['']
)
