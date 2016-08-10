import psycopg2
import csv


def main():
    conn = psycopg2.connect(database="test", user="postgres")

    cur = conn.cursor()

    f = open('us-president-tenures.csv', 'r')
    reader = csv.reader(f)
    headers = next(reader)

    cur.execute("CREATE TABLE IF NOT EXISTS presidents (name VARCHAR, \
                 termStart DATE, termEnd DATE, party VARCHAR);")

    cur.copy_from(f, 'presidents', sep=',', columns=headers)

    f.close()

    cur.execute("SELECT * FROM presidents;")
    x = cur.fetchone()
    print(x)
    conn.commit()
    cur.close()
    conn.close()

    # add_or_search = input("Would you like to [S]earch data or [A]dd data? ")


if __name__ == '__main__':
    main()
