from flask import Flask
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host="10.24.24.218",
        database = "testdb",
        user= "postgres",
        password= "Bungfodder123")

    return conn



@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM smellass;')
    bookass = cur.fetchall()
    cur.close()
    conn.close()
    return bookass



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug=True)