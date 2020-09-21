# CFE Code - Flask  Server
from flask import Flask , render_template , url_for , request , redirect
from flask_sqlalchemy import SQLAlchemy 
#from datetime import datetime 
from flask_mysqldb import MySQL 

app_fServer = Flask(__name__)
#MySQL
app_fServer.config['MYSQL_HOST'] = 'localhost'
app_fServer.config['MYSQL_USER'] = 'dhankar'
app_fServer.config['MYSQL_PASSWORD'] = 'dhankPass_!@#_09*'
app_fServer.config['MYSQL_DB'] = 'flask_schema'
mysql = MySQL(app_fServer)
print(mysql) #<flask_mysqldb.MySQL object at 0x7f478c7d0f40>


@app_fServer.route('/flaskServer',methods=['GET']) # Add methods to route -decorator
def meth_flaskServer():
    """
    """
    # MySQL 
    cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM flask_schema.users")
    cur.execute("SELECT * FROM flask_schema.mtcars")
    fetchdata = cur.fetchall()
    #print(fetchdata) # OK
    #print(type(fetchdata)) #<class 'tuple'>


    #return "Hello this is the Flask Server"
    return render_template('fServer_Index.html')#,tasks=tasks , data = fetchdata)

if __name__ == "__main__":
    app_fServer.run(debug=True)    