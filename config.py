# configure the app
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """ Base configuration reading from .env file"""
    DEBUG = True
    # SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_ADDRESS")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]

    # Generated secret key for user authentication 
    SECRET_KEY = '3697993477dc2bef2215fb9cf7f1e638'
