from db import LikeDB

like_db = LikeDB('data.json')

# print(like_db.add_student('32343'))
print(like_db.all_likes('12343'))