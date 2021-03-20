from unidecode import unidecode
from os import listdir
from os.path import isfile, join

import sqlite3 as sl
import matplotlib.pyplot as plt

TEMP = "temp.csv"
DB = "database.db"


def get_files():
    files = [f for f in listdir("input") if isfile(join("input", f))]
    if not files:
        raise ("No files found")

    return sorted([f for f in files if f.split(".")[-1] == "csv"])


def join_csv(files):
    with open(TEMP, "w+") as tmp:

        tmp.write("date,category,title,amount\n")

        for item in files:
            print(f"joining {item}")
            with open(f"input/{item}", "r") as csv:
                csv.readline()  # ignore header
                for line in csv:
                    tmp.write(line)
                csv.close()
                tmp.write("\n")
        tmp.close()


def create_database():
    db = sl.connect(DB)

    with db:
        db.execute("DROP TABLE IF EXISTS PURCHASE")
        db.execute(
            """
        CREATE TABLE PURCHASE (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          year INTEGER NOT NULL,
          month INTEGER NOT NULL,
          day INTEGER NOT NULL,
          date STRING,
          category TEXT,
          title TEXT,
          amount REAL
        )
      """
        )

        sql = "INSERT INTO PURCHASE (year, month, day, date, category, title, amount) VALUES(?, ?, ?, ?, ?, ?, ?)"
        with open(TEMP, "r") as tmp:
            tmp.readline()

            for line in tmp:
                date, category, title, amount = line.split(",")
                category = unidecode(category) if category else "sem categoria"
                title = unidecode(title)
                amount = float(amount)
                year, month, day = date.split("-")

                db.execute(sql, (year, month, day, date, category, title, amount))
            tmp.close()
    return db


def main():
    print("💰 Credit Card data analyzer")

    try:
        files = get_files()
    except:
        print("No data found! 👀 ")
        print(
            "Please create a input directory and place your files inside, as described in the README"
        )
        quit()

    if len(files) > 1:
        print("Joining CSV files... 🙄")
        join_csv(files)
        print(f"finished joining files 👍")

    print("Creating database")
    db = create_database()

    categories = db.execute("SELECT DISTINCT category FROM PURCHASE LIMIT 1") # todo: remove limit

    dataset = {}
    for category in categories: 
        data = db.execute(
            """
                SELECT year, month, category, sum(amount) as s 
                FROM PURCHASE 
                WHERE category = ? 
                GROUP BY YEAR 
                ORDER BY year, month
            """,
            category
        )

        result = [(f"{month}/{year}", amount) for year, month, _, amount in data]

        dataset[category] = result
        plt.scatter(*zip(*result))
    plt.show()
    print(dataset)


main()