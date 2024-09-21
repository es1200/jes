from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
  return ""

@app.get("/.well-known/atproto-did")
def inscrito():
  return "did:plc:3sqrtb7n3gya7w7567eceqku"

if __name__ == "__main__":
  app.run()
