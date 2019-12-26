# Native import
import csv
from pathlib import Path

# Third party import
import psycopg2
import pymysql

# Local import
from test.database import const


# noinspection SqlDialectInspection,SqlNoDataSourceInspection
class Postgres:

    def __init__(self, info_dict, csv_dict):
        self.info_dict = info_dict
        self.csv_dict = csv_dict
        self.connection = None
        self.cursor = None

    def connect_to_test(self):
        # Connect on "correct" (/test) database
        self.connection = psycopg2.connect(
            host=self.info_dict.get('HOST'),
            database=self.info_dict.get('DATABASE'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT')
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def connect_to_default(self):
        self.connection = psycopg2.connect(
            host=self.info_dict.get('HOST'),
            database=const.POSTGRES,
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT')
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection is not None and not self.connection.closed:
            self.connection.close()

    def create_database(self):
        qs = f"CREATE DATABASE {self.info_dict.get('DATABASE')} " \
             f"WITH OWNER {self.info_dict.get('USER')}"
        self.cursor.execute(qs)

    def drop_database(self):
        qs = f"DROP DATABASE IF EXISTS {self.info_dict.get('DATABASE')}"
        self.cursor.execute(qs)

    def create_tables(self):
        # Create "country"
        qs_create_country = \
            f"CREATE TABLE country (" \
            f" id serial PRIMARY KEY," \
            f" country VARCHAR (50)," \
            f" code VARCHAR (4)" \
            f")"
        self.cursor.execute(qs_create_country)

        # Create "resident"
        qs_create_resident = \
            f"CREATE TABLE resident (" \
            f" id serial PRIMARY KEY," \
            f" first_name VARCHAR (50)" \
            f")"
        self.cursor.execute(qs_create_resident)

        # Create "address"
        qs_create_address = \
            f"CREATE TABLE address (" \
            f" id serial PRIMARY KEY," \
            f" complete_address VARCHAR (255) NOT NULL," \
            f" country_id SMALLINT REFERENCES country(id)," \
            f" resident_id SMALLINT REFERENCES resident(id)" \
            f")"
        self.cursor.execute(qs_create_address)

    def populate_tables(self):
        with open(self.csv_dict.get('country_path'), 'r') as country:
            next(country)  # Skip the header row.
            self.cursor.copy_from(country, 'country', sep=',')

        with open(self.csv_dict.get('resident_path'), 'r') as resident:
            next(resident)  # Skip the header row.
            self.cursor.copy_from(resident, 'resident', sep=',')

        with open(self.csv_dict.get('address_path'), 'r') as address:
            next(address)  # Skip the header row.
            self.cursor.copy_from(address, 'address', sep=',')


# noinspection SqlDialectInspection,SqlNoDataSourceInspection
class MySQL:

    def __init__(self, info_dict, csv_dict):
        self.info_dict = info_dict
        self.csv_dict = csv_dict
        self.connection = None
        self.cursor = None

    def connect_to_test(self):
        # Connect on "correct" (/test) database
        self.connection = pymysql.connect(
            host=self.info_dict.get('HOST'),
            database=self.info_dict.get('DATABASE'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT'),
            autocommit=True
        )
        self.cursor = self.connection.cursor()

    def connect_to_default(self):
        self.connection = pymysql.connect(
            host=self.info_dict.get('HOST'),
            database=const.MYSQL,
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT'),
            autocommit=True
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection is not None and self.connection.open:
            self.connection.close()

    def create_database(self):
        qs = f"CREATE DATABASE {self.info_dict.get('DATABASE')}"
        self.cursor.execute(qs)

    def drop_database(self):
        qs = f"DROP DATABASE IF EXISTS {self.info_dict.get('DATABASE')}"
        self.cursor.execute(qs)

    def create_tables(self):
        # Create "country"
        qs_create_country = \
            f"CREATE TABLE country (" \
            f" id SMALLINT PRIMARY KEY," \
            f" country VARCHAR (50)," \
            f" code VARCHAR (4)" \
            f")"
        self.cursor.execute(qs_create_country)

        # Create "resident"
        qs_create_resident = \
            f"CREATE TABLE resident (" \
            f" id SMALLINT PRIMARY KEY," \
            f" first_name VARCHAR (50)" \
            f")"
        self.cursor.execute(qs_create_resident)

        # Create "address"
        qs_create_address = \
            f"CREATE TABLE address (" \
            f" id SMALLINT PRIMARY KEY," \
            f" complete_address VARCHAR (255) NOT NULL," \
            f" country_id SMALLINT REFERENCES country(id)," \
            f" resident_id SMALLINT REFERENCES resident(id)" \
            f")"
        self.cursor.execute(qs_create_address)

    def populate_tables(self):
        with open(self.csv_dict.get('country_path'), 'r') as country:
            next(country)  # Skip the header row.
            data = [list(line) for line in csv.reader(country, delimiter=',')]
            qs = f"INSERT INTO country VALUES (%s, %s, %s)"
            self.cursor.executemany(qs, data)

        with open(self.csv_dict.get('resident_path'), 'r') as resident:
            next(resident)  # Skip the header row.
            data = [list(line) for line in csv.reader(resident, delimiter=',')]
            qs = f"INSERT INTO resident VALUES (%s, %s)"
            self.cursor.executemany(qs, data)

        with open(self.csv_dict.get('address_path'), 'r') as address:
            next(address)  # Skip the header row.
            data = [list(line) for line in csv.reader(address, delimiter=',')]
            qs = f"INSERT INTO address VALUES (%s, %s, %s, %s)"
            self.cursor.executemany(qs, data)


class CreateFixtureDB:

    def __init__(self, db_type, info_dict):
        current_dir = Path(__file__).parent.resolve()
        self.csv_dict = {
            'country_path': current_dir.joinpath('country.csv'),
            'resident_path': current_dir.joinpath('resident.csv'),
            'address_path': current_dir.joinpath('address.csv')
        }
        self.db_type = db_type
        self.info_dict = info_dict
        if self.db_type is const.POSTGRES:
            self.db = Postgres(self.info_dict, self.csv_dict)
        if self.db_type is const.MYSQL:
            self.db = MySQL(self.info_dict, self.csv_dict)

    def create_database(self):
        if self.db:
            self.db.connect_to_default()
            self.db.drop_database()  # "Safety check"
            self.db.create_database()
            self.db.disconnect()

    def drop_database(self):
        if self.db:
            self.db.connect_to_default()
            self.db.drop_database()
            self.db.disconnect()

    def create_and_populate_tables(self):
        if self.db:
            self.db.connect_to_test()
            self.db.create_tables()
            self.db.populate_tables()
            self.db.disconnect()

    def create(self):
        self.create_database()
        self.create_and_populate_tables()

    def delete(self):
        self.drop_database()
