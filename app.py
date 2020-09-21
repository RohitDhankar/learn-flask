from flask import Flask , render_template , url_for , request , redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 
from flask_mysqldb import MySQL 

app = Flask(__name__)
# above for providing - root DIR of relative paths 
# MySQL 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dhankar'
app.config['MYSQL_PASSWORD'] = 'dhankPass_!@#_09*'
app.config['MYSQL_DB'] = 'flask_schema'
mysql = MySQL(app)
print(mysql) #<flask_mysqldb.MySQL object at 0x7f478c7d0f40>

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
    #cur.execute("SELECT * FROM flask_schema.users")
    cur.execute("SELECT * FROM flask_schema.mtcars")
    fetchdata = cur.fetchall()
    #print(fetchdata) # OK
    #print(type(fetchdata)) #<class 'tuple'>


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