from flask import Flask, jsonify
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
    cur.execute('SELECT json_agg(smellass) FROM smellass;')
    bookass = cur.fetchall()
    cur.close()
    conn.close()
    json_data = []
    # for i in bookass:
    #     json_data.append({"id": i[0], "title": i[1], "author": i[2], "pages": i[3], "review": i[4], "dateAdded": i[5]})
    #     print('smell', json_data)
    return jsonify(bookass)



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug=True)