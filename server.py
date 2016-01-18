from flask import Flask, redirect
from flask import render_template
from api_tools import outlook_api

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/ms_login")
def ms_login():
  api = outlook_api.OutlookAPI()
  return redirect(api.get_authorization_url('http://localhost:5000'))

if __name__ == "__main__":
  app.run()

