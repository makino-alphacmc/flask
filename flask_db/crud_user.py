from app import db, User

user3 = User("test_user@example.com", "Test User3", "333")
db.session.add(user3)
db.session.commit()

#全レコードの取得
all_users = User.query.all()
print(all_users)

#レコードの取得(ID指定)
userid_1 = User.query.get(1)
print(userid_1.username)

#レコードの取得(条件指定)
username_user2 = User.query.filter_by(username="Test User2")
print(username_user2.all())

#レコードの更新
user_id_1 = User.query.get(1)
user_id_1.username = "TestUserA"
db.session.add(user_id_1)
db.session.commit()

#レコードの削除
user_id_2 = User.query.get(2)
db.session.delete(user_id_2)
db.session.commit()

#全レコードの取得
all_users = User.query.all()
print(all_users)