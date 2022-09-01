from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os, firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

firestore_db = firestore.client()

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
PUBLIC_IP = os.getenv('PUBLIC_IP')
DB_NAME = os.getenv('DB_NAME')
PROJECT_ID = os.getenv('PROJECT_ID')
REGION = os.getenv('REGION')
INSTANCE_NAME = os.getenv('INSTANCE_NAME')

app = Flask(__name__)
env = 'PROD'
if env == 'DEV':
    # Conn to dev db
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/{DB_NAME}'
    # Conn to prod db from local
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{PUBLIC_IP}:5432/{DB_NAME}"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@/{DB_NAME}?host=/cloudsql/{PROJECT_ID}:{REGION}:{INSTANCE_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
    
db = SQLAlchemy(app)

