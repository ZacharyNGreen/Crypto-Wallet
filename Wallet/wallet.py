 
import subprocess
import json
from constants import *

mnemonic =  os.getenv('MNEMONIC', 'write place dash similar hello lazy open raw visual harbor length bicycle')




p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, error) = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys[0]['address'])

#Set up mnemonic

class Coins:

    def_init_(self,mnemonic,coin,numderive):
        def create_command(mnemonic, coin):
            command = f'../Blockchain-Tools/derive -g --mnemonic={mnemonic} --cols=path,address,privkey,pubkey --coin={coin} --format=json'
            return create_command


       for j in coin:
            #create bitcoin children
            coin_child[j]=[]
            for i in numderive:
                bitcoin_children[i]=createcommand(mnemonic,coin[j])

    return self


#create transactions function
def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }

#send transactions function
def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()
       
#initialize Coins object
coins=["eth","btc-test"]



myWallet=Coins.__init__(self,coins, 3)


signed.rawTransaction=create_raw_tx(myWallet["eth"][1]['privkey'])
signed=create_raw_tx(myWallet["btc_test"][1]['privkey'])

#send ethereum transaction:
w3.eth.sendRawTransaction(signed.rawTransaction)
NetworkAPI.broadcast_tx_testnet(signed)





    
        





