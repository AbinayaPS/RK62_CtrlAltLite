from flask import Flask, render_template, redirect, url_for, request
import pyotp
import requests
import re
import json

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

def isValidPhNo(phno):
    pattern = re.compile("[6-9][0-9]{9}")
    return pattern.match(phno)

def getOTP():
    totp = pyotp.TOTP('base32secret3232')
    totp.interval = 180
    otp = totp.now()
    return otp
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        phno = request.form['phno']
        if not isValidPhNo(phno):
            error = 'Invalid Credentials. Please try again.'
        else:
            otp = getOTP()
            #SMS Configuration
            url = "https://www.fast2sms.com/dev/bulk"
            payload = "sender_id=FSTSMS&message=" + otp +"&language=english&route=p&numbers=" + request.form['phno']
            headers = {
            'authorization': "lp5vMe6bcjQZEIk1aGKHgt7UroNfxYuRLdOSDCTh904VqiyF8wApboRLyjIlxBXc6HgFzN7V0Yfa2kGq",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            return redirect(url_for('authenticate'))
    return render_template('login.html', error=error)

def isValidOTP(otp):
    pattern = re.compile("[0-9]{6}")
    if pattern.match(otp):
        original = getOTP()
        return otp == original
    else:
        return False
@app.route('/authenticate', methods=['GET','POST'])
def authenticate():
    error = None
    if request.method == 'POST':
        if not isValidOTP(request.form['otp']):
            error = 'Invalid OTP.'
        else:
            return redirect(url_for('index'))
    return render_template('authenticate.html',error=error)

"""@app.route('/index', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
      val = str(request.args.get('text'))
      data = json.dumps({"sender": "Rasa","message": val})
      headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
      res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
      res = res.json()
      val = res[0]['text']
      return render_template('index.html', val=val)"""

@app.route('/index', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
