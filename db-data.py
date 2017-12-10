from server.models.Base import Base, engine, db_session
from server.models.User import User
from server.models.Devotional import Devotional
from server.models.Comment import Comment
from datetime import datetime

def print_user(user):
    print('Id: {}'.format(user.id))
    print('Email: {}'.format(user.email))
    print('First name: {}'.format(user.first_name))
    print('Last name: {}'.format(user.last_name))

def print_devo(devo):
    print('Id: {}'.format(devo.id))
    print('Title: {}'.format(devo.title))
    print('Body: {}'.format(devo.body))

def print_comm(comment):
    print('Id: {}'.format(comment.id))
    print('Body: {}'.format(comment.body))

"""
Base.metadata.create_all(bind=engine)
user1 = User(email='sebita.urbina@gmail.com', first_name='Sebastian', last_name='Urbina')

db_session.add(user1)

db_session.commit()
"""
user2 = User.query.filter_by(first_name='Sebastian').first()

"""
print('User 1')
print_user(user1)
"""

print('User 2')
print_user(user2)

"""
devo_data = {
    'title': 'titulo loco',
    'passage': '1 cor 3.5',
    'body': 'el contenido del devo',
    'creation_date': datetime(2017, 12, 10),
    'publish_date': datetime(2017, 12, 11),
    'publish_status': 'DRAFT',
    'author_id': 1
}

devo = Devotional(**devo_data)

db_session.add(devo)
db_session.commit()
"""

devo1 = Devotional.query.filter_by(title='titulo loco').first()
print('Devo 1')
print_devo(devo1)

"""
comment_data = {
    'body': 'el comentario re loco',
    'author_id': 1,
    'devotional_id': 1
}

comm = Comment(**comment_data)
db_session.add(comm)
db_session.commit()
"""

comm1 = Comment.query.filter_by(body='el comentario re loco').first()
print('Comment 1')
print_comm(comm1)
