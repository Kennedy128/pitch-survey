from app import create_app,db
from flask_script import Manager, Server
from app.models import User, Pitch, Category,Comment
from flask_migrate import Migrate, MigrateCommand

#create app instance
app = create_app("development")

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Category= Category, Pitch = Pitch,Comment = Comment)

if __name__ == '__main__':
    manager.run()