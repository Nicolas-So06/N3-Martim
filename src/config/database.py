from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("CONNECTION_STRING")

client = MongoClient(connection_string)
db = client['martimdb']
collection = db['clients']