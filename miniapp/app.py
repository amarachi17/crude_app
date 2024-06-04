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
mysql = MySQL(app)

# Function to create student details
@app.route('/index', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('index.html')
    
    if request.method == "POST":
        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str, hobby))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        year = request.form['year']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO information (first_name, last_name, email, password, gender, hobbies, year) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                    (first_name, last_name, email, password, gender, hobbies, year))
        mysql.connection.commit()
        cur.close()

        return redirect('/')

# Function to create student list       
@app.route('/', methods=['GET','POST'])
def StudentList():
    try:
        cur = mysql.connection.cursor()
        cur.execute("select * from information")
        data = cur.fetchall()
        cur.close()
        return render_template('list.html', data=data)
        
    except Exception as e:
        return str(e)

# Function to create student update by id   
@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM information WHERE id=%s", (id,))
        edit = cur.fetchone()
        cur.close()
        
        if request.method == 'POST':
            hobby = request.form.getlist('hobbies')
            hobbies = ",".join(map(str, hobby))
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            hobbies = hobbies
            year = request.form['year']
            
            cur = mysql.connection.cursor()
            cur.execute("UPDATE information SET first_name=%s, last_name=%s, email=%s, password=%s, gender=%s, hobbies=%s, year=%s WHERE id=%s",
                        (first_name, last_name, email,password, gender, hobbies, year, id))
            mysql.connection.commit()
            cur.close()
            return redirect('/')
        
        return render_template('update.html', edit=edit)
    
    except Exception as e:
        return str(e)
        
# Function to create student delete by id 
@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM information WHERE id=%s", (id,))
    dele = cur.fetchone()
    cur.close()
    
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM information WHERE id=%s", (id,))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    return render_template('delete.html', dele=dele)

 