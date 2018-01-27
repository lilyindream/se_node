""""
远程操作mongodb
api.mongodb.com/python/current/tutorial.html
"""

from pymongo import MongoClient
client = MongoClient('mongodb://118.31.19.120:27017/')
"""激活注册的账号"""
print(client.database_names)

db=client.get_database('node_club_dev')

collections = db.collection_names()

print(collections)
users = db.get_collection('users')
print(users)
users.find_one_and_update({"loginname":"lilytest"},{'$set':{"active": True}})

