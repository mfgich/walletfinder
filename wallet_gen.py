from bitcoinaddress import Wallet
import requests
import json
import time

counter = 0
def getRich():
    wallet = Wallet()
    wa = str(wallet)
    wa1 = wa.splitlines(False)
    wal1 = str(wa1[13])
    wal2 = wal1.split(sep=":")
    qaddr = wal2[-1]
    qaddr1 = qaddr.split(sep=" ")
    qwerywallet = str(qaddr1[1])
    print(qwerywallet)

    url = "https://blockchain.info/rawaddr/"+qwerywallet
    btc_addr = requests.get(url)
    dict_addr = json.loads(btc_addr.text)
    balance = dict_addr.get("final_balance")

    if balance != "":
        datei = "wallet"+str(counter)+".txt"
        dat = open(datei, "wt")
        dat.write(wa)
        dat.close()
    else:
        counter +1
        print(counter)
        time.sleep(15) 
        # nicht unter 11 Secunden da sonst die Anfragen von der IP geblockt werden
        getRich()
getRich()