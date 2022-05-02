from brownie import DaisyCoin, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    daisy_coin = DaisyCoin.deploy(
        initial_supply, {"from": account}, publish_source=True
    )
    print(daisy_coin.name())
