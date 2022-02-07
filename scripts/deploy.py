from brownie import PoliceAndThief, config, network, config
from scripts.helper import get_account
from web3 import Web3


def deploy_project():
    account = get_account()
    # if not in development use production pricefeed address for contract
    if network.show_active() != "development":
        myContract = PoliceAndThief.deploy({"from": account})


def main():
    deploy_project()
