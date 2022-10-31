from web3 import Web3
import web3
import config
w3= Web3(Web3.HTTPProvider(config.INFURA_URL))

print (w3.eth.block_number)
balance = w3.eth.get_balance('0x098B716B8Aaf21512996dC57EB0615e2383E2f96')
ether_balance = w3.fromWei(balance , 'ether')
print (ether_balance)


 <tr>
        <td>transaction detail</td>
        <td>{{transaction.detail}}</td>
    </tr>
    <tr>
        <td>blockHash</td>
        <td>{{transaction.blockHash}}</td>
    </tr>
    <tr>
        <td>transaction blockNumber</td>
        <td>{{transaction.blockNumber}}}</td>
    </tr>