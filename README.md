
# Police and Thief Game Fork

A fork of police and thief game smart contract

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```
Or, if that doesn't work, via pipx
```bash
pip install --user pipx
pipx ensurepath
# restart your terminal
pipx install eth-brownie
```

2. Clone this repo
```
brownie compile
brownie run scripts/deploy.py
```

deploy to testnets,

4. Set your environment variables

 You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/).


You can add your environment variables to the `.env` file:

```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

Then, make sure your `brownie-config.yaml` has:

```
dotenv: .env
```


Any questions? hit me up [Twitter](https://twitter.com/royaliben)

## License

[MIT license](LICENSE).