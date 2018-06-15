from flaskproject import create_application
from flaskproject.config import Config

# setup any "custom" configuration options you need below
conf = Config()
Config.SQLALCHEMY_DATABASE_URI = "mysql://remote_read_write:rrw4th1s@192.168.1.170:3306/flaskbb_test_db"
Config.SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
Config.SQLALCHEMY_TRACK_MODIFICATIONS = False
# create the application instance
app = create_application(conf)

# this starts the Flask process
if __name__ == '__main__':
    app.run(debug=True, host="localhost")
