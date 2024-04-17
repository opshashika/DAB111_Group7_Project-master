import sqlite3

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('transaction_data.db')

# Function to fetch data from the transactions table
def fetch_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions limit 20')
    rows = cursor.fetchall()
    conn.close()
    return rows
