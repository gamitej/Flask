import sqlite3

def connect_to_db():
    connection = sqlite3.connect('data.db')
    return connection

def selectFromTable(rows, table_name, find_by_row, value):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = f"select {rows} from {table_name} where {find_by_row}=?"
    result = cursor.execute(query, (value,))
    row = result.fetchone()
    connection.close()
    return row

def insertIntoTable(table_name, total_values, values):
    connection = connect_to_db()
    cursor = connection.cursor()
    insert_query = f"INSERT OR IGNORE INTO {table_name} VALUES{total_values}"
    cursor.execute(insert_query, values)
    connection.commit()
    connection.close()

def updateTable(table_name, rows_to_update, where_cond, values):
    connection = connect_to_db()
    cursor = connection.cursor()
    update_query = f"UPDATE {table_name} SET {rows_to_update} where {where_cond}"
    cursor.execute(update_query, values)
    connection.commit()
    connection.close()