from datetime import datetime
from flaskproject.database import database

"""
For the models you need at minimum the database since you need to extend database.Model on your models.
I've also imported the datetime.datetime module as it's easy to use as a default for DateTime columns.

I've included a "User" model as an example.
"""


class User(database.Model):
    # Auto incrementing by default due to primary_key status
    id = database.Column(database.Integer, primary_key=True)
    # Unique string field, not nullable (e.g NOT NULL in SQL)
    username = database.Column(database.String(120), unique=True, nullable=False)
    # same, but not Unique since people can have the same password, be sure to use hashing
    password = database.Column(database.String(120), nullable=False)
    # a text field
    bio = database.Column(database.Text, nullable=True)
    # date that can be used as the "registration" date, also shows the datetime.utcnow
    # NOTE: be sure not to call the utcnow, this needs to be a reference to a function
    create_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    # boolean flag, this will be either a Boolean (PosgresSQL etc) or a TinyInt(1) (MySQL etc)
    is_admin = database.Column(database.Boolean, nullable=False, default=False)
