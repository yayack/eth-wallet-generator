from eth_account import Account
from web3 import Web3
import secrets
import os
from time import sleep

os.system("clear")
print("\n\n\n")
print("      ------  script by : yayack_13  ------")
print("      -------------------------------------")
print("      -------  Ox wallet generator  -------")
print("      -  auto generate mnemonic 12 words  -")
print("      -------------------------------------\n")
def script():
    file = open("mnemonic.txt","w")
    file1 = open("wallet.txt","w")
    jumlah = input("-How much wallet? ( example : 100 ) : ")
    print("\n")
    no = 0-1
    for muter in range(int(jumlah)):
        no = no + 1
        Account.enable_unaudited_hdwallet_features()
        acct, mnemonic = Account.create_with_mnemonic()
        print("-wallet number : "+str(no+1))
        print("-Address : "+acct.address)
        print("-Mnemonic : "+mnemonic)
        file.write(str(no+1)+".Mnemonic : "+str(mnemonic)+"\n  Address : "+str(acct.address)+"\n")
        file1.write(str(acct.address)+"\n")
try:
    script()
    print("\n\n-wallet successfully saved in wallet.txt\n-mnemonic successfully saved in mnemonic.txt\n\n")
except ModuleNotFoundError:
    print("\n\nmake sure you have installed all of the module required to run this program\n\n")
except KeyboardInterrupt:
    print("Interrupted")
