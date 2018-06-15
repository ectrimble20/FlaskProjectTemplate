from flaskproject import create_application, crypt
from flaskproject.database import database
from flaskproject.config import Config

"""
Build is used to initially create the applications database, it doesn't technically do anything else except
build the database to the model.

This is useful while testing and can be used during a deployment BUT should not be used if production data
is already in place as data loss IS possible.

Be careful when using this.
"""
if __name__ == '__main__':
    # setup your configuration here, really you only need to setup the database URI
    # but you can setup other things if you need them
    test_config = Config()
    Config.SQLALCHEMY_DATABASE_URI = "mysql://remote_read_write:rrw4th1s@192.168.1.170:3306/flaskbb_test_db"
    app = create_application(test_config)
    with app.app_context():
        # drop the database, this just cleans the data (e.g. drops existing data)
        database.drop_all()
        # Load all models
        # from flaskproject.models import User, Car, Employee
        # build the database, this recreates the tables
        database.create_all()
        # do any table stuff we need here like default stuff
        # for instance if we need like a default admin user or some pre-set value
        # example:
        # database.session.add(User(username="admin", password="secret_password"))
        # database.session.add(Car(make="Toyota", model="Camery", year="1999"))
        # last, commit the new changes to the database.
        database.session.commit()
