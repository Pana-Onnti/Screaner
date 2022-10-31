from web3 import Web3
#import ccxt 
from flask import Flask, render_template 
import config

w3= Web3(Web3.HTTPProvider(config.INFURA_URL))

app = Flask(__name__)

#stock = yf.Ticker("ETH-USD")

#@app.route('/')
#def home (): 
#    binance = ccxt.binance ()
#    ethereum_price = binance.fetch_ticker('ETH/USDC')
#    return render_template('home.html', ethereum_price= ethereum_price)

@app.route('/')
def home ():
    ethereum_price = int(1400)
    return render_template('home.html', ethereum_price= ethereum_price)

@app.route("/tx/<hash>")
def transaction(hash):
    transaction = w3.eth.get_transaction(hash)
    return render_template('transaction.html', hash=hash, transaction=transaction
    )


@app.route("/address/<addr>")
def adress(addr):
    return render_template("address.html", addr=addr)


@app.route("/block/<block_number>")
def block (block_number):
    return render_template("block.html", block_number=block_number)












if __name__== "__main__":
    app.run(debug=True)
    