import unittest
import os
import shangyin.storage as storage

class StorageTest(unittest.TestCase):
    def setUp(self):
        # Assuming we trust setup() works
        self.file = 'testdb.sqlite3'
        self.db = storage.Storage(self.file)
        self.db.setup()

    def test_adduser(self):
        madress = 'user@mail.mail'
        id = self.db.create_user(madress, 'User', '', '')

        self.assertGreaterEqual(self.db.get_count('user'), 1)
        self.assertGreaterEqual(id, 0)

        user = self.db.get_by_id('user', id, 'email')
        self.assertNotEqual(user, None)
        self.assertEqual(user[0], madress)

    def test_addcard(self):
        cardid = '6465465498498486465'
        uid = self.db.create_user('userwithcard@mail.mail', 'User', '', '')
        self.db.create_card(cardid)
        self.db.assign_card(cardid, uid)
        
        card = self.db.get_by_id('card', cardid, 'user_id')
        self.assertNotEqual(card, None)
        self.assertEqual(card[0], uid)

    def test_addcoffee(self):
        cid = self.db.create_card('546521564944984984')
        self.db.create_coffee(cid, 1)

        coffees = self.db.select('id, card_id, milk', 'coffee', 'WHERE card_id = "{}"'.format(cid))
        self.assertNotEqual(coffees, None)
        self.assertGreaterEqual(len(coffees), 1)
        self.assertEqual(coffees[0][2], 1)


    def tearDown(self):
        os.remove(self.file)
