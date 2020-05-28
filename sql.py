from sqlite3 import connect


class SQLDB:
    def __init__(self):
        self.connection = connect('phailfebot.db')
        self.cursor= self.connection.cursor()
        self.cursor.execute('create table if not exists coolmsg (text VARCHAR(255) primary key not null)')

    def add(self, text):
        if len(list(self.cursor.execute('select * from coolmsg where text=?', [text])))==0:
            self.cursor.execute('insert into coolmsg values (?)', [text])
            self.connection.commit()

    def get(self):
        try:
            text=list(self.cursor.execute('select * from coolmsg order by random() limit 1'))[0][0]
            self.cursor.execute('delete from coolmsg where text=?', [text])
            self.connection.commit()
        except:
            text=None
        return text

    def size(self):
        return list(self.cursor.execute('select count(*) from coolmsg'))[0][0]
