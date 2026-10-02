import mysql.connector

def connect_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arman@7733",
        database="electricity_db"
    )
    return connection

def add_record(name, date, units):
    connection = connect_database()
    cursor = connection.cursor()
    query = """
    INSERT INTO consumption (consumer_name, date, units_consumed)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, date, units))
    connection.commit()
    cursor.close()
    connection.close()

def get_records():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM consumption")
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return records

def delete_record(record_id):
    connection = connect_database()
    cursor = connection.cursor()

    query = "DELETE FROM consumption WHERE id = %s"
    cursor.execute(query, (record_id,))

    deleted = cursor.rowcount

    connection.commit()
    cursor.close()
    connection.close()

    return deleted