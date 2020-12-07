from app import db, Countries, Cities

db.drop_all() # Deletes all tables etc
db.create_all() # Creates new tables etc

uk = Countries(name = 'United Kingdom') # add example to countries table
db.session.add(uk)
db.session.commit()

ldn = Cities(name = 'London', country = uk)
mcr = Cities(name = 'Manchester', country = Countries.query.filter_by(name='United Kingdom').first())
lvp = Cities(name='Liverpool', country = uk)

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()