from brownie import accounts, config, network


def get_account():
    if network.show_active() == "development":
        return accounts[0]

    else:
        # get wallet key from .env
        return accounts.add(config["wallets"]["from_key"])
