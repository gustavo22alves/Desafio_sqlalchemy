import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://gustavodeoliveira_sjc:<password>@cluster0.yaa3shz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
posts = db.posts

for post in posts.find():
    print.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({'author':'Mike'}))
print(posts.count_documents({'tags':'Mongo'}))

print.pprint(posts.find_one({'tags':'insert'}))


# RECUPERANDO INFO DA COLEÇAO POST DE MANEIRA ORDENADA...
for post in posts.find({}).sort('data'):
    print.pprint(post)

result = db.profiles.create_index([('author', pyM.ASCENDING)], unique = True)

print(sorted(list(db.profiles.index_information())))

user_profile1 = [
    {'user_id': 211, 'name':'luke'},
    {'user_id': 212, 'name':'Joao'}
]

result = db.profiles_user.insert_many(user_profile1)

print('\nCOLEÇOES ARMAZENADAS NO MONGOBD')
collections = db.list_collection_names()

for collection in collections:
    print(collection)


# APAGANDO A COLEÇAO POSTS
db['posts'].drop()

for post in posts.find():
    print.pprint(post)

print(db.profiles_user.drop())


client.drop_database('test')










