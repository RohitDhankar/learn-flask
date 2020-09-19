from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#3 Fwd Slashes means - Relative path
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    content = db.Column()

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)    