from django.db import connection
from django.test import TransactionTestCase


class DatabaseConnectionTests(TransactionTestCase):
    def test_database_is_connected_ready_and_usable(self):
        connection.ensure_connection()
        self.assertIsNotNone(connection.connection)
        self.assertTrue(connection.is_usable())
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            self.assertEqual(cursor.fetchone()[0], 1)
