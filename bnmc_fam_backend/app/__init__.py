from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS
from flask import Flask
import rsa

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

CORS(app)

# Load the config file
app.config.from_object('config')

# Connect to DB
print("hereDB")
print(app.config["DEBUG"])

keydata = None
encUri=None

with open(app.config["MONGODB_CRED_URI"], mode='rb') as encUrifile:
    encUri = encUrifile.read()

with open(app.config["MONGODB_CRED_PRIVATE_KEY_PATH"], mode='rb') as privatefile:
    keydata = privatefile.read()

privkey = rsa.PrivateKey.load_pkcs1(keydata)

uri = rsa.decrypt(encUri, privkey).decode()

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
for dbs in client.list_databases():
    print(dbs)
db = client['BNMC-FAM']
collection = db['Resources']

# Load the views and models
from app import views,models
