import os
import psycopg2

conn = psycopg2.connect(
    host="10.24.24.218",
    database = "testdb",
    user= "postgres",
    password= "Bungfodder123"
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS smellass;')
cur.execute('CREATE TABLE smellass (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO smellass (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO smellass (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

conn.commit()

cur.close()
conn.close()
