from flask import Flask, request
import requests
import json


app = Flask(__name__)

SNS_TYPE = "X-Amz-Sns-Message-Type"
SNS_CONFIRMATION = "SubscriptionConfirmation"
SNS_SUB_URL = "SubscribeURL"


@app.route("/")
def hello():
    print("headers == \n", request.headers)
    print("values == \n", request.values)
    return "hello world"

@app.route("/sns", methods=['POST'])
def sns():
    data = json.loads(request.data)
    print("data == ", data)
    if request.headers.get(SNS_TYPE) == SNS_CONFIRMATION:
        print("receive sns confirmation")
        sub_url = data.get(SNS_SUB_URL)
        print("sub url == ", sub_url)
        r = requests.get(sub_url)
        print("requests result == ", r)

    print("headers == \n", request.headers)
    print("values == \n", request.values)
    return "hello world"

if __name__ == "__main__":
    app.run(port=8888)
