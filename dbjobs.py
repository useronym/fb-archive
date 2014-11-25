# -*- coding: utf-8 -*-

import sqlite3
import os

class Database:
    def __init__(self, dbpath):
        database_exists = os.path.exists(dbpath)
        self.conn = sqlite3.connect(dbpath)
        self.cursor = self.conn.cursor()
        if not database_exists:
            print("Creating database")
            self.create_db()

    def create_db(self):
        self.conn.execute("CREATE TABLE works (id INTEGER NOT NULL, \
                                               concert_id INTEGER NOT NULL, \
                                               composer TEXT NOT NULL, \
                                               work TEXT NOT NULL)")

        self.conn.execute("CREATE TABLE soloists (id INTEGER NOT NULL, \
                                                  concert_id TEXT NOT NULL, \
                                                  name TEXT NOT NULL)")

        self.conn.execute("CREATE TABLE festivals (id INTEGER NOT NULL, \
                                                   name TEXT NOT NULL)")

        self.conn.execute("CREATE TABLE dirigents (id INTEGER NOT NULL, \
                                                   concert_id INTEGER NOT NULL, \
                                                   name TEXT NOT NULL)")

        self.conn.execute("CREATE TABLE concerts (id INTEGER NOT NULL, \
                                                  festival_id INTEGER, \
                                                  date TEXT NOT NULL, \
                                                  state TEXT NOT NULL, \
                                                  city TEXT NOT NULL, \
                                                  hall TEXT NOT NULL, \
                                                  type TEXT, \
                                                  note TEXT)")
        self.conn.commit()
        print("Database successfuly created")

    def add_work(concert_id, composer, work):
        id = self.get_next_id("works")
        self.cursor.execute("INSERT INTO works VALUES ({0}, {1}, {2}, {3})".format(id, concert_id, composer, work))
        self.conn.commit()

    def add_soloist(concert_id, name):
        id = self.get_next_id("soloists")
        self.cursor.execute("INSERT INTO soloists VALUES ({0}, {1}, {2})".format(id, concert_id, name))
        self.conn.commit()

    def add_festival(self, name):
        id = self.get_next_id("festivals")
        self.cursor.execute("INSERT INTO festivals VALUES ({0}, {1})".format(id, name))
        self.conn.commit()

    def add_dirigent(self, concert_id, name):
        id = self.get_next_id("dirigents")
        self.cursor.execute("INSERT INTO dirigents VALUES ({0}, {1}, {2})".format(id, concert_id, name))
        self.conn.commit()

    def add_concert(self, festival_id, date, state, city, hall, type, note):
        id = self.get_next_id("concerts")
        if (festival_id is None):
            festival_id = "NULL"

        if (type is None and note is None):
            self.cursor.execute("INSERT INTO concerts VALUES ({0}, {1}, '{2}', '{3}', '{4}', '{5}', {6}, {7})".format(
                id, festival_id, date, state, city, hall, "NULL", "NULL"))
        elif (type is None):
            self.cursor.execute("INSERT INTO concerts VALUES ({0}, {1}, '{2}', '{3}', '{4}', '{5}', {6}, '{7}')".format(
                id, festival_id, date, state, city, hall, "NULL", note))
        elif (note is None):
            self.cursor.execute("INSERT INTO concerts VALUES ({0}, {1}, '{2}', '{3}', '{4}', '{5}', '{6}', {7})".format(
                id, festival_id, date, state, city, hall, note, "NULL"))
        else:
            self.cursor.execute("INSERT INTO concerts VALUES ({0}, {1}, '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(
                id, festival_id, date, state, city, hall, type, note))
        self.conn.commit()

    def get_next_id(self, table):
        self.cursor.execute("SELECT MAX(id) FROM {0}".format(table))
        id = self.cursor.fetchone()
        if (id[0] is None):
            id = 0
        else:
            id = id[0] + 1
        return id

    def debug_print(self):
        self.cursor.execute("SELECT * FROM concerts")
        print(self.cursor.fetchall())

    def close(self):
        self.conn.close()
