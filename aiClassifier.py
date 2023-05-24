from pymongo import MongoClient
# Use for connecting to mongo.
# import certifi
import json
import yaml

# Pull URI string from yaml file.
config = yaml.safe_load(open('db.yaml'))

# Attempt to establish MongoDB connection using the URI string.
try:
    client = MongoClient(config['uri'])
    # Use this version below if the one above doesn't work.
    # client = MongoClient(config['uri'], tlsCAFile = certifi.where())

    print("\nSuccessfully connected to MongoDB.\n")
except:
    print("\nCould not establish MongoDB connection.\n")

# Access 'biomez' database and 'raw_records' collection that will store uncategorized, web-scraped articles.
db = client['biomez']
collection = db.raw_records

# Output of the AI.
tags = "Bio, Distal"

allRecords = collection.find()
for record in allRecords:
    doi = record['doi']
    
    autoTags = { "autoTags": record['autoTags']}

    # Run AI here. Output is Tags.

    newTags = { "$set": { "autoTags": tags} }
    collection.update_one(autoTags, newTags)

    cursor = collection.find({"doi": doi})
    for doc in cursor:
        db["records"].insert_one(doc)
        collection.delete_one({"doi": doi})
    

