from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")  

client = MongoClient(config["MONGODB_URI"])
print("MDB connected successfully", client)

db = client.raw_data
collection_name = db["sample_collection"]
