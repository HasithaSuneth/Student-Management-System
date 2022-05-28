import os
import glob
import sqlite3
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import ImageTk,Image
from operator import itemgetter

def logging_window(): # Logging Display
	logging = Tk()
	logging.title('Student Database Login')
	logging.resizable(False, False)
	logging.iconbitmap('data/image/icon.ico')
	#root.geometry("800x600")

	def confirm_logging(event=None):
		if logging_username_entry.get()=="admin" and logging_password_entry.get()=="admin":
			logging.destroy()
			main_menu_window()
		else:
			messagebox.showerror("Login Error", " Wrong username or password")
			#logging_username_entry.delete(0, END)
			logging_password_entry.delete(0, END)
	# Frames
	logging_logo_frame = LabelFrame(logging, padx=1, pady=1, bg='#424242', relief="flat")
	logging_logo_frame.grid(row=0, column=0, sticky=W+E)
	logging_add_frame = LabelFrame(logging, padx=1, pady=1, bg='#424242', relief="flat")
	logging_add_frame.grid(row=1, column=0, sticky=W+E)
	# Label
	logo_logging_label = Label(logging_logo_frame, text="PATHAKADA NAVODYA M.V", padx=5, bg='#424242', fg="white", relief="flat",font=("Verdana", "8","roman")) # logo image add later
	logging_username_label =Label(logging_add_frame, text="Username", padx=5, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"), anchor=W)
	logging_password_label =Label(logging_add_frame, text="Password", padx=5, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"), anchor=W)
	logo_logging_label.pack(fill=BOTH)
	logging_username_label.grid(row=0, column=0, sticky=W+E)
	logging_password_label.grid(row=2, column=0, sticky=W+E)
	# Entry
	logging_username_entry = Entry(logging_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=47, borderwidth=5)
	logging_password_entry = Entry(logging_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=47, borderwidth=5, show="*")
	logging_username_entry.grid(row=1, column=0, pady=(7,7), padx=(5,5))
	logging_password_entry.grid(row=3, column=0, pady=(7,7), padx=(5,5))
	logging_username_entry.bind('<Return>', lambda e: logging_password_entry.focus_set())
	logging_password_entry.bind('<Return>', confirm_logging)
	# Button
	confirm_logging_button = Button(logging_add_frame, text="Confirm", command=confirm_logging, width=10,height=1, relief="flat", font=("Comic", "10"), fg="white", activebackground ="#2c4c66", bg='#212121')
	confirm_logging_button.grid(row=4, column=0, pady=(10,10))
	mainloop()

def main_menu_window():
	main_menu = Tk()
	main_menu.title('Student Database Main Menu')
	main_menu.resizable(False, False)
	main_menu.iconbitmap('data/image/icon.ico')
	#root.geometry("800x600")

	def add_detail_enter(event):
		add_student_detail_button.config(image=add_details_focus_img)
	def add_detail_leave(event):
		add_student_detail_button.config(image=add_details_img) 
	def add_marks_enter(event):
		add_student_mark_button.config(image=add_marks_focus_img)
	def add_marks_leave(event):
		add_student_mark_button.config(image=add_marks_img) 
	def search_database_enter(event):
		search_student_button.config(image=search_database_focus_img)
	def search_database_leave(event):
		search_student_button.config(image=search_database_img) 
	def edit_marks_enter(event):
		edit_student_mark_button.config(image=edit_marks_focus_img)
	def edit_marks_leave(event):
		edit_student_mark_button.config(image=edit_marks_img) 

	logo_img = ImageTk.PhotoImage(Image.open("data/image/logo2.jpg"))
	add_details_img = ImageTk.PhotoImage(Image.open("data/image/add_detail.jpg"))
	add_details_focus_img = ImageTk.PhotoImage(Image.open("data/image/add_detail_focus.jpg"))
	search_database_img = ImageTk.PhotoImage(Image.open("data/image/search_database.jpg"))
	search_database_focus_img = ImageTk.PhotoImage(Image.open("data/image/search_database_focus.jpg"))
	add_marks_img = ImageTk.PhotoImage(Image.open("data/image/add_marks.jpg"))
	add_marks_focus_img = ImageTk.PhotoImage(Image.open("data/image/add_marks_focus.jpg"))
	edit_marks_img = ImageTk.PhotoImage(Image.open("data/image/edit_marks.jpg"))
	edit_marks_focus_img = ImageTk.PhotoImage(Image.open("data/image/edit_marks_focus.jpg"))
	# Frames
	main_menu_logo_frame = LabelFrame(main_menu, bg='#424242', relief="flat")
	main_menu_logo_frame.grid(row=0, column=1, sticky=W+E+N+S)
	main_menu_add_frame = LabelFrame(main_menu, bg='#424242', relief="flat")
	main_menu_add_frame.grid(row=0, column=2, sticky=W+E+N+S)
	main_menu_add2_frame = LabelFrame(main_menu, bg='#424242', relief="flat")
	main_menu_add2_frame.grid(row=0, column=0, sticky=W+E+N+S)
	# Label
	logo_main_menu_label = Label(main_menu_logo_frame, image=logo_img, width=138, height=145, text="PATHAKADA NAVODYA M.V", bg='#424242', fg="white", relief="flat",font=("Verdana", "8","roman")) # logo image add later
	logo_main_menu_label.pack(pady=(110,0))
	'''
	# Buttons
	add_student_detail_button = Button(main_menu_add2_frame, text="Add Student Details", image=add_details_img,command=add_student_detail_database,width=156,height=164, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e", bg='#424242', activebackground ="#424242")
	add_student_mark_button = Button(main_menu_add2_frame, text="Add Student Marks", image=add_marks_img, command=add_student_mark_database, width=155,height=162, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e",bg='#424242',  activebackground ="#424242")
	search_student_button = Button(main_menu_add_frame, text="Search Database", image=search_database_img, width=155,height=162, command=search_student_database, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e", bg='#424242', activebackground ="#424242")
	edit_student_mark_button = Button(main_menu_add_frame, text="Update Student Marks", image=edit_marks_img, command=edit_student_mark_database, width=155,height=162, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e", bg='#424242',  activebackground ="#424242")
	add_student_detail_button.grid(row=0, column=0,pady=(10,0))
	add_student_mark_button.grid(row=1, column=0,pady=(0,10))
	edit_student_mark_button.grid(row=1, column=0,pady=(0,10))
	search_student_button.grid(row=0, column=0,pady=(10,0))
	'''
	# LabelButtons
	add_student_detail_button = Label(main_menu_add2_frame, text="Add Student Details", image=add_details_img,width=156,height=164, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e", bg='#424242', activebackground ="#424242")
	add_student_mark_button = Label(main_menu_add2_frame, text="Add Student Marks", image=add_marks_img,  width=155,height=162, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e",bg='#424242',  activebackground ="#424242")
	search_student_button = Label(main_menu_add_frame, text="Search Database", image=search_database_img, width=155,height=162, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e", bg='#424242', activebackground ="#424242")
	edit_student_mark_button = Label(main_menu_add_frame, text="Update Student Marks", image=edit_marks_img, width=155,height=162, relief="flat", font=("Comic", "10", "bold"), fg="#1a237e", bg='#424242',  activebackground ="#424242")
	add_student_detail_button.grid(row=0, column=0,pady=(10,0))
	add_student_mark_button.grid(row=1, column=0,pady=(0,10))
	edit_student_mark_button.grid(row=1, column=0,pady=(0,10))
	search_student_button.grid(row=0, column=0,pady=(10,0))
	add_student_detail_button.bind('<Button-1>', add_student_detail_database)
	add_student_mark_button.bind('<Button-1>', add_student_mark_database)
	search_student_button.bind('<Button-1>',search_student_database)
	edit_student_mark_button.bind('<Button-1>',edit_student_mark_database)
	add_student_detail_button.bind('<Enter>',add_detail_enter)
	add_student_detail_button.bind('<Leave>',add_detail_leave)
	add_student_mark_button.bind('<Enter>',add_marks_enter)
	add_student_mark_button.bind('<Leave>',add_marks_leave)
	search_student_button.bind('<Enter>',search_database_enter)
	search_student_button.bind('<Leave>',search_database_leave)
	edit_student_mark_button.bind('<Enter>',edit_marks_enter)
	edit_student_mark_button.bind('<Leave>',edit_marks_leave)

	mainloop()

def add_student_detail_database(event):
	add_student_detail_window =  Toplevel()
	add_student_detail_window.title('Student Database - Add Student Details')
	add_student_detail_window.resizable(False, False)
	add_student_detail_window.iconbitmap('data/image/icon.ico')
	add_student_detail_window.grab_set()
	#root.geometry("800x600")

	def submit_student_details():
		if add_admission_num_entry.get()=="" or add_fullname_entry.get()=="" or add_address_entry.get()=="" or add_birth_division_entry.get()=="" or add_birth_registey_entry.get()=="" or add_identi_type_entry.get()=="":
			messagebox.showerror("Error", " Entry can't be blank" ,parent=add_student_detail_window)
		else:
			response3 = messagebox.askquestion("Attention", " Do you want to add Student Details into Database? ", parent=add_student_detail_window)
			if response3 == 'yes':
				conn = sqlite3.connect('data/student_detail_database.db')
				c = conn.cursor()
				if birthday_month.get() == 'January':
					birthday_month_temp = '1'
				elif birthday_month.get() == 'February':
					birthday_month_temp = '2'
				elif birthday_month.get() == 'March':
					birthday_month_temp = '3'
				elif birthday_month.get() == 'April':
					birthday_month_temp = '4'
				elif birthday_month.get() == 'May':
					birthday_month_temp = '5'
				elif birthday_month.get() == 'June':
					birthday_month_temp = '6'
				elif birthday_month.get() == 'July':
					birthday_month_temp = '7'
				elif birthday_month.get() == 'August':
					birthday_month_temp = '8'
				elif birthday_month.get() == 'September':
					birthday_month_temp = '9'
				elif birthday_month.get() == 'October':
					birthday_month_temp = '10'
				elif birthday_month.get() == 'November':
					birthday_month_temp = '11'
				elif birthday_month.get() == 'December':
					birthday_month_temp = '12'
				birthday_combine = str(birthday_day.get())+'/'+ birthday_month_temp +'/'+str(birthday_year.get())
				c.execute("INSERT INTO student_detail VALUES (:admission_num,:name,:gender,:birthday,:address,:birth_divisional,:birth_registrar,:Identity)",
					{
						'admission_num': add_admission_num_entry.get(),
						'name': add_fullname_entry.get(),
						'gender': add_gender_radio.get(),
						'birthday': birthday_combine,
						'address': add_address_entry.get(),
						'birth_divisional': add_birth_division_entry.get(),
						'birth_registrar': add_birth_registey_entry.get(),
						'Identity': add_identi_type_entry.get(),
					})
				conn.commit()
				conn.close()
				detail_clear_entry()
			
	def detail_clear_entry():
		add_admission_num_entry.delete(0,END)
		add_fullname_entry.delete(0,END)
		add_address_entry.delete(0,END)
		add_birth_division_entry.delete(0,END)
		add_birth_registey_entry.delete(0,END)
		add_identi_type_entry.delete(0,END)
		birthday_day.set('1')
		birthday_month.set('January')
		birthday_year.set('2000')

	# Frames
	add_student_detail_menu_frame = LabelFrame(add_student_detail_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_detail_menu_frame.grid(row=0, column=0, sticky=W+E)
	add_student_detail_add_frame = LabelFrame(add_student_detail_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_detail_add_frame.grid(row=1, column=0, sticky=W+E)
	add_student_detail_confirm_frame = LabelFrame(add_student_detail_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_detail_confirm_frame.grid(row=2, column=0, sticky=W+E)
	add_gender_frame = LabelFrame(add_student_detail_add_frame, bg='#424242', relief="flat")
	add_gender_frame.grid(row=2, column=1, sticky=W+E)
	add_birthday_frame = LabelFrame(add_student_detail_add_frame, bg='#424242', relief="flat")
	add_birthday_frame.grid(row=3, column=1, sticky=W+E)

	# Label
	logo_add_detail_label = Label(add_student_detail_menu_frame, text="PATHAKADA NAVODYA M.V", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Verdana", "8","roman")) # logo image add later
	add_admission_num_label = Label(add_student_detail_add_frame, text="Admission Number : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	add_fullname_label = Label(add_student_detail_add_frame, text="Full Name : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	add_gender_label = Label(add_student_detail_add_frame, text="Gender : ", padx=5, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	add_birthday_label = Label(add_student_detail_add_frame, text="Date Of Birth : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	add_address_label = Label(add_student_detail_add_frame, text="Address : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_birth_division_label = Label(add_student_detail_add_frame, text="Birth Divisional Secretariat : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	add_birth_registey_label = Label(add_student_detail_add_frame, text="Birth Registrar Office : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	add_identi_type_label = Label(add_student_detail_add_frame, text="Identity Type : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	birthday_day_label = 	Label(add_birthday_frame, text=" Day :", padx=1, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	birthday_month_label = Label(add_birthday_frame, text=" Month :", padx=1, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	birthday_year_label = Label(add_birthday_frame, text=" Year :", padx=1, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic")) 
	logo_add_detail_label.pack()
	add_admission_num_label.grid(row=0, column=0,sticky=W)
	add_fullname_label.grid(row=1, column=0,sticky=W)
	add_gender_label.grid(row=2, column=0,sticky=W)
	add_birthday_label.grid(row=3, column=0,sticky=W)
	add_address_label.grid(row=4, column=0,sticky=W)
	add_birth_division_label.grid(row=5, column=0,sticky=W)
	add_birth_registey_label.grid(row=6, column=0,sticky=W)
	add_identi_type_label.grid(row=7, column=0,sticky=W)
	birthday_day_label.grid(row=0, column=0)
	birthday_month_label.grid(row=0, column=2)
	birthday_year_label.grid(row=0, column=4)

	# Entry
	add_admission_num_entry = Entry(add_student_detail_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=60)
	add_fullname_entry = Entry(add_student_detail_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=60)
	add_address_entry = Entry(add_student_detail_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=60)
	add_birth_division_entry = Entry(add_student_detail_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=60)
	add_birth_registey_entry = Entry(add_student_detail_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=60)
	add_identi_type_entry = Entry(add_student_detail_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=60)
	add_admission_num_entry.grid(row=0, column=1, pady=2, padx=(2,8))
	add_fullname_entry.grid(row=1, column=1, pady=2, padx=(2,8))
	add_address_entry.grid(row=4, column=1, pady=2, padx=(2,8))
	add_birth_division_entry.grid(row=5, column=1, pady=2, padx=(2,8))
	add_birth_registey_entry.grid(row=6, column=1, pady=2, padx=(2,8))
	add_identi_type_entry.grid(row=7, column=1, pady=2, padx=(2,8))
	add_identi_type_entry.insert(0,'Sri Lankan - BC')

	# Button
	add_student_detail_submit_button = Button(add_student_detail_confirm_frame, text="Submit", bg='#212121', command=submit_student_details, width=10,height=1, relief="flat", font=("Comic", "10"), fg="white", activebackground ="#2c4c66")
	add_student_detail_submit_button.pack(side=RIGHT, padx=(0,8), pady=(2,10))

	# Radiobutton
	add_gender_radio = StringVar()
	Radiobutton(add_gender_frame, text="Male", variable=add_gender_radio, value='M', width=10, relief='flat', anchor=W, bg='#424242', font=("Comic Sans MS", "8", "italic"), fg="White", selectcolor='#424242', activebackground='#424242').grid(row=0, column=0)
	Radiobutton(add_gender_frame, text="Female", variable=add_gender_radio, value='F', width=10, relief='flat', anchor=W, bg='#424242', font=("Comic Sans MS", "8", "italic"), fg="White", selectcolor='#424242', activebackground='#424242').grid(row=0, column=1)
	add_gender_radio.set('M')

	# Dropbox
	birthday_day = IntVar()
	birthday_month = StringVar()
	birthday_year = IntVar()
	days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
	months = ['January','February','March','April','May','June','July','August','September','October','November','December']
	years = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
	birthday_day_box = OptionMenu(add_birthday_frame, birthday_day, *days)
	birthday_day_box.config(width=5, bg='#515A5A', font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=1,highlightthickness=0, relief='flat')
	birthday_day_box["menu"].config(bg='#515A5A', font=("times","9","bold italic"), fg="White", activebackground="#2c4c66")
	birthday_month_box = OptionMenu(add_birthday_frame, birthday_month, *months)
	birthday_month_box.config(width=10, bg='#515A5A', font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=1,highlightthickness=0, relief='flat')
	birthday_month_box["menu"].config(bg='#515A5A', font=("times","9","bold italic"), fg="White", activebackground="#2c4c66")
	birthday_year_box = OptionMenu(add_birthday_frame, birthday_year, *years)
	birthday_year_box.config(width=6, bg='#515A5A', font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=1,highlightthickness=0, relief='flat')
	birthday_year_box["menu"].config(bg='#515A5A', font=("times","9","bold italic"), fg="White", activebackground="#2c4c66")
	birthday_day_box.grid(row=0, column=1)
	birthday_month_box.grid(row=0, column=3)
	birthday_year_box.grid(row=0, column=5)
	birthday_day.set('1')
	birthday_month.set('January')
	birthday_year.set('2000')

def edit_student_mark_database(event):
	edit_student_mark_window =  Toplevel()
	edit_student_mark_window.title('Student Database - Update / Delete Student Marks')
	edit_student_mark_window.resizable(False, False)
	edit_student_mark_window.iconbitmap('data/image/icon.ico')
	edit_student_mark_window.grab_set()
	#root.geometry("800x600")
	global oid_of_edit_mark
	oid_of_edit_mark = ''

	def update_student_marks():
		global student_name_mark
		global student_id_mark
		global oid_of_edit_mark
		try:
			if student_name_mark == "" or student_id_mark == "":
				messagebox.showerror("Error", " Search Student For Update Marks" ,parent=edit_student_mark_window)
			else:
				if edit_grade_mark_entry.get() == '' or edit_term_mark_entry.get() == '' or edit_year_mark_entry.get() == '':
					messagebox.showerror("Error", " Grade, Year & Trem can't be blank!" ,parent=edit_student_mark_window)
				else:
					response1 = messagebox.askquestion("Attention", " Do you want to update Student Marks into Database? ", parent=edit_student_mark_window)
					if response1 == "yes":
						marks_year_temp = 'Grade'+str(edit_grade_mark_entry.get())+' Term'+str(edit_term_mark_entry.get())+' '+str(edit_year_mark_entry.get())
						conn = sqlite3.connect('data/student_mark_database.db')
						c = conn.cursor()
						c.execute("""UPDATE student_mark SET
							id = :id,
							name = :name,
							year = :year,
							buddhism = :buddhism,
							sinhala = :sinhala,
							mathematics = :mathematics,
							science = :science,
							english = :english,
							history = :history,
							tamil = :tamil,
							ict = :ict,
							agriculture = :agriculture,
							homescience = :homescience,
							health = :health,
							media = :media,
							music = :music,
							dancing = :dancing,
							art = :art,
							geography = :geography,
							civic = :civic
							WHERE oid = :oid""",
							{
								'id': student_id_mark,
								'name': student_name_mark,
								'year': marks_year_temp,
								'buddhism': edit_buddhism_mark_entry.get(),
								'sinhala': edit_sinhala_mark_entry.get(),
								'mathematics': edit_mathematics_mark_entry.get(),
								'science': edit_science_mark_entry.get(),
								'english': edit_english_mark_entry.get(),
								'history': edit_history_mark_entry.get(),
								'tamil': edit_tamil_mark_entry.get(),
								'ict': edit_ict_mark_entry.get(),
								'agriculture': edit_agriculture_mark_entry.get(),
								'homescience': edit_homescience_mark_entry.get(),
								'health': edit_health_mark_entry.get(),
								'media': edit_media_mark_entry.get(),
								'music': edit_music_mark_entry.get(),
								'dancing': edit_dancing_mark_entry.get(),
								'art': edit_art_mark_entry.get(),
								'geography': edit_geography_mark_entry.get(),
								'civic': edit_civic_mark_entry.get(),
								'oid': oid_of_edit_mark
							})
						conn.commit()
						conn.close()
						student_name_mark = ""
						student_id_mark = ""
						oid_of_edit_mark = ""
						mark_clear_entry()
						messagebox.showinfo("Info", " Student Marks Updated " ,parent=edit_student_mark_window)
					else:
						response2 = messagebox.askquestion("Attention", " Do you want to clear entered data? ", parent=edit_student_mark_window)
						if response2 == "yes":
							mark_clear_entry()	
		except:
			messagebox.showerror("Error", " Search Student For Update Marks" ,parent=edit_student_mark_window)

	def mark_clear_entry():		
		edit_student_id_mark_label2.config(text="None")
		edit_student_name_mark_label2.config(text="None")
		edit_year_mark_entry.delete(0,END)
		edit_grade_mark_entry.delete(0,END)
		edit_term_mark_entry.delete(0,END)
		edit_buddhism_mark_entry.delete(0,END)
		edit_sinhala_mark_entry.delete(0,END)
		edit_mathematics_mark_entry.delete(0,END)
		edit_science_mark_entry.delete(0,END)
		edit_english_mark_entry.delete(0,END)
		edit_history_mark_entry.delete(0,END)
		edit_tamil_mark_entry.delete(0,END)
		edit_ict_mark_entry.delete(0,END)
		edit_agriculture_mark_entry.delete(0,END)
		edit_homescience_mark_entry.delete(0,END)
		edit_health_mark_entry.delete(0,END)
		edit_media_mark_entry.delete(0,END)
		edit_music_mark_entry.delete(0,END)
		edit_dancing_mark_entry.delete(0,END)
		edit_art_mark_entry.delete(0,END)
		edit_geography_mark_entry.delete(0,END)
		edit_civic_mark_entry.delete(0,END)
		edit_student_id_mark_search_entry.delete(0,END)
		edit_student_name_mark_search_entry.delete(0,END)

	def delete_student_marks():
		global student_name_mark
		global student_id_mark
		global oid_of_edit_mark
		if oid_of_edit_mark !='':
			response4 = messagebox.askquestion("Warning", " Do you want to DELETE All Marks? \n This process can't be undo", parent=edit_student_mark_window)
			if response4 == 'yes':
				conn = sqlite3.connect('data/student_mark_database.db')
				c = conn.cursor()
				c.execute("DELETE from student_mark WHERE oid="+ str(oid_of_edit_mark))
				conn.commit()
				conn.close()
				student_name_mark = ""
				student_id_mark = ""
				oid_of_edit_mark = ""
				mark_clear_entry()
				messagebox.showinfo("Info", " Student Marks Deleted " ,parent=edit_student_mark_window)
		else:
			messagebox.showerror("Error", " Search Student For Delete All Marks" ,parent=edit_student_mark_window)
		
	def search_student_marks():
		def edit_name_mark(event):
			if mark_search_list.curselection() != ():
				global student_name_mark
				global student_id_mark
				student_name_mark = edit_mark_search_record[mark_search_list.curselection()[0]][1]
				student_id_mark = edit_mark_search_record[mark_search_list.curselection()[0]][0]
				mark_search_window.destroy()
				edit_year_mark()

		def edit_year_mark():
			def edit_year_show_mark(event):
				if year_search_list.curselection() != ():
					mark_clear_entry()
					global oid_of_edit_mark
					oid_of_edit_mark = edit_mark_year_search_record[year_search_list.curselection()[0]][20]
					temp = edit_mark_year_search_record[year_search_list.curselection()[0]][2]
					edit_student_id_mark_label2.config(text=student_id_mark)
					edit_student_name_mark_label2.config(text=student_name_mark)
					edit_year_mark_entry.insert(END, temp.split(" ",2)[2])
					edit_grade_mark_entry.insert(END,temp.split(" ",2)[0].replace('Grade',''))
					edit_term_mark_entry.insert(END,temp.split(" ",2)[1].replace('Term',''))
					edit_buddhism_mark_entry.insert(END, edit_mark_year_search_record[year_search_list.curselection()[0]][3])
					edit_sinhala_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][4])
					edit_mathematics_mark_entry .insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][5])
					edit_science_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][6])
					edit_english_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][7])
					edit_history_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][8])
					edit_tamil_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][9])
					edit_ict_mark_entry .insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][10])
					edit_agriculture_mark_entry .insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][11])
					edit_homescience_mark_entry .insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][12])
					edit_health_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][13])
					edit_media_mark_entry .insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][14])
					edit_music_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][15])
					edit_dancing_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][16])
					edit_art_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][17])
					edit_geography_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][18])
					edit_civic_mark_entry.insert(END,edit_mark_year_search_record[year_search_list.curselection()[0]][19])
					year_search_window.destroy()

			# Display
			year_search_window = Toplevel()
			year_search_window.title('Student Database - Search Result')
			year_search_window.resizable(False, False)
			year_search_window.iconbitmap('data/image/icon.ico')
			year_search_window.grab_set()
			# Frame
			year_search_frame = LabelFrame(year_search_window, padx=0, pady=0,  bg="#424242", relief="flat")
			year_search_frame.grid(row=0, column=0, sticky=W+E)
			# Scrollbar
			year_scrollbar = Scrollbar(year_search_frame)
			year_scrollbar.pack(side=RIGHT, fill=Y)
			# Listbox
			year_search_list = Listbox(year_search_frame, width=50, height=10, yscrollcommand=year_scrollbar.set, bg="#424949", font=("Helvetica", "9"), highlightthickness=0, selectbackground="#408f9b", fg="White", relief="flat", bd=0)
			year_search_list.pack(side=LEFT, fill=BOTH, pady=(3,0))
			year_search_list.delete(0,END)
			year_search_list.bind('<<ListboxSelect>>', edit_year_show_mark)
			year_scrollbar.config(command=year_search_list.yview)

			global edit_mark_year_search_record
			conn = sqlite3.connect('data/student_mark_database.db')
			c = conn.cursor()
			c.execute("SELECT *, oid FROM student_mark WHERE id like '%'||?||'%'",(student_id_mark,))
			edit_mark_year_search_record = c.fetchall()
			conn.commit()
			conn.close()
			for show in edit_mark_year_search_record:
				show_name='     '+str(itemgetter(2)(show))
				year_search_list.insert(END, show_name)
			
		global edit_mark_search_record
		edit_mark_search_record = ()
		if edit_student_id_mark_search_entry.get() != "":
			search_id_temp = edit_student_id_mark_search_entry.get()
			search_id = search_id_temp.split(" ",2)[0]
			conn = sqlite3.connect('data/student_detail_database.db')
			c = conn.cursor()
			c.execute("SELECT *, oid FROM student_detail WHERE admission_number like '%'||?||'%'",(search_id,))
			edit_mark_search_record = c.fetchall()
			conn.commit()
			conn.close()

		elif edit_student_name_mark_search_entry.get() != "":
			search_name_temp = edit_student_name_mark_search_entry.get()
			search_name = search_name_temp.split(" ",2)[0]
			conn = sqlite3.connect('data/student_detail_database.db')
			c = conn.cursor()
			c.execute("SELECT *, oid FROM student_detail WHERE full_name like '%'||?||'%'",(search_name,))
			edit_mark_search_record = c.fetchall()
			conn.commit()
			conn.close()
		else:
			messagebox.showerror("Error", " Enter Student ID or Name for search" ,parent=edit_student_mark_window)
		if edit_mark_search_record != ():
			# Display
			mark_search_window = Toplevel()
			mark_search_window.title('Student Database - Search Result')
			mark_search_window.resizable(False, False)
			mark_search_window.iconbitmap('data/image/icon.ico')
			mark_search_window.grab_set()
			# Frame
			mark_search_frame = LabelFrame(mark_search_window, padx=0, pady=0,  bg="#424242", relief="flat")
			mark_search_frame.grid(row=0, column=0, sticky=W+E)
			# Scrollbar
			mark_scrollbar = Scrollbar(mark_search_frame)
			mark_scrollbar.pack(side=RIGHT, fill=Y)
			# Listbox
			mark_search_list = Listbox(mark_search_frame, width=75, height=10, yscrollcommand=mark_scrollbar.set, bg="#424949", font=("Helvetica", "9"), highlightthickness=0, selectbackground="#408f9b", fg="White", relief="flat", bd=0)
			mark_search_list.pack(side=LEFT, fill=BOTH, pady=(3,0))
			mark_search_list.delete(0,END)
			mark_search_list.bind('<<ListboxSelect>>', edit_name_mark)
			for show in edit_mark_search_record:
				show_name=str(itemgetter(0)(show))+"   :   "+str(itemgetter(1)(show))
				mark_search_list.insert(END, show_name)
			mark_scrollbar.config(command=mark_search_list.yview)

	def callback(inStr, acttyp):
		if acttyp == '1':
			if not inStr.isdigit():
				return False
		return True

	# Frames
	edit_student_mark_menu_frame = LabelFrame(edit_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	edit_student_mark_search_frame = LabelFrame(edit_student_mark_window, padx=1, pady=1, bg='#424242')
	edit_student_mark_id_name_frame = LabelFrame(edit_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	edit_student_mark_year_frame = LabelFrame(edit_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	edit_student_mark_subject_frame = LabelFrame(edit_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	edit_student_mark_submit_frame = LabelFrame(edit_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	edit_student_mark_menu_frame.grid(row=0, column=0, sticky=W+E)
	edit_student_mark_search_frame.grid(row=1, column=0, sticky=W+E)
	edit_student_mark_id_name_frame.grid(row=2, column=0, sticky=W+E)
	edit_student_mark_year_frame.grid(row=3, column=0, sticky=W+E)
	edit_student_mark_subject_frame.grid(row=4, column=0, sticky=W+E)
	edit_student_mark_submit_frame.grid(row=5, column=0, sticky=W+E)
	# Label
	edit_student_id_mark_search_label = Label(edit_student_mark_search_frame, text="Student ID :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_student_name_mark_search_label = Label(edit_student_mark_search_frame, text="Student Name :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	logo_edit_mark_label = Label(edit_student_mark_menu_frame, text="PATHAKADA NAVODYA M.V", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Verdana", "8","roman")) # logo image add later
	edit_student_id_mark_label1 = Label(edit_student_mark_id_name_frame, text="Student ID :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_student_id_mark_label2 = Label(edit_student_mark_id_name_frame, text="None", width=65, padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_student_name_mark_label1 = Label(edit_student_mark_id_name_frame, text="Student Name :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_student_name_mark_label2 = Label(edit_student_mark_id_name_frame, text="None", width=65, padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_year_mark_label = Label(edit_student_mark_year_frame, text=" Year : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_buddhism_mark_label = Label(edit_student_mark_subject_frame, text="Buddhism :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_sinhala_mark_label = Label(edit_student_mark_subject_frame, text="First Language- Sinhala :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_mathematics_mark_label = Label(edit_student_mark_subject_frame, text="Mathematics :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_science_mark_label = Label(edit_student_mark_subject_frame, text="Science :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_english_mark_label = Label(edit_student_mark_subject_frame, text="English :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_history_mark_label = Label(edit_student_mark_subject_frame, text="History :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_tamil_mark_label = Label(edit_student_mark_subject_frame, text="Tamil :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_ict_mark_label = Label(edit_student_mark_subject_frame, text="Information and communication Technology :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_agriculture_mark_label = Label(edit_student_mark_subject_frame, text="Agriculture :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_homescience_mark_label = Label(edit_student_mark_subject_frame, text="Homescience :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_health_mark_label = Label(edit_student_mark_subject_frame, text="Health & physical Education :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_media_mark_label = Label(edit_student_mark_subject_frame, text="Communication & Media studies :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_music_mark_label = Label(edit_student_mark_subject_frame, text="Music :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_dancing_mark_label = Label(edit_student_mark_subject_frame, text="Dancing :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_art_mark_label = Label(edit_student_mark_subject_frame, text="Art :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_geography_mark_label = Label(edit_student_mark_subject_frame, text="Geography :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_civic_mark_label = Label(edit_student_mark_subject_frame, text="Civic Education :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_grade_mark_label = Label(edit_student_mark_year_frame, text="Grade : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	edit_term_mark_label = Label(edit_student_mark_year_frame, text=" Term : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))

	logo_edit_mark_label.pack()
	edit_student_id_mark_search_label.grid(row=0, column=0,sticky=W)
	edit_student_name_mark_search_label.grid(row=0, column=2,sticky=W)
	edit_student_id_mark_label1.grid(row=0, column=0,sticky=W)
	edit_student_name_mark_label1.grid(row=1, column=0,sticky=W)
	edit_student_id_mark_label2.grid(row=0, column=1,sticky=W)
	edit_student_name_mark_label2.grid(row=1, column=1,sticky=W)
	edit_year_mark_label.grid(row=0, column=2,sticky=W)
	edit_buddhism_mark_label.grid(row=3, column=0,sticky=W)
	edit_sinhala_mark_label.grid(row=4, column=0,sticky=W)
	edit_mathematics_mark_label.grid(row=5, column=0,sticky=W)
	edit_science_mark_label.grid(row=6, column=0,sticky=W)
	edit_english_mark_label.grid(row=7, column=0,sticky=W)
	edit_history_mark_label.grid(row=8, column=0,sticky=W)
	edit_tamil_mark_label.grid(row=9, column=0,sticky=W)
	edit_ict_mark_label.grid(row=10, column=0,sticky=W)
	edit_agriculture_mark_label.grid(row=11, column=0,sticky=W)
	edit_homescience_mark_label.grid(row=12, column=0,sticky=W)
	edit_health_mark_label.grid(row=13, column=0,sticky=W)
	edit_media_mark_label.grid(row=14, column=0,sticky=W)
	edit_music_mark_label.grid(row=15, column=0,sticky=W)
	edit_dancing_mark_label.grid(row=16, column=0,sticky=W)
	edit_art_mark_label.grid(row=17, column=0,sticky=W)
	edit_geography_mark_label.grid(row=18, column=0,sticky=W)
	edit_civic_mark_label.grid(row=19, column=0,sticky=W)
	edit_grade_mark_label.grid(row=0, column=0,sticky=W)
	edit_term_mark_label.grid(row=0, column=4,sticky=W)

	# Entry
	edit_student_id_mark_search_entry = Entry(edit_student_mark_search_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=10)
	edit_student_name_mark_search_entry = Entry(edit_student_mark_search_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=30)
	edit_year_mark_entry = Entry(edit_student_mark_year_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=15)
	edit_buddhism_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_sinhala_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_mathematics_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_science_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_english_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_history_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_tamil_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_ict_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_agriculture_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_homescience_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_health_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_media_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_music_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_dancing_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_art_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_geography_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_civic_mark_entry = Entry(edit_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	edit_grade_mark_entry = Entry(edit_student_mark_year_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=6)
	edit_term_mark_entry = Entry(edit_student_mark_year_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=5)

	edit_student_id_mark_search_entry.grid(row=0, column=1,sticky=W)
	edit_student_name_mark_search_entry.grid(row=0, column=3,sticky=W)
	edit_year_mark_entry.grid(row=0, column=3,sticky=W)
	edit_buddhism_mark_entry.grid(row=3, column=1,sticky=W)
	edit_sinhala_mark_entry.grid(row=4, column=1,sticky=W)
	edit_mathematics_mark_entry.grid(row=5, column=1,sticky=W)
	edit_science_mark_entry.grid(row=6, column=1,sticky=W)
	edit_english_mark_entry.grid(row=7, column=1,sticky=W)
	edit_history_mark_entry.grid(row=8, column=1,sticky=W)
	edit_tamil_mark_entry.grid(row=9, column=1,sticky=W)
	edit_ict_mark_entry.grid(row=10, column=1,sticky=W)
	edit_agriculture_mark_entry.grid(row=11, column=1,sticky=W)
	edit_homescience_mark_entry.grid(row=12, column=1,sticky=W)
	edit_health_mark_entry.grid(row=13, column=1,sticky=W)
	edit_media_mark_entry.grid(row=14, column=1,sticky=W)
	edit_music_mark_entry.grid(row=15, column=1,sticky=W)
	edit_dancing_mark_entry.grid(row=16, column=1,sticky=W)
	edit_art_mark_entry.grid(row=17, column=1,sticky=W)
	edit_geography_mark_entry.grid(row=18, column=1,sticky=W)
	edit_civic_mark_entry.grid(row=19, column=1,sticky=W)
	edit_grade_mark_entry.grid(row=0, column=1,sticky=W)
	edit_term_mark_entry.grid(row=0, column=5,sticky=W)
	edit_buddhism_mark_entry.config(validate='key', validatecommand=(edit_buddhism_mark_entry.register(callback),'%P','%d'))
	edit_sinhala_mark_entry.config(validate='key', validatecommand=(edit_sinhala_mark_entry.register(callback),'%P','%d'))
	edit_mathematics_mark_entry.config(validate='key', validatecommand=(edit_mathematics_mark_entry.register(callback),'%P','%d'))
	edit_science_mark_entry.config(validate='key', validatecommand=(edit_science_mark_entry.register(callback),'%P','%d'))
	edit_english_mark_entry.config(validate='key', validatecommand=(edit_english_mark_entry.register(callback),'%P','%d'))
	edit_history_mark_entry.config(validate='key', validatecommand=(edit_history_mark_entry.register(callback),'%P','%d'))
	edit_tamil_mark_entry.config(validate='key', validatecommand=(edit_tamil_mark_entry.register(callback),'%P','%d'))
	edit_ict_mark_entry.config(validate='key', validatecommand=(edit_ict_mark_entry.register(callback),'%P','%d'))
	edit_agriculture_mark_entry.config(validate='key', validatecommand=(edit_agriculture_mark_entry.register(callback),'%P','%d'))
	edit_homescience_mark_entry.config(validate='key', validatecommand=(edit_homescience_mark_entry.register(callback),'%P','%d'))
	edit_health_mark_entry.config(validate='key', validatecommand=(edit_health_mark_entry.register(callback),'%P','%d'))
	edit_media_mark_entry.config(validate='key', validatecommand=(edit_media_mark_entry.register(callback),'%P','%d'))
	edit_music_mark_entry.config(validate='key', validatecommand=(edit_music_mark_entry.register(callback),'%P','%d'))
	edit_dancing_mark_entry.config(validate='key', validatecommand=(edit_dancing_mark_entry.register(callback),'%P','%d'))
	edit_art_mark_entry.config(validate='key', validatecommand=(edit_art_mark_entry.register(callback),'%P','%d'))
	edit_geography_mark_entry.config(validate='key', validatecommand=(edit_geography_mark_entry.register(callback),'%P','%d'))
	edit_civic_mark_entry.config(validate='key', validatecommand=(edit_civic_mark_entry.register(callback),'%P','%d'))
	edit_year_mark_entry.config(validate='key', validatecommand=(edit_year_mark_entry.register(callback),'%P','%d'))
	edit_term_mark_entry.config(validate='key', validatecommand=(edit_term_mark_entry.register(callback),'%P','%d'))
	# Button
	edit_student_mark_search_button = Button(edit_student_mark_search_frame, text="Search", command=search_student_marks, width=15,height=1, relief="flat", font=("Comic", "9"), fg="white", activebackground ="#2c4c66", bg='#212121')
	edit_student_mark_submit_button = Button(edit_student_mark_submit_frame, text="Update", command=update_student_marks, width=25,height=1, relief="flat", font=("Comic", "10"), fg="white", activebackground ="#2c4c66", bg='#212121')
	edit_student_mark_delete_button = Button(edit_student_mark_submit_frame, text="Delete", command=delete_student_marks, width=15,height=1, relief="flat", font=("Comic", "10"), fg="white", activebackground ="#2c4c66", bg='#212121')
	edit_student_mark_delete_button.pack(side=RIGHT, padx=10, pady=5)
	edit_student_mark_submit_button.pack(pady=5)
	edit_student_mark_search_button.grid(row=0, column=4, padx=10)

def add_student_mark_database(event):
	add_student_mark_window =  Toplevel()
	add_student_mark_window.title('Student Database - Add Student Marks')
	add_student_mark_window.resizable(False, False)
	add_student_mark_window.iconbitmap('data/image/icon.ico')
	add_student_mark_window.grab_set()
	#root.geometry("800x600")

	def submit_student_marks():
		global student_name_mark
		global student_id_mark
		try:
			if student_name_mark == "" or student_id_mark == "":
				messagebox.showerror("Error", " Search Student For Add Marks" ,parent=add_student_mark_window)
			else:
				if add_grade_mark_entry.get() == '' or add_term_mark_entry.get() == '' or add_year_mark_entry.get() == '':
					messagebox.showerror("Error", " Grade, Year & Trem can't be blank!" ,parent=add_student_mark_window)
				else:
					response1 = messagebox.askquestion("Attention", " Do you want to add Student Marks into Database? ", parent=add_student_mark_window)
					if response1 == "yes":
						marks_year_temp = 'Grade'+str(add_grade_mark_entry.get())+' Term'+str(add_term_mark_entry.get())+' '+str(add_year_mark_entry.get())
						conn = sqlite3.connect('data/student_mark_database.db')
						c = conn.cursor()
						c.execute("INSERT INTO student_mark VALUES (:id,:name,:year,:buddhism,:sinhala,:mathematics,:science,:english,:history,:tamil,:ict,:agriculture,:homescience,:health,:media,:music,:dancing,:art,:geography,:civic)",
							{
								'id': student_id_mark,
								'name': student_name_mark,
								'year': marks_year_temp,
								'buddhism': add_buddhism_mark_entry.get(),
								'sinhala': add_sinhala_mark_entry.get(),
								'mathematics': add_mathematics_mark_entry.get(),
								'science': add_science_mark_entry.get(),
								'english': add_english_mark_entry.get(),
								'history': add_history_mark_entry.get(),
								'tamil': add_tamil_mark_entry.get(),
								'ict': add_ict_mark_entry.get(),
								'agriculture': add_agriculture_mark_entry.get(),
								'homescience': add_homescience_mark_entry.get(),
								'health': add_health_mark_entry.get(),
								'media': add_media_mark_entry.get(),
								'music': add_music_mark_entry.get(),
								'dancing': add_dancing_mark_entry.get(),
								'art': add_art_mark_entry.get(),
								'geography': add_geography_mark_entry.get(),
								'civic': add_civic_mark_entry.get(),

							})
						conn.commit()
						conn.close()
						mark_clear_entry()
						messagebox.showinfo("Info", " Student Marks Inserted Successfuly! " ,parent=add_student_mark_window)
					else:
						response2 = messagebox.askquestion("Attention", " Do you want to clear entered data? ", parent=add_student_mark_window)
						if response2 == "yes":
							mark_clear_entry()		
		except:
			messagebox.showerror("Error", " Search Student For Add Marks" ,parent=add_student_mark_window)

	def mark_clear_entry():
		global student_name_mark
		global student_id_mark
		student_name_mark = ""
		student_id_mark = ""
		add_student_id_mark_label2.config(text="None")
		add_student_name_mark_label2.config(text="None")
		add_year_mark_entry.delete(0,END)
		add_grade_mark_entry.delete(0,END)
		add_term_mark_entry.delete(0,END)
		add_buddhism_mark_entry.delete(0,END)
		add_sinhala_mark_entry.delete(0,END)
		add_mathematics_mark_entry.delete(0,END)
		add_science_mark_entry.delete(0,END)
		add_english_mark_entry.delete(0,END)
		add_history_mark_entry.delete(0,END)
		add_tamil_mark_entry.delete(0,END)
		add_ict_mark_entry.delete(0,END)
		add_agriculture_mark_entry.delete(0,END)
		add_homescience_mark_entry.delete(0,END)
		add_health_mark_entry.delete(0,END)
		add_media_mark_entry.delete(0,END)
		add_music_mark_entry.delete(0,END)
		add_dancing_mark_entry.delete(0,END)
		add_art_mark_entry.delete(0,END)
		add_geography_mark_entry.delete(0,END)
		add_civic_mark_entry.delete(0,END)
		add_student_id_mark_search_entry.delete(0,END)
		add_student_name_mark_search_entry.delete(0,END)

	def search_student_marks():
		def add_name_mark(event):
			if mark_search_list.curselection() != ():
				global student_name_mark
				global student_id_mark
				student_name_mark = mark_search_record[mark_search_list.curselection()[0]][1]
				student_id_mark = mark_search_record[mark_search_list.curselection()[0]][0]
				add_student_id_mark_label2.config(text=student_id_mark)
				add_student_name_mark_label2.config(text=student_name_mark)
				mark_search_window.destroy()

		global mark_search_record
		mark_search_record = ()
		if add_student_id_mark_search_entry.get() != "":
			search_id_temp = add_student_id_mark_search_entry.get()
			search_id = search_id_temp.split(" ",2)[0]
			conn = sqlite3.connect('data/student_detail_database.db')
			c = conn.cursor()
			c.execute("SELECT *, oid FROM student_detail WHERE admission_number like '%'||?||'%'",(search_id,))
			mark_search_record = c.fetchall()
			conn.commit()
			conn.close()

		elif add_student_name_mark_search_entry.get() != "":
			search_name_temp = add_student_name_mark_search_entry.get()
			search_name = search_name_temp.split(" ",2)[0]
			conn = sqlite3.connect('data/student_detail_database.db')
			c = conn.cursor()
			c.execute("SELECT *, oid FROM student_detail WHERE full_name like '%'||?||'%'",(search_name,))
			mark_search_record = c.fetchall()
			conn.commit()
			conn.close()
		else:
			messagebox.showerror("Error", " Enter Student ID or Name for search" ,parent=add_student_mark_window)
		if mark_search_record != ():
			# Display
			mark_search_window = Toplevel()
			mark_search_window.title('Student Database - Search Result')
			mark_search_window.resizable(False, False)
			mark_search_window.iconbitmap('data/image/icon.ico')
			mark_search_window.grab_set()
			# Frame
			mark_search_frame = LabelFrame(mark_search_window, padx=0, pady=0,  bg="#424242", relief="flat")
			mark_search_frame.grid(row=0, column=0, sticky=W+E)
			# Scrollbar
			mark_scrollbar = Scrollbar(mark_search_frame)
			mark_scrollbar.pack(side=RIGHT, fill=Y)
			# Listbox
			mark_search_list = Listbox(mark_search_frame, width=75, height=10, yscrollcommand=mark_scrollbar.set, bg="#424949", font=("Helvetica", "9"), highlightthickness=0, selectbackground="#408f9b", fg="White", relief="flat", bd=0)
			mark_search_list.pack(side=LEFT, fill=BOTH, pady=(3,0))
			mark_search_list.delete(0,END)
			mark_search_list.bind('<<ListboxSelect>>', add_name_mark)
			for show in mark_search_record:
				show_name=str(itemgetter(0)(show))+"   :   "+str(itemgetter(1)(show))
				mark_search_list.insert(END, show_name)
			mark_scrollbar.config(command=mark_search_list.yview)

	def callback(inStr, acttyp):
		if acttyp == '1':
			if not inStr.isdigit():
				return False
		return True

	global student_name_mark
	global student_id_mark
	student_name_mark = ""
	student_id_mark = ""

	# Frames
	add_student_mark_menu_frame = LabelFrame(add_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_mark_search_frame = LabelFrame(add_student_mark_window, padx=1, pady=1, bg='#424242')
	add_student_mark_id_name_frame = LabelFrame(add_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_mark_year_frame = LabelFrame(add_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_mark_subject_frame = LabelFrame(add_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_mark_submit_frame = LabelFrame(add_student_mark_window, padx=1, pady=1, bg='#424242', relief="flat")
	add_student_mark_menu_frame.grid(row=0, column=0, sticky=W+E)
	add_student_mark_search_frame.grid(row=1, column=0, sticky=W+E)
	add_student_mark_id_name_frame.grid(row=2, column=0, sticky=W+E)
	add_student_mark_year_frame.grid(row=3, column=0, sticky=W+E)
	add_student_mark_subject_frame.grid(row=4, column=0, sticky=W+E)
	add_student_mark_submit_frame.grid(row=5, column=0, sticky=W+E)
	# Label
	add_student_id_mark_search_label = Label(add_student_mark_search_frame, text="Student ID :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_student_name_mark_search_label = Label(add_student_mark_search_frame, text="Student Name :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	logo_add_mark_label = Label(add_student_mark_menu_frame, text="PATHAKADA NAVODYA M.V", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Verdana", "8","roman")) # logo image add later
	add_student_id_mark_label1 = Label(add_student_mark_id_name_frame, text="Student ID :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_student_id_mark_label2 = Label(add_student_mark_id_name_frame, text="None", width=65, padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_student_name_mark_label1 = Label(add_student_mark_id_name_frame, text="Student Name :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_student_name_mark_label2 = Label(add_student_mark_id_name_frame, text="None", width=65, padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_year_mark_label = Label(add_student_mark_year_frame, text=" Year : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_buddhism_mark_label = Label(add_student_mark_subject_frame, text="Buddhism :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_sinhala_mark_label = Label(add_student_mark_subject_frame, text="First Language- Sinhala :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_mathematics_mark_label = Label(add_student_mark_subject_frame, text="Mathematics :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_science_mark_label = Label(add_student_mark_subject_frame, text="Science :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_english_mark_label = Label(add_student_mark_subject_frame, text="English :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_history_mark_label = Label(add_student_mark_subject_frame, text="History :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_tamil_mark_label = Label(add_student_mark_subject_frame, text="Tamil :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_ict_mark_label = Label(add_student_mark_subject_frame, text="Information and communication Technology :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_agriculture_mark_label = Label(add_student_mark_subject_frame, text="Agriculture :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_homescience_mark_label = Label(add_student_mark_subject_frame, text="Homescience :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_health_mark_label = Label(add_student_mark_subject_frame, text="Health & physical Education :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_media_mark_label = Label(add_student_mark_subject_frame, text="Communication & Media studies :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_music_mark_label = Label(add_student_mark_subject_frame, text="Music :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_dancing_mark_label = Label(add_student_mark_subject_frame, text="Dancing :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_art_mark_label = Label(add_student_mark_subject_frame, text="Art :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_geography_mark_label = Label(add_student_mark_subject_frame, text="Geography :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_civic_mark_label = Label(add_student_mark_subject_frame, text="Civic Education :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_grade_mark_label = Label(add_student_mark_year_frame, text="Grade : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	add_term_mark_label = Label(add_student_mark_year_frame, text=" Term : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))

	logo_add_mark_label.pack()
	add_student_id_mark_search_label.grid(row=0, column=0,sticky=W)
	add_student_name_mark_search_label.grid(row=0, column=2,sticky=W)
	add_student_id_mark_label1.grid(row=0, column=0,sticky=W)
	add_student_name_mark_label1.grid(row=1, column=0,sticky=W)
	add_student_id_mark_label2.grid(row=0, column=1,sticky=W)
	add_student_name_mark_label2.grid(row=1, column=1,sticky=W)
	add_year_mark_label.grid(row=0, column=2,sticky=W)
	add_buddhism_mark_label.grid(row=3, column=0,sticky=W)
	add_sinhala_mark_label.grid(row=4, column=0,sticky=W)
	add_mathematics_mark_label.grid(row=5, column=0,sticky=W)
	add_science_mark_label.grid(row=6, column=0,sticky=W)
	add_english_mark_label.grid(row=7, column=0,sticky=W)
	add_history_mark_label.grid(row=8, column=0,sticky=W)
	add_tamil_mark_label.grid(row=9, column=0,sticky=W)
	add_ict_mark_label.grid(row=10, column=0,sticky=W)
	add_agriculture_mark_label.grid(row=11, column=0,sticky=W)
	add_homescience_mark_label.grid(row=12, column=0,sticky=W)
	add_health_mark_label.grid(row=13, column=0,sticky=W)
	add_media_mark_label.grid(row=14, column=0,sticky=W)
	add_music_mark_label.grid(row=15, column=0,sticky=W)
	add_dancing_mark_label.grid(row=16, column=0,sticky=W)
	add_art_mark_label.grid(row=17, column=0,sticky=W)
	add_geography_mark_label.grid(row=18, column=0,sticky=W)
	add_civic_mark_label.grid(row=19, column=0,sticky=W)
	add_grade_mark_label.grid(row=0, column=0,sticky=W)
	add_term_mark_label.grid(row=0, column=4,sticky=W)

	# Entry
	add_student_id_mark_search_entry = Entry(add_student_mark_search_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=10)
	add_student_name_mark_search_entry = Entry(add_student_mark_search_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=30)
	add_year_mark_entry = Entry(add_student_mark_year_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=15)
	add_buddhism_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_sinhala_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_mathematics_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_science_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_english_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_history_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_tamil_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_ict_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_agriculture_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_homescience_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_health_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_media_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_music_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_dancing_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_art_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_geography_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_civic_mark_entry = Entry(add_student_mark_subject_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=26)
	add_grade_mark_entry = Entry(add_student_mark_year_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=6)
	add_term_mark_entry = Entry(add_student_mark_year_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=5)

	add_student_id_mark_search_entry.grid(row=0, column=1,sticky=W)
	add_student_name_mark_search_entry.grid(row=0, column=3,sticky=W)
	add_year_mark_entry.grid(row=0, column=3,sticky=W)
	add_buddhism_mark_entry.grid(row=3, column=1,sticky=W)
	add_sinhala_mark_entry.grid(row=4, column=1,sticky=W)
	add_mathematics_mark_entry.grid(row=5, column=1,sticky=W)
	add_science_mark_entry.grid(row=6, column=1,sticky=W)
	add_english_mark_entry.grid(row=7, column=1,sticky=W)
	add_history_mark_entry.grid(row=8, column=1,sticky=W)
	add_tamil_mark_entry.grid(row=9, column=1,sticky=W)
	add_ict_mark_entry.grid(row=10, column=1,sticky=W)
	add_agriculture_mark_entry.grid(row=11, column=1,sticky=W)
	add_homescience_mark_entry.grid(row=12, column=1,sticky=W)
	add_health_mark_entry.grid(row=13, column=1,sticky=W)
	add_media_mark_entry.grid(row=14, column=1,sticky=W)
	add_music_mark_entry.grid(row=15, column=1,sticky=W)
	add_dancing_mark_entry.grid(row=16, column=1,sticky=W)
	add_art_mark_entry.grid(row=17, column=1,sticky=W)
	add_geography_mark_entry.grid(row=18, column=1,sticky=W)
	add_civic_mark_entry.grid(row=19, column=1,sticky=W)
	add_grade_mark_entry.grid(row=0, column=1,sticky=W)
	add_term_mark_entry.grid(row=0, column=5,sticky=W)
	add_buddhism_mark_entry.config(validate='key', validatecommand=(add_buddhism_mark_entry.register(callback),'%P','%d'))
	add_sinhala_mark_entry.config(validate='key', validatecommand=(add_sinhala_mark_entry.register(callback),'%P','%d'))
	add_mathematics_mark_entry.config(validate='key', validatecommand=(add_mathematics_mark_entry.register(callback),'%P','%d'))
	add_science_mark_entry.config(validate='key', validatecommand=(add_science_mark_entry.register(callback),'%P','%d'))
	add_english_mark_entry.config(validate='key', validatecommand=(add_english_mark_entry.register(callback),'%P','%d'))
	add_history_mark_entry.config(validate='key', validatecommand=(add_history_mark_entry.register(callback),'%P','%d'))
	add_tamil_mark_entry.config(validate='key', validatecommand=(add_tamil_mark_entry.register(callback),'%P','%d'))
	add_ict_mark_entry.config(validate='key', validatecommand=(add_ict_mark_entry.register(callback),'%P','%d'))
	add_agriculture_mark_entry.config(validate='key', validatecommand=(add_agriculture_mark_entry.register(callback),'%P','%d'))
	add_homescience_mark_entry.config(validate='key', validatecommand=(add_homescience_mark_entry.register(callback),'%P','%d'))
	add_health_mark_entry.config(validate='key', validatecommand=(add_health_mark_entry.register(callback),'%P','%d'))
	add_media_mark_entry.config(validate='key', validatecommand=(add_media_mark_entry.register(callback),'%P','%d'))
	add_music_mark_entry.config(validate='key', validatecommand=(add_music_mark_entry.register(callback),'%P','%d'))
	add_dancing_mark_entry.config(validate='key', validatecommand=(add_dancing_mark_entry.register(callback),'%P','%d'))
	add_art_mark_entry.config(validate='key', validatecommand=(add_art_mark_entry.register(callback),'%P','%d'))
	add_geography_mark_entry.config(validate='key', validatecommand=(add_geography_mark_entry.register(callback),'%P','%d'))
	add_civic_mark_entry.config(validate='key', validatecommand=(add_civic_mark_entry.register(callback),'%P','%d'))
	add_year_mark_entry.config(validate='key', validatecommand=(add_year_mark_entry.register(callback),'%P','%d'))
	add_term_mark_entry.config(validate='key', validatecommand=(add_term_mark_entry.register(callback),'%P','%d'))
	# Button
	add_student_mark_submit_button = Button(add_student_mark_submit_frame, text="Submit", command=submit_student_marks, width=30,height=1, relief="flat", font=("Comic", "10"), fg="white", activebackground ="#2c4c66", bg='#212121')
	add_student_mark_submit_button.pack(  pady=(2,10))
	add_student_mark_search_button = Button(add_student_mark_search_frame, text="Search", command=search_student_marks, width=15,height=1, relief="flat", font=("Comic", "9"), fg="white", activebackground ="#2c4c66", bg='#212121')
	add_student_mark_search_button.grid(row=0, column=4, padx=10)


def search_student_database(event):
	search_student_main_window =  Toplevel()
	search_student_main_window.title('Student Database - Search Student Details/Marks')
	search_student_main_window.resizable(False, False)
	search_student_main_window.iconbitmap('data/image/icon.ico')
	search_student_main_window.grab_set()
	#root.geometry("800x600")

	def search_main_details_search():
		def add_details_text(event):
			if search_main_details_search_list.curselection() != ():
				global student_name_search
				global student_id_search
				global student_gender_search
				global student_birthday_search
				global student_address_search
				global student_birth_divisional_search
				global student_birth_registrar_search
				global student_identity_search
				student_name_search = search_main_details[search_main_details_search_list.curselection()[0]][1]
				student_id_search = search_main_details[search_main_details_search_list.curselection()[0]][0]
				student_gender_search = search_main_details[search_main_details_search_list.curselection()[0]][2]
				student_birthday_search = search_main_details[search_main_details_search_list.curselection()[0]][3]
				student_address_search = search_main_details[search_main_details_search_list.curselection()[0]][4]
				student_birth_divisional_search = search_main_details[search_main_details_search_list.curselection()[0]][5]
				student_birth_registrar_search = search_main_details[search_main_details_search_list.curselection()[0]][6]
				student_identity_search = search_main_details[search_main_details_search_list.curselection()[0]][7]
				search_main_details_search_window.destroy()
				show_details_results_search()

		def show_details_results_search():
			search_student_main_search_text.config(state=NORMAL)
			search_student_main_search_text.delete('1.0', END)
			search_student_main_search_text.insert(END, '\n'+' Student ID : '+ str(student_id_search) + '\n')
			search_student_main_search_text.insert(END, ' Student Name : '+ str(student_name_search) + '\n')
			search_student_main_search_text.insert(END, ' Gender : '+ str(student_gender_search) + '\n')
			search_student_main_search_text.insert(END, ' Date Of Birth  : '+ str(student_birthday_search) + '\n')
			search_student_main_search_text.insert(END, ' Address : '+ str(student_address_search) + '\n')
			search_student_main_search_text.insert(END, ' Birth Divisional Secretariat : '+ str(student_birth_divisional_search) + '\n')
			search_student_main_search_text.insert(END, ' Birth Registrar Office : '+ str(student_birth_registrar_search) + '\n')
			search_student_main_search_text.insert(END, ' Identity Type : '+ str(student_identity_search) + '\n')
			search_student_main_search_text.config(state=DISABLED)
			search_student_main_text_frame.grid(row=2, column=0, sticky=W+E)

		global search_main_details
		search_main_details = ()
		if search_student_main_id_entry.get() != "":
			search_id_temp = search_student_main_id_entry.get()
			search_id = search_id_temp.split(" ",2)[0]
			conn = sqlite3.connect('data/student_detail_database.db')
			c = conn.cursor()
			c.execute("SELECT *, oid FROM student_detail WHERE admission_number like '%'||?||'%'",(search_id,))
			search_main_details = c.fetchall()
			conn.commit()
			conn.close()

		elif search_student_main_name_entry.get() != "":
			search_name_temp = search_student_main_name_entry.get()
			search_name = search_name_temp.split(" ",2)[0]
			conn = sqlite3.connect('data/student_detail_database.db')
			c = conn.cursor()
			c.execute("SELECT *, oid FROM student_detail WHERE full_name like '%'||?||'%'",(search_name,))
			search_main_details = c.fetchall()
			conn.commit()
			conn.close()
		else:
			messagebox.showerror("Error", " Enter Student ID or Name for search" ,parent=search_student_main_window)
		if search_main_details != ():
			# Display
			search_main_details_search_window = Toplevel()
			search_main_details_search_window.title('Student Database - Search Result')
			search_main_details_search_window.resizable(False, False)
			search_main_details_search_window.iconbitmap('data/image/icon.ico')
			search_main_details_search_window.grab_set()
			# Frame
			search_main_details_search_frame = LabelFrame(search_main_details_search_window, padx=0, pady=0,  bg="#424242", relief="flat")
			search_main_details_search_frame.grid(row=0, column=0, sticky=W+E)
			# Scrollbar
			search_main_details_scrollbar = Scrollbar(search_main_details_search_frame)
			search_main_details_scrollbar.pack(side=RIGHT, fill=Y)
			# Listbox
			search_main_details_search_list = Listbox(search_main_details_search_frame, width=75, height=10, yscrollcommand=search_main_details_scrollbar.set, bg="#424949", font=("Helvetica", "9"), highlightthickness=0, selectbackground="#408f9b", fg="White", relief="flat", bd=0)
			search_main_details_search_list.pack(side=LEFT, fill=BOTH, pady=(3,0))
			search_main_details_search_list.delete(0,END)
			search_main_details_search_list.bind('<<ListboxSelect>>', add_details_text)
			for show in search_main_details:
				show_name=str(itemgetter(0)(show))+"   :   "+str(itemgetter(1)(show))
				search_main_details_search_list.insert(END, show_name)
			search_main_details_scrollbar.config(command=search_main_details_search_list.yview)

	def search_main_marks_search():
		if student_id_search == '':
			messagebox.showerror("Error", " Search Student Result Empty! \n Pl Search Student First" ,parent=search_student_main_window)
		else:
			# Display
			search_main_marks_search_window = Toplevel()
			search_main_marks_search_window.title('Student Database - Student Marks')
			search_main_marks_search_window.resizable(False, False)
			search_main_marks_search_window.iconbitmap('data/image/icon.ico')
			search_main_marks_search_window.grab_set()

			def show_student_marks():
				global search_main_marks
				search_mark_years = []
				search_mark_years.clear()
				search_id = student_id_search
				conn = sqlite3.connect('data/student_mark_database.db')
				c = conn.cursor()
				c.execute("SELECT *, oid FROM student_mark WHERE id like '%'||?||'%'",(search_id,))
				search_main_marks = c.fetchall()
				conn.commit()
				conn.close()
				for result in search_main_marks:
					search_mark_years.append(result[2])
				# Optionmenu
				if search_mark_years == []:
					search_mark_years = ['Empty']
				global year_semester
				year_semester = StringVar()	
				search_student_marks_year_box = OptionMenu(search_main_marks_marks_year_search_frame, year_semester, *search_mark_years, command=year_vise_result)
				search_student_marks_year_box.config(width=25, bg='#515A5A', font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=1,highlightthickness=0, relief='flat')
				search_student_marks_year_box["menu"].config(bg='#515A5A', font=("times","9","bold italic"), fg="White", activebackground="#2c4c66")
				search_student_marks_year_box.grid(row=2, column=1,sticky=W, pady=(0,5))
				year_semester.set("Select")

			def year_vise_result(event):
				for result in search_main_marks:
					if result[2] == year_semester.get():
						student_rank(result)
						show_marks_results_search(result)

			def show_marks_results_search(input):
				temp = itemgetter(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)(input)
				temp = [i for i in temp if i != '']
				total_marks = sum(temp)
				average_marks = int(total_marks / len(temp))
				search_student_marks_textbox.config(state=NORMAL)
				search_student_marks_textbox.delete('1.0', END)
				search_student_marks_textbox.insert(END, '\n'+' Buddhism : '+ str(input[3]) + '\n')
				search_student_marks_textbox.insert(END, ' First Language - Sinhala : '+ str(input[4]) + '\n')
				search_student_marks_textbox.insert(END, ' Mathematics  : '+ str(input[5]) + '\n')
				search_student_marks_textbox.insert(END, ' Science : '+ str(input[6]) + '\n')
				search_student_marks_textbox.insert(END, ' English  : '+ str(input[7]) + '\n')
				search_student_marks_textbox.insert(END, ' History : '+ str(input[8]) + '\n')
				search_student_marks_textbox.insert(END, ' Tamil : '+ str(input[9]) + '\n')
				search_student_marks_textbox.insert(END, ' Information and communication Technology : '+ str(input[10]) + '\n')
				search_student_marks_textbox.insert(END, ' Agriculture  : '+ str(input[11]) + '\n')
				search_student_marks_textbox.insert(END, ' Homescience : '+ str(input[12]) + '\n')
				search_student_marks_textbox.insert(END, ' Health & physical Education: '+ str(input[13]) + '\n')
				search_student_marks_textbox.insert(END, ' Communication & Media studies : '+ str(input[14]) + '\n')
				search_student_marks_textbox.insert(END, ' Music : '+ str(input[15]) + '\n')
				search_student_marks_textbox.insert(END, ' Dancing : '+ str(input[16]) + '\n')
				search_student_marks_textbox.insert(END, ' Art : '+ str(input[17]) + '\n')
				search_student_marks_textbox.insert(END, ' Geography : '+ str(input[18]) + '\n')
				search_student_marks_textbox.insert(END, ' Civic Education : '+ str(input[19]) + '\n'+ '\n')
				search_student_marks_textbox.insert(END, ' Total : '+ str(total_marks) + ' out of '+ str(len(temp)*100)+'\n')
				search_student_marks_textbox.insert(END, ' Average : '+ str(average_marks) + ' per subject '+ '\n')
				search_student_marks_textbox.insert(END, ' Rank : '+ str(student_rank(input)) + '\n')
				search_student_marks_textbox.config(state=DISABLED)
				search_main_marks_marks_search_frame.grid(row=2, column=0, sticky=W+E)

			def student_rank(select):
				rank_list = []
				rank_list.clear()
				conn = sqlite3.connect('data/student_mark_database.db')
				c = conn.cursor()
				c.execute("SELECT *, oid FROM student_mark WHERE year like '%'||?||'%'",(select[2],))
				rank_search = c.fetchall()
				conn.commit()
				conn.close()
				for rank in rank_search:
					temp1 = itemgetter(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)(rank)
					temp1 = [i for i in temp1 if i != '']
					rank_list.append(sum(temp1))
						
				rank_list.sort(key=int, reverse=True)
				temp2 = itemgetter(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)(select)
				temp2= [i for i in temp2 if i != '']
				rank = rank_list.index(sum(temp2))+1
				rank_total = len(rank_list)
				if rank == 1:
					num = 'st'
				elif rank == 2:
					num = 'nd'
				elif rank == 3:
					num = 'rd'
				else:
					num = 'th'
				student_rank = str(rank)+ num + ' place from '+ str(rank_total) + ' students'
				return student_rank
				
			# Frame
			search_main_marks_main_search_frame = LabelFrame(search_main_marks_search_window, padx=0, pady=0,  bg="#424242", relief="flat")
			search_main_marks_marks_search_frame = LabelFrame(search_main_marks_search_window, padx=0, pady=0,  bg="#424242", relief="flat")
			search_main_marks_marks_year_search_frame = LabelFrame(search_main_marks_search_window, padx=0, pady=0,  bg="#424242", relief="flat")
			search_main_marks_main_search_frame.grid(row=0, column=0, sticky=W+E)
			#search_main_marks_marks_search_frame.grid(row=2, column=0, sticky=W+E)
			search_main_marks_marks_year_search_frame.grid(row=1, column=0, sticky=W+E)
			# Label 
			search_student_marks_name_label = Label(search_main_marks_main_search_frame, text="Student Name : "+ str(student_name_search),width=80, padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"),anchor=W)
			search_student_marks_id_label = Label(search_main_marks_main_search_frame, text="Student ID : "+ str(student_id_search), padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"),anchor=W)
			search_student_marks_year_label = Label(search_main_marks_marks_year_search_frame, text="Year & Term : ", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
			search_student_marks_name_label.grid(row=1, column=0,sticky=W)
			search_student_marks_id_label.grid(row=0, column=0,sticky=W)
			search_student_marks_year_label.grid(row=2, column=0,sticky=W)
			# Textbox
			search_student_marks_textbox = Text(search_main_marks_marks_search_frame,width=65, height=23, bg='#424242', relief='flat', fg='white', state=DISABLED)
			search_student_marks_textbox.grid(row=0, column=0)
			show_student_marks()

	global student_name_search
	global student_id_search
	student_id_search = ''
	# Frames
	search_student_main_logo_frame = LabelFrame(search_student_main_window, padx=1, pady=1, bg='#424242', relief="flat")
	search_student_main_search_frame = LabelFrame(search_student_main_window, padx=1, pady=1, bg='#424242', relief="flat")
	search_student_main_text_frame = LabelFrame(search_student_main_window, padx=1, pady=1, bg='#424242', relief="flat")
	search_student_main_logo_frame.grid(row=0, column=0, sticky=W+E)
	search_student_main_search_frame.grid(row=1, column=0, sticky=W+E)
	#search_student_main_text_frame.grid(row=2, column=0, sticky=W+E)
	# Label
	search_student_main_logo_label = Label(search_student_main_logo_frame, text="PATHAKADA NAVODYA M.V", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Verdana", "8","roman"))
	search_student_main_id_label = Label(search_student_main_search_frame, text="Student ID :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	search_student_main_name_label = Label(search_student_main_search_frame, text="Student Name :", padx=5,pady=3, bg='#424242', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
	search_student_main_logo_label.pack()
	search_student_main_id_label.grid(row=0, column=0)
	search_student_main_name_label.grid(row=0, column=2)
	# Entry
	search_student_main_id_entry = Entry(search_student_main_search_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=10)
	search_student_main_name_entry = Entry(search_student_main_search_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=25)
	search_student_main_id_entry.grid(row=0, column=1, padx=5)
	search_student_main_name_entry.grid(row=0, column=3, padx=5)
	# Button
	search_student_main_search_button = Button(search_student_main_search_frame, text="Search Student", command=search_main_details_search, width=15,height=1, relief="flat", font=("Comic", "10"), fg="white", activebackground ="#2c4c66", bg='#212121')
	search_student_main_mark_button = Button(search_student_main_search_frame, text="Student Marks", command=search_main_marks_search, width=15,height=1, relief="flat", font=("Comic", "10"), fg="white", activebackground ="#2c4c66", bg='#212121')
	search_student_main_search_button.grid(row=0, column=4, padx=5,pady=(0,8))
	search_student_main_mark_button.grid(row=0, column=5, padx=5,pady=(0,8))
	# Textbox
	search_student_main_search_text = Text(search_student_main_text_frame, width=96, height=10, bg='#424242', relief='flat', fg='white', state=DISABLED, tabs=1, font=("Time", "10", "bold"))
	search_student_main_search_text.grid(row=0, column=0)

logging_window()
