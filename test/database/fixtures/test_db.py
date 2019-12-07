import psycopg2

from pathlib import Path


# noinspection SqlDialectInspection,SqlNoDataSourceInspection
class CreateDBs:

    def __init__(self, info_dict, db_type):
        self.info_dict = info_dict
        self.current_dir = Path(__file__).parent.resolve()
        if db_type == 'psql':
            self.psql_drop_and_create_database()
            self.psql_create_and_populate_tables()

    def psql_drop_and_create_database(self):
        connection = psycopg2.connect(
            host=self.info_dict.get('HOST', 'localhost'),
            database=self.info_dict.get('DEFAULT_DB'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT', 5432),
        )
        connection.autocommit = True
        cursor = connection.cursor()

        qs = f"DROP DATABASE IF EXISTS {self.info_dict.get('DATABASE', 'pyd')}"
        cursor.execute(qs)

        qs = f"CREATE DATABASE {self.info_dict.get('DATABASE', 'pyd')} " \
             f"WITH OWNER {self.info_dict.get('USER')}"
        cursor.execute(qs)

        connection.close()

    def psql_create_and_populate_tables(self):
        connection = psycopg2.connect(
            host=self.info_dict.get('HOST', 'localhost'),
            database=self.info_dict.get('DATABASE'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT', 5432),
        )
        connection.autocommit = True
        cursor = connection.cursor()

        # Create and populate "country"
        qs_create_country = \
            f"CREATE TABLE country (" \
            f" id serial PRIMARY KEY," \
            f" country VARCHAR (50)," \
            f" code VARCHAR (4)" \
            f")"
        cursor.execute(qs_create_country)

        country_path = self.current_dir.joinpath('country.csv')
        with open(country_path, 'r') as country:
            next(country)  # Skip the header row.
            cursor.copy_from(country, 'country', sep=',')

        # Create and populate "resident"
        qs_create_resident = \
            f"CREATE TABLE resident (" \
            f" id serial PRIMARY KEY," \
            f" first_name VARCHAR (50)" \
            f")"
        cursor.execute(qs_create_resident)

        resident_path = self.current_dir.joinpath('resident.csv')
        with open(resident_path, 'r') as resident:
            next(resident)  # Skip the header row.
            cursor.copy_from(resident, 'resident', sep=',')

        # Create and populate "address"
        qs_create_address = \
            f"CREATE TABLE address (" \
            f" id serial PRIMARY KEY," \
            f" complete_address VARCHAR (255) NOT NULL," \
            f" country_id SMALLINT REFERENCES country(id)," \
            f" resident_id SMALLINT REFERENCES resident(id)" \
            f")"
        cursor.execute(qs_create_address)

        address_path = self.current_dir.joinpath('address.csv')
        with open(address_path, 'r') as address:
            next(address)  # Skip the header row.
            cursor.copy_from(address, 'address', sep=',')
