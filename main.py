import psycopg2
from config import host, user, password, db_name, port

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name,
        port = port
    )
    connection.autocommit = True

except:
    print("Cannot connect to db")

try:
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO public.users(id, first_name, last_name)
	    VALUES (777, 'test_name', 'test_surname');"""
        )
        print("[INFO] User was successfully created")

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT id, first_name, last_name FROM public.users WHERE id = 777;"""
        )
        print(cursor.fetchall())

    with connection.cursor() as cursor:
        cursor.execute(
            """UPDATE public.users SET first_name = 'new_name', last_name = 'new_surname' WHERE id = 777;"""
        )
        print("[INFO] User was successfully updated", sep='\n')


    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT id, first_name, last_name FROM public.users where id = 777;"""
        )
        print(cursor.fetchall())

    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM public.users WHERE id = 777;"""
        )
        print("User with id = 777 was successfully deleted")


except Exception as ex:
    print("[INFO] Error while working with PostgreSQL")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")

