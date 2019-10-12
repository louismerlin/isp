from flask import Flask, request, make_response
import hmac
import time
import math
import binascii
import base64

app = Flask(__name__)

cookie_name = "LoginCookie"
key = binascii.unhexlify("e179017a62b049968a38e91aa9b1")

@app.route("/login",methods=['POST'])
def login(): 
    username = request.form['username']
    password = request.form['password']
    status = "user"
    if (username == "admin") and (password == "42"):
        status = "admin"
    cookie = "%s,%s,com402,hw2,ex3,%s," % (username, math.floor(time.time()), status)
    h = hmac.new(key, cookie.encode())
    cookie += h.hexdigest()
    resp = make_response()
    resp.set_cookie(cookie_name, base64.b64encode(cookie.encode("utf-8")))
    return resp

@app.route("/auth",methods=['GET'])
def auth():
    cookie = request.cookies.get(cookie_name)
    if cookie == "":
        return '', 403
    cookie = base64.b64decode(str.encode(cookie)).decode("utf-8")
    cookieHash = cookie.split(',')[-1]
    toHash = ','.join(cookie.split(',')[0:-1]) + ","
    h = hmac.new(key, toHash.encode())
    if not hmac.compare_digest(h.hexdigest(), cookieHash):
        return '', 403
    if cookie.split(',')[-2] == 'admin':
        return '', 200
    if cookie.split(',')[-2] == 'user':
        return '', 201
    return '', 400

if __name__ == '__main__':
    app.run()
