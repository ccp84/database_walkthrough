import psycopg2


# connect to chinook database
connection = psycopg2.connect(database="chinook")


# cursor object of the database
cursor = connection.cursor()


# query the database
# cursor.execute('SELECT * FROM "Artist"')
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])


# fetch results (multiple)
results = cursor.fetchall()


# fetch single result
# results = cursor.fetchone()


# close connection
connection.close


# print results
for result in results:
    print(result)
