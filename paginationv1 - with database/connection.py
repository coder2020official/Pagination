import sqlite3

#CREATE DATABASE
def create_db_new():
    db = sqlite3.connect('users.db', check_same_thread=False)
    sql = db.cursor()
    sql.execute('''CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER,
        first_name VARCHAR,
        page VARCHAR)''')
    sql.close()
    db.close()
#PERFORMS SQLITE3
def database_query(query: str,args):
    """Performs database commands.
    :params:
    query: str - this should be your command to be executed
    args: Arguments that should be put instead of ? in a query"""
    db = sqlite3.connect('users.db', check_same_thread=False)
    with db:
        sql = db.cursor()
        sql.execute(query,args)
        result = sql.fetchall()
    if db:
        db.commit()
        sql.close()

    return result