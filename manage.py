import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db


#app.config.from_object(os.environ[''])
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///resume_store"

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()