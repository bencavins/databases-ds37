import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://bencavins:Hn4q6c25cl8SkupC@cluster0.2vdvn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
db = client.test

# db.test.insert_one({'name': 'bob', 'age': 55})
# db.test.insert_one({'name': 'janet', 'age': 40})
# db.test.insert_one({'name': 'sam', 'age': 23})
# db.test.insert_many([{}, {}])
# db.test.insert_one({'key': 'value', 'sub_doc': {'abc': 999, 'xyz': 345}})

# print(db.test.count_documents({'number': 23}))

# print(db.test.find_one({}))

# db.test.delete_one({'test_key': 'test_value'})
db.test.update_one({'key': 'value'}, {'$set': {'name': 'rob'}})


cursor = db.test.find({})

for doc in cursor:
    print(doc)