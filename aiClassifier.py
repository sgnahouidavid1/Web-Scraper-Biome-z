from pymongo import MongoClient
# Use for connecting to mongo.
# import certifi
import json
import yaml
from aiBSP import *

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

allRecords = collection.find()
for record in allRecords:
    doi = record['doi']
    
    title = record['title']
    abstract = record['abstract']

    autoTags = { "autoTags": record['autoTags']}

    paragraph = title + ' ' + abstract

    # Run AI here. Output is Tags.
    tags = categorize_bps(paragraph)

    newTags = { "$set": { "autoTags": tags} }
    collection.update_one(autoTags, newTags)

    cursor = collection.find({"doi": doi})
    for doc in cursor:
        db["records"].insert_one(doc)
        collection.delete_one({"doi": doi})

