#!/usr/bin/env python3
import os
import sys
import populate
from flask import g
from flask import Flask, current_app
from flask import render_template, request, jsonify
import pymysql


app = Flask(__name__)
username = "root"
password = "root"
database = "hw5_ex2"

## This method returns a list of messages in a json format such as 
## [
##  { "name": <name>, "message": <message> },
##  { "name": <name>, "message": <message> },
##  ...
## ]
## If this is a POST request and there is a parameter "name" given, then only
## messages of the given name should be returned.
## If the POST parameter is invalid, then the response code must be 500.
@app.route("/messages",methods=["GET","POST"])
def messages():
    with db.cursor() as cursor:
        json = ""
        name = None
        if request.method == "POST":
            name = request.form["name"]
        if name != None:
            sql = "SELECT `name`, `message` FROM `messages` WHERE `name`=%s"
            cursor.execute(sql, (name))
        else:
            sql = "SELECT `name`, `message` FROM `messages`"
            cursor.execute(sql)
        json = cursor.fetchall()
        header = [x[0] for x in cursor.description]
        json_data = []
        for result in json:
            json_data.append(dict(zip(header, result)))
        return jsonify(json_data),200


## This method returns the list of users in a json format such as
## { "users": [ <user1>, <user2>, ... ] }
## This methods should limit the number of users if a GET URL parameter is given
## named limit. For example, /users?limit=4 should only return the first four
## users.
## If the paramer given is invalid, then the response code must be 500.
@app.route("/users",methods=["GET"])
def contact():
    with db.cursor() as cursor:
        limit = request.args.get("limit")
        lim = 0
        if limit != None:
            try:
                lim = int(limit)
            except ValueError:
                return "", 500
        if lim < 0:
            return "", 500
        json = ""
        if lim > 0:
            sql = "SELECT `id`, `name`, `password` FROM `users` LIMIT %s"
            size = cursor.execute(sql, (lim))
            if size == 0:
                return "",500
        else:
            sql = "SELECT `id`, `name`, `password` FROM `users`"
            cursor.execute(sql)
        json = cursor.fetchall()
        header = [x[0] for x in cursor.description]
        json_data = []
        for result in json:
            json_data.append(dict(zip(header, result)))
        return jsonify(users=json_data)

if __name__ == "__main__":
    seed = "randomseed"
    if len(sys.argv) == 2:
        seed = sys.argv[1]

    db = pymysql.connect("localhost",
                username,
                password,
                database)
    with db.cursor() as cursor:
        populate.populate_db(seed,cursor)             
        db.commit()
    print("[+] database populated")

    app.run(host='0.0.0.0',port=80)
