from flask import Flask
from flask import render_template
from flask import request

import math
import MySQLdb

from student import Student

pageSize = 6
app = Flask(__name__)

def startDB():
	db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="whatever_your_heart_desires")
	curl = db.cursor()
	return db, curl

def select(limit, offset):
	db, curl = startDB()
	curl.execute('SELECT * FROM Student LIMIT %s OFFSET %s', (limit, offset),)
	dbResult = curl.fetchall()
	db.close()
	
	tup = ()
	for i in range(len(dbResult)):
		tup += Student(dbResult[i][0], dbResult[i][1], dbResult[i][2]),
	return tup

def insert(student):
	db, curl = startDB()
	curl.execute('INSERT INTO Student (name, age) VALUES (%s, %s);', (student.name, student.age),)
	db.commit()
	db.close()
	
def update(student):
	db, curl = startDB()
	curl.execute('UPDATE Student SET name = %s, age = %s WHERE id = %s;', (student.name, student.age, student.id),)
	db.commit()
	db.close()

def delete(student):
	db, curl = startDB()
	curl.execute('DELETE FROM Student WHERE id = %s;', [student.id])
	db.commit()
	db.close()

def getRows():
	db, curl = startDB()
	curl.execute('SELECT Count(*) FROM Student;')
	db.close()
	return curl.fetchall()[0][0];

def  pagination(pages, current):
	if(pages < 8):
		return list(range(1, pages+1))
	if(current < 4):
		return list(range(1, 6)) + ["...", pages]
	if(current >  pages-3):
		return [1, "..."] + list(range(pages-4, pages+1))
	return [1, "..."] + list(range(current-1, current+2)) + ["...", pages]

@app.route("/<int:page>", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home(page = 1):
	print(page)
	print(getRows() - 1)
	args = request.view_args.copy()
	print(args)
	print("START")
	db, curl = startDB()

	pages = math.ceil(getRows() / pageSize) 
	if(page > pages):
		page = pages
	test = select(pageSize, (page-1)*pageSize)
	#test = select(10, 0)
	

	print(test)
	#print(test[-1].name)

	#student = (Student(1, "David", 21), Student(1, "David", 21))
	pages = pagination(pages, page)
	if request.form:
		#newstudent = student + (Student(1, request.form.get("title"), 21),)
		print("PRINGING")
		if(request.form.get("create1") != None and len(request.form.get("create1")) != 0
			and request.form.get("create2") != None and len(request.form.get("create2")) != 0):
			print("Creating")
			insert(Student(-1, request.form.get("create1"), request.form.get("create2")))
			test = select(pageSize, (page-1)*pageSize)
	
		if(request.form.get("update1") != None and len(request.form.get("update1")) != 0
			and request.form.get("update2") != None and len(request.form.get("update2")) != 0
			and request.form.get("update3") != None and len(request.form.get("update3")) != 0):
			print("Updating")
			update(Student(request.form.get("update1"), request.form.get("update2"), request.form.get("update3")))
			test = select(pageSize, (page-1)*pageSize)
	
		
		if(request.form.get("delete1") != None and len(request.form.get("delete1")) != 0):
			print("Deleting")
			delete(Student(request.form.get("delete1"), "", -1))
			test = select(pageSize, (page-1)*pageSize)
	
		print("Ok")
		#test += (Student(1, request.form.get("title"), 21),)
		return render_template("home.html", books = test, len = len(test), pages = pages)
		
	return render_template("home.html", books = test, len = len(test), pages = pages)
	
if __name__ == "__main__":
    app.run(debug=True)