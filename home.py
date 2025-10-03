# app.py
from flask import Flask, render_template
import  sqlite3

app = Flask(__name__)

con = sqlite3.connect('students.db')
con.execute('''
CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
            phone TEXT NOT NULL,
              address TEXT NOT NULL);''')

con.commit()
con.close()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route('/saved', methods=['POST'])
def save_student():
    sname = 'Mg Mg'
    phone = '121212'
    address = 'Yangon'
    print(sname)
    print(phone)
    print(address)
    return render_template("homepage.html")



@app.route("/about")
def about():
    return render_template("address.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/student")
def student():
    return render_template("students.html")


if __name__ == "__main__":
    app.run(debug=True)
