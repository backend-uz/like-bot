from db import LikeDB

like_db = LikeDB('data.json')

print(like_db.all_likes('12321'))