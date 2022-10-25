from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',port=8080)

def getInfo(network, address):
    url = "https://solana-gateway.moralis.io/nft/" + network + "/" + address + "/metadata"
    headers = {
        "accept": "application/json",
        "X-API-Key": "a5R4WCSyiPb3tWXq6kDkQ8D21ZWnVMdtmgLzbBnYO7vIWlcuj8dRjoNb6RCs0qbZ"
    }
    response = requests.get(url, headers=headers)
    return response
