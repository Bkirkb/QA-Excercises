from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra
testuser2 = Users(first_name='Michael', last_name='Trent') # Another test user
testuser3 = Users(first_name='Michel', last_name='Trunt') # Another test user

db.session.add(testuser)
db.session.add(testuser2)
db.session.add(testuser3)
db.session.commit()