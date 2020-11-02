import  os
from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, '/uploads')
app.config['SECRET_KEY'] = 'cb035d9e3ac1d65c1c37a4af8aa31b1e'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from intelense import routes
