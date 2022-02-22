#!/usr/bin/python3

import MySQLdb


def print_n_state():
    from sys import argv
    if len(argv) == 5:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4],))
        for rows in cursor.fetchall():
            if rows[1] == (argv[4],):
                print(rows)

        cursor.close()
        db.close()
    else:
        return


if __name__ == "__main__":
    print_n_state()
