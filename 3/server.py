from flask import Flask, request
import bcrypt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hash_password(): 
  data = request.json
  hashed = bcrypt.hashpw(data['pass'].encode(), bcrypt.gensalt())
  return hashed, 200

if __name__ == "__main__":
  app.run()
