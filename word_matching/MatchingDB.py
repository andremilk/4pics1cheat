import MySQLdb

class MatchingDB:
    def __init__(self, host, user, passwd, db, table, column):
        self.conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        self.table = table
        self.db = db
        self.column = column
        self.cursor = self.conn.cursor()

    def word_exists(self, word):
        sql = "SELECT {0} FROM {1} where {1} = '{2}'".format(self.db, self.column, word)
        return bool(self.cursor.execute(sql))

    def get_words(self, length):
        sql = "SELECT * from {0} where LENGTH({0}) = {1}".format(self.column, length)
        self.cursor.execute(sql)
        return self.cursor
