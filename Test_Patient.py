import sqlite3
import unittest


class Patient(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect('hospitalDB.db')
        self.code = "1002"
        self.name = "sandy"

    def tearDown(self):
        self.code = "0"
        self.name = ""
        self.connection.close()

    def test_case(self):
        result = self.connection.execute("SELECT name FROM Patient_Details WHERE patientCode =" + self.code)
        for i in result:
            fetchname = i[0]
        self.assertEqual(fetchname, self.name)


if __name__ == "__main__":
    unittest.main()
