import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/demandradar'

# Test if environment variables are loaded
if __name__ == '__main__':
    print(f"SECRET_KEY is set: {'SECRET_KEY' in os.environ}")
    print(f"MONGO_URI is set: {'MONGO_URI' in os.environ}")