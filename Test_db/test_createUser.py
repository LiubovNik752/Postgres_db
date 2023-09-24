import psycopg2
from conf import *


class Test_crud_user():
    def test_create_user(self):
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

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO public.users(id, first_name, last_name)
	            VALUES (777, 'test_name', 'test_surname');"""
                )
                print("User was successfully created")

        finally:
            if connection:
                connection.close()
                print("PostgreSQL connection closed")


    def test_get_user(self):
        try:
            connection = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database = db_name,
                port = port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT id, first_name, last_name FROM public.users WHERE id = 777;"""
                )
                assert cursor.fetchone() == (777, 'test_name', 'test_surname')

        finally:
            if connection:
                connection.close()
                print("PostgreSQL connection closed")

    def test_update_user(self):
        try:
            connection = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database = db_name,
                port = port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE public.users SET first_name = 'new_name', last_name = 'new_surname' WHERE id = 777;"""
                )
                print("User was successfully updated")

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT id, first_name, last_name FROM public.users WHERE id = 777;"""
                )
                assert cursor.fetchone() == (777, 'new_name', 'new_surname')

        finally:
            if connection:
                connection.close()
            print("PostgreSQL connection closed")

    def test_delete_user(self):
        try:
            connection = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database = db_name,
                port = port
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    """DELETE FROM public.users WHERE id = 777;"""
                )
                assert cursor.fetchone() is None

        finally:
            if connection:
                connection.close()
            print("PostgreSQL connection closed")

