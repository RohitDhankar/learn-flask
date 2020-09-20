from flask import Flask , render_template , url_for , request , redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 
from flask_mysqldb import MySQL 



app = Flask(__name__)
# MySQL 
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql_root_pass'
app.config['MYSQL_DATABASE_DB'] = 'schema_flask'
mysql = MySQL(app)
print(mysql) #<flask_mysqldb.MySQL object at 0x7f478c7d0f40>
"""
MySQLdb._exceptions.OperationalError
MySQLdb._exceptions.OperationalError: (1045, "Access denied for user 'dhankar'@'localhost' (using password: NO)")
"""

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#3 Fwd Slashes means - Relative path
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    content = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime , default = datetime.utcnow)# Time Stamp

    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/',methods=['POST','GET']) # Add methods to route -decorator



def index():
    # MySQL 
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users") #SQL
    fetchdata = cur.fetchall()
    print(type(fetchdata))


    if request.method == 'POST':
        task_content = request.form['content']
        new_task = todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()

            return redirect('/')
        except:
            print("Exception while creating a Task")
    else:
        tasks = todo.query.order_by(todo.date_created).all()
        #tasks = todo.query.order_by(todo.date_created).first()
        return render_template('index.html',tasks=tasks , data = fetchdata)

if __name__ == "__main__":
    app.run(debug=True)    