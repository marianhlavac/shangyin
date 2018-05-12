import unittest
import os
import shangyin.storage as storage

class StorageTest(unittest.TestCase):
    def setUp(self):
        self.file = 'testdb.db'
        self.db = storage.Storage(self.file)
        self.db.setup()

    def test_adduser(self):
        self.db.add_user('mail@mail.mail', 'fullname', 'dep', 'pwd')
        self.assertGreaterEqual(len(self.db.get_users()), 1)
        print(self.db.get_users())

    def tearDown(self):
        pass
        #os.remove(self.file)
