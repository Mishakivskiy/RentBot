import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exist(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", [(user_id)])
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", [(user_id)])
        return result.fetchall()[0]

    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)",[(user_id)])
        return self.conn.commit()

    def add_add(self, user_id, address, price):
        self.cursor.execute("INSERT INTO `ads` (`users_id`, `address`, `price`) VALUES (?, ?, ?)",
                           [(self.get_user_id(user_id), address, price)])
        return self.conn.commit()

    def get_add(self, user_id):

        result = self.cursor.execute("SELEST * FROM `ads` WHERE `user_id` = ?", [self.get_user_id(user_id)])
        return result.fetchall()


    def close(self):
        self.conn.close()