import os
from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Role #User model in our models.py
from flask_migrate import Migrate, MigrateCommand #import migrate class

# Creating app instance
app = create_app('development')
migrate = Migrate(app,db) #initialize the Migrate class and pass in the app instance and the db SQLAlchemy instance


manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand) #create a new manager command 'db' and pass in the MigrateCommand class.
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User , Role=Role)

if __name__ == '__main__':
    manager.run()