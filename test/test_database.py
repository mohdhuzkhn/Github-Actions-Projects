from database import get_connection


def test_postgresql_connection():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()

    connection.close()

    assert result == (1,)