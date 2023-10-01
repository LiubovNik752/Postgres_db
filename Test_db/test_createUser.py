


class Test_crud_user():
    def test_create_user(self, connection):

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO public.users(id, first_name, last_name)
	        VALUES (777, 'test_name', 'test_surname');"""
            )
            print("User was successfully created")


    def test_get_user(self, connection):

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT id, first_name, last_name FROM public.users WHERE id = 777;"""
                )
                assert cursor.fetchone() == (777, 'test_name', 'test_surname')


    def test_update_user(self, connection):

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


    def test_delete_user(self, connection):

            with connection.cursor() as cursor:
                cursor.execute(
                    """DELETE FROM public.users WHERE id = 777;"""
                )
                assert cursor.fetchone() is None


