import psycopg2
import csv

conn = psycopg2.connect(database="test", user="postgres")

cur = conn.cursor()

f = open('us-president-tenures.csv', 'r')
reader = csv.reader(f)
headers = next(reader)

cur.execute("CREATE TABLE IF NOT EXISTS presidents (name VARCHAR, \
             termStart DATE, termEnd DATE, party VARCHAR);")

cur.copy_from(f, 'presidents', sep=',', columns=headers)

f.close()


def add():
    name = input("What is the new president\'s name? ")
    start_term = input("When was this president inaugurated? ")
    end_term = input("When did/will this president leave office? ")
    party = input("Which political party does this president belong to? ")
    cur.execute("INSERT INTO presidents (name, termStart, termEnd, party) \
    VALUES (%s, %s, %s, %s)", (name, start_term, end_term, party))


def search():
    criterion = input('Would you like to search by \
[N]ame, [Y]ear, or [P]arty?')
    pass


def main():

    # cur.execute("SELECT * FROM presidents;")
    while True:
        print('Enter \'q\' to quit.')
        add_or_search = input("Would you like to [S]earch data \
or [A]dd data? ")
        if add_or_search.lower() == 'q':
            break
        if add_or_search.lower() == 'a':
            add()
            continue
        if add_or_search.lower() == 's':
            search()
            continue

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
