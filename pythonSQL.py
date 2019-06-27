import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="whatever_your_heart_desires")
curl = db.cursor()
curl.execute("SELECT * FROM Student")
print(curl.fetchall())