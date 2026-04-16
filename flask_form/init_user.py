from app import db, User

# データベースの初期化とユーザーの追加。
# 既存のテーブルを削除してから再作成する場合は、db.drop_all()を使用。注意: データが失われる。

db.drop_all()
db.create_all()

user1 = User("admin_user1@test.com", "Admin_user1", "111", "1")
user2 = User("test_user1@test.com", "Test_user1", "111", "0")

db.session.add_all([user1, user2])

db.session.commit()

print(f"ユーザーの追加が完了しました。{user1}, {user2}")
