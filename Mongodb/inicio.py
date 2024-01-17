import pymongo as pyM
import datetime as datetime

client = pyM.MongoClient('mongodb+srv://gustavodeoliveira_sjc:<password>@cluster0.yaa3shz.mongodb.net/?retryWrites=true&w=majority')

db = client.test

collection = db.test_collection

print(db.list_collection_names)

post = {
    'author':'Mike',
    'text':'My first mongodb application based on python',
    'tags':['mongodb','python3','pymongo'],
    }

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.posts.find_one())

print.pprint(db.posts.find_one())  #PRINTA DE FORMA O QUAL FICA INFO EMBAIXO DE INFO.

# BULKS INSERTS... CRIA-SE UMA LISTA... PODENDO SER INSERIDO UMA QUANTIDADE MAIOR DE INFORMAÇOES.

new_posts = [{
    'autor':'Mike',
    'text': 'Another post',
    'tags':['bulk','post','insert']
},
{   
    'autor': 'Joao',
    'text':'Post from Joao. New post available',
    'title':'Mongo is fun'
}]

result = posts.insert_many(new_posts)

print.pprint(new_posts)

print('\nRecuperação final')
print.pprint(db.posts.find_one({'autor':'Joao'}))

print.pprint(posts.find())

# RECUPERAÇÃO POST 

for post in posts.find():
    print.pprint(post)





