import unittest
from app import app, db, Expense

class ExpenseTrackerTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_expenses.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_expense(self):
        response = self.app.post('/add', data=dict(name='Test Expense', amount='100'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Expense.query.count(), 1)

    def test_get_expenses(self):
        self.app.post('/add', data=dict(name='Test Expense', amount='100'))
        response = self.app.get('/')
        self.assertIn(b'Test Expense', response.data)

if __name__ == '__main__':
    unittest.main()
