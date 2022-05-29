import os
import sqlite3

if os.path.isfile('data/student_detail_database.db')== False:
	conn = sqlite3.connect('data/student_detail_database.db')
	c = conn.cursor()
	# Create Table
	c.execute("""CREATE TABLE student_detail (
		admission_number integer,
		full_name text,
		gender text,
		birthday text,
		address text,
		birth_divisional text,
		birth_registrar text,
		Identity text	
		)""")
	conn.commit()
	conn.close()
else:
	os.remove("data/student_detail_database.db")
	conn = sqlite3.connect('data/student_detail_database.db')
	c = conn.cursor()
	# Create Table
	c.execute("""CREATE TABLE student_detail (
		admission_number integer,
		full_name text,
		gender text,
		birthday text,
		address text,
		birth_divisional text,
		birth_registrar text,
		Identity text	
		)""")
	conn.commit()
	conn.close()

if os.path.isfile('data/student_mark_database.db')== False:
	conn = sqlite3.connect('data/student_mark_database.db')
	c = conn.cursor()
	# Create Table
	c.execute("""CREATE TABLE student_mark (
		id integer,
		name text,
		year integer,
		buddhism integer,
		sinhala integer,
		mathematics integer,
		science integer,
		english integer,
		history integer,
		tamil integer,
		ict integer,
		agriculture integer,
		homescience integer,
		health integer,
		media integer,
		music integer,
		dancing integer,
		art integer,
		geography integer,
		civic integer
		)""")
	conn.commit()
	conn.close()
else:
	os.remove("data/student_mark_database.db")
	conn = sqlite3.connect('data/student_mark_database.db')
	c = conn.cursor()
	# Create Table
	c.execute("""CREATE TABLE student_mark (
		id integer,
		name text,
		year integer,
		buddhism integer,
		sinhala integer,
		mathematics integer,
		science integer,
		english integer,
		history integer,
		tamil integer,
		ict integer,
		agriculture integer,
		homescience integer,
		health integer,
		media integer,
		music integer,
		dancing integer,
		art integer,
		geography integer,
		civic integer
		)""")
	conn.commit()
	conn.close()