import pymongo
import certifi


con_string = "mongodb+srv://test:test@cluster0.nvjfa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("organika")