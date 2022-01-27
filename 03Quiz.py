from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 1.매트릭스 평점 가져오기

# target_movie = db.movies.find_one({'title':'매트릭스'})
# print(target_movie['star'])

# 2. 매트릭스의 평점과 같은 평점의 영화 가져오기

# target_movie = db.movies.find_one({'title':'매트릭스'})
# target_star = target_movie['star']
#
# movies = list(db.movies.find({'star':target_star}))
#
# for movie in movies :
#     print(movie['title'])

# 3. 매트릭스 영화의 평점을 0으로 만들기.
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})

