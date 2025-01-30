import sqlite3

databaseName = "tickets.db"

class TicketData():
    def connect():
        con = sqlite3.connect(f"./{databaseName}")
        return con

    def cursor(connection):
        cur = connection.cursor()
        return cur

    def createlayout(connection, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS TicketData(ChannelID, AuthorID, Claimed, TimeCreated, Type, Status, MessageID)")
        connection.commit()

    def getall(cursor):
        return cursor.execute("SELECT * FROM TicketData").fetchall()
