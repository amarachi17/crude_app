from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration of MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'studentData'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initializing MySQL

# Function to create student details
@app.route('/', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('index.html')
