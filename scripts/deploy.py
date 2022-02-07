from brownie import Bank, config, network, config
from scripts.helper import get_account
from web3 import Web3


def deploy_project():
    account = get_account()
    myContract = Bank.deploy(
        "0x3032E78978A96A7a0907883631aC227F542357e2",
        "0x3032E78978A96A7a0907883631aC227F542357e2",
        {"from": account},
    )
    # if not in development use production pricefeed address for contract
    # if network.show_active() != "development":
    #     myContract = PoliceAndThief.deploy('0x3032E78978A96A7a0907883631aC227F542357e2', '0x3032E78978A96A7a0907883631aC227F542357e2', {"from": account})


def main():
    deploy_project()
