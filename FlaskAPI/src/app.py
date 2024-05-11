from flask import Flask, render_template
import os

from config.mongodb import mongo
from routes.logsRoutes import logs
from routes.usersRoutes import users

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGOURI')
mongo.init_app(app)

app.register_blueprint(logs, url_prefix='/api/logs')
app.register_blueprint(users, url_prefix='/api/users')

@app.route('/')
def index():
    return render_template('index.html')