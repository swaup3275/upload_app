
from app import db
from models import *
 
 
# create the database and the database table
db.create_all()
 
# insert recipe data
result1 = Result('hello this is the first url!')
result2 = Result('second url will be here')
result3 = Result('time for the 3rd url.')
db.session.add(result1)
db.session.add(result2)
db.session.add(result3)
 
# commit the changes
db.session.commit()
