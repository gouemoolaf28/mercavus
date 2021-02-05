from database import cursor, db
import mysql.connector

def add_brand(id, name, country, date):
    try:
        sql = ("INSERT INTO mercavus_brand (id, name, country, date) VALUES (%s, %s, %s, %s)")
        cursor.execute(sql, (id, name, country, date))
        db.commit()
    except mysql.connector.errors.IntegrityError:
        return