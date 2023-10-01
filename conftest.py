import psycopg2
import pytest
from conf.config import host, user, password, db_name, port

@pytest.fixture
def connection():
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port = port
        )
        connection.autocommit = True
        print("Connection open")

    except:
        print("Cannot connect to db")

    yield connection

    print("PostgreSQL connection closed")
    connection.close()