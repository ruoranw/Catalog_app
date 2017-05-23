from flask import Flask , render_template, request,redirect, url_for, flash , jsonify

# Import CRUD Operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, Class

# Create an instance of this class with the name of running application as the argument
app = Flask(__name__)
engine = create_engine('sqlite:///studentclass.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Making an API Endpoint
# These two are decorators
@app.route('/')
@app.route('/students/', methods=['GET','POST'])

def studentClass():
    students = session.query(Student).all()
    print students



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8030)