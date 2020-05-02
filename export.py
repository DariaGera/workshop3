import csv
import cx_Oracle

username = 'MYONLINEEDU'
password = 'oracle'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

cursor.execute("""
SELECT
    trim(town)
FROM
    town""")

for [town] in cursor:

    with open("Town_" + town + ".csv", "w", newline="") as file:

        writer = csv.writer(file)
        cursor_values = connection.cursor()

        query = """
                SELECT
                    address,
                    timestamp,
                    title
                FROM
                         place
                    JOIN accident ON accident.place_place_id = place.place_id
                WHERE
                    town_town = :town"""

        cursor_values.execute(query, town=town)

        writer.writerow(["address", "timestamp", "title"])
        for address, timestamp, title in cursor_values:
            writer.writerow([address, timestamp, title])


cursor.close()
