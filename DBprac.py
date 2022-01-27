#pymongo도 기본 코드가 존재한다.
#따라서 이 기본 코드를 mongo를 쓰기 전에 먼저 써 넣어야 한다.
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#-------------기본 코드 ----------

# inset, find, update, delete를 기억하자.

#insert 사용하기
# doc = {'name':'jane','age':21}
# db.users.insert_one(doc)

# same_ages = list(db.users.find({},{'_id':False}))
#
# for person in same_ages:
#     print(person)

# user = db.users.find_one({'name':'bobby'},{'_id':False})
#
# print(user['age'])

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

db.users.delete_one({'name':'bobby'})