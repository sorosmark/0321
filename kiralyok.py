from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                              host='127.0.0.1',
                              database='kiralyok')

cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT * FROM uralkodo WHERE ragnev IS NOT NULL 
ORDER BY szul ASC;""")
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT *  FROM uralkodo 
INNER JOIN hivatal ON uralkodo.azon = hivatal.azon
WHERE uhaz_az = 1 
ORDER BY hivatal.mettol ASC;
""")
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT *  FROM uralkodo 
INNER JOIN hivatal ON uralkodo.azon = hivatal.azon
WHERE hivatal.koronazas > hivatal.mettol """)
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT * FROM uralkodo 
INNER JOIN hivatal ON uralkodo.azon = hivatal.azon 
WHERE hivatal.koronazas > 1601 AND hivatal.koronazas < 1700;""")
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT * FROM uralkodo 
INNER JOIN hivatal ON uralkodo.azon = hivatal.azon
ORDER BY ABS(hivatal.meddig - hivatal.mettol) DESC
LIMIT 1""")
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT * FROM uralkodo 
INNER JOIN hivatal ON uralkodo.azon = hivatal.azon
WHERE hivatal.mettol - uralkodo.szul < 15 
ORDER BY hivatal.mettol - uralkodo.szul ASC
""")
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT nev, COUNT(hivatal.azon) FROM hivatal
INNER JOIN uralkodo on hivatal.uralkodo_az = uralkodo.azon
GROUP BY uralkodo.nev
HAVING COUNT(*) > 1;""")
for table in cursor:
    print(table)
print()


cursor.execute("""SELECT uralkodohaz.nev, COUNT(uralkodo.uhaz_az) FROM hivatal
INNER JOIN uralkodo on hivatal.uralkodo_az = uralkodo.azon
INNER JOIN uralkodohaz ON uralkodo.uhaz_az
GROUP BY uralkodohaz.nev
ORDER BY COUNT(uralkodo.uhaz_az) DESC""")
for table in cursor:
    print(table)
print()


cnx.close()