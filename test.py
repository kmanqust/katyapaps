import unittest
from GG import User
import sqlite3
import datetime

class TestUser(unittest.TestCase):

    def test_init(self):
        obj = User('Katya', 'Mangutova', 50)
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM User WHERE card_id = 50')
        result = cursor.fetchall()
        cursor.execute('DELETE FROM User WHERE card_id = 50')
        conn.commit()
        conn.close()
        self.assertEqual(result, [('Katya', 'Mangutova', 50)])

    def test_createEx(self):
        obj = User('Katya', 'Mangutova', 40)
        obj.CreateEx(3.0, datetime.date(2023, 4, 8), 'Default')
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Expense WHERE card_id = 40')
        result = cursor.fetchall()
        cursor.execute('DELETE FROM User WHERE card_id = 40')
        cursor.execute('DELETE FROM Expense WHERE card_id = 40')
        conn.commit()
        conn.close()
        self.assertEqual(result, [(40, 3.0, '2023-04-08', 'Default')])

    def test_user_card_id_unique(self):
        obj = User('1', '1', 1)
        with self.assertRaises(sqlite3.IntegrityError):
            obj = User('1', '1', 1)
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM User WHERE card_id = 1')
        conn.commit()
        conn.close()

    def test_delete(self):
        obj = User('Katya', 'Mangutova', 50)
        obj.delete()
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM User WHERE card_id = 50')
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()