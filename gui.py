from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as m_box
import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='root@123')
cursor=conn.cursor()

try:
	cursor.execute('create database gui')
	cursor.execute('use gui')
	cursor.execute('create table bank (Account_number int primary key,First_name varchar(30), Last_Name varchar(30),DateOfBirth date,Address varchar(50),Pin_code int ,Mobile varchar(10),email varchar(50),Deposit float,Account_Type varchar(20),Gender varchar(10),Security varchar(20))')
except:
	try:
		cursor.execute('use gui')
		cursor.execute('create table bank (Account_number int Primary key,First_name varchar(30), Last_Name varchar(30),DateOfBirth date,Address varchar(50),Pin_code int ,Mobile varchar(10),email varchar(50),Deposit float,Account_Type varchar(20),Gender varchar(10),Security varchar(20))')
	except:
		pass
		
win = Tk()

win.geometry("1366x780")
load = Image.open("k.jpg")
render = ImageTk.PhotoImage(load)
img = Label(win,image=render)
img.place(x=500,y=0, relwidth=1, relheight=1)

load1 = Image.open("b2.jpg")
render1 = ImageTk.PhotoImage(load1)
img1 = Label(win,image=render1)
img1.place(x=-50,y=0)

win.title("DK Bank")


win.configure(bg="pink")


def create():
	
	create_frame = LabelFrame(win,text='Create Account',fg="red",bd=5,height=15,font=("Helvetica", 40, "bold"))
	create_frame.grid(row=5,column=1,pady=2)
	
	l1 = Label(create_frame,text='First Name : ').grid(row=2,column=1)
	l2 = Label(create_frame,text='Last Name : ').grid(row=3,column=1)
	l3 = Label(create_frame,text='Date of Birth : ').grid(row=4,column=1)
	l4 = Label(create_frame,text='Address : ').grid(row=5,column=1)
	l5 = Label(create_frame,text='Pin Code : ').grid(row=6,column=1)
	l6 = Label(create_frame,text='Mobile No : ').grid(row=7,column=1)
	l7 = Label(create_frame,text='Email : ').grid(row=8,column=1)
	l8 = Label(create_frame,text='Deposit : ').grid(row=9,column=1)	
	l10 = Label(create_frame,text='Account Type : ').grid(row=10,column=1)
	l11 = Label(create_frame,text='Gender : ').grid(row=11,column=1)		
	l9 = Label(create_frame,text='Securty : ').grid(row=12,column=1)
	actype = StringVar()
	r1 = Radiobutton(create_frame,text = "Saving",variable=actype,value="SAVING").grid(row=10,column=2,sticky="w")
	r2 = Radiobutton(create_frame,text = "Current",variable=actype,value="CURRENT").grid(row=10,columnspan=3)
	
	gender = StringVar()
	options = ttk.Combobox(create_frame,width=15,textvariable=gender)
	options['values'] = ("Male","Female","Others")
	options.grid(row=11,column=2,sticky="w")
	options.current(0)
	#l=[e1,e2,e3,e4,e5,e6,e7,e8]
	l=[]
	for i in range(8):
		a=StringVar()		
		i1 = Entry(create_frame, width = 40, textvariable=a).grid(row=i+2,column=2)
		l.append(a)
	secure=StringVar()	
	entry = Entry(create_frame, width = 40, textvariable=secure).grid(row=12,column=2)
	def sub():
		try:		
			res=[]
			a=cursor.execute('select Account_number from bank')
			m=cursor.fetchall()
			m=len(m)
			acc = list(range(1000,5001))
			acc_no=acc[m]
			res.append(acc_no)
			for i in range(len(l)):
				res.append(l[i].get())
			try:
				act  = str(actype.get())
				gend = str(gender.get())
				sec = str(secure.get())
			except:
				pass
			res.append(act)
			res.append(gend)
			res.append(sec)
			print(res)
			res=tuple(res)
			query = 'insert into bank (Account_number,First_name , Last_Name ,DateOfBirth ,Address ,Pin_code,Mobile ,email,Deposit,Account_Type,Gender,Security) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
			cursor.execute(query,res)
			conn.commit()
			m_box.showinfo('Successfull',f" Dear Customer Your Account number is {acc_no} . \n Note Down For Future Reference ")
		except:
			m_box.showwarning('Error','Check if You Have Entered Correct Data And try Again.....!!')
		#m_box=showinfo('hey','Your Account Number is',))

	btn = Button(create_frame,text="Submit",command=sub).grid(row=15,column=2,padx=10)
	btn1 = Button(create_frame,text='Exit',command=lambda: create_frame.destroy()).grid(row=15,columnspan=4,padx=10)

#m_box.showwarning('title','create Account...!!')
#---------------------------------------------------------Login Page-------------------------------------

	
def login():
	
	login_frame = LabelFrame(win,text="Login Details",fg='blue',font=("halvatica", 20,"bold"))
	login_frame.grid(row=4,column=1)
	acc = Label(login_frame,text="Account Number : ").grid(row=1,column=0)
	mob = Label(login_frame,text="Password : ").grid(row=2,column=0)
	
	ac_var=IntVar()
	key_a = StringVar()
	
	acc_no = Entry(login_frame,width=30,textvariable=ac_var).grid(row=1,column=1)
	key = Entry(login_frame,width=30,textvariable=key_a).grid(row=2,column=1)	
	
	def validate():
		
		
		global win_login
		try:
			if win_login.state()=='normal':win_login.focus()
			m_box.showwarning('Warning !','First LogOut Current Session Then Try Again')
		except:
			
			win_login=Toplevel(win)
			win_login.geometry("1200x720+10+10")
			win_login.title("Personal Page")
			img = Label(win_login,image=render)
			img.place(x=500,y=0, relwidth=1, relheight=1)
			
			img1 = Label(win,image=render1)
			img1.place(x=-50,y=0)

			acc = ac_var.get()
			pswd = key_a.get()
			pswd = str(pswd)
			
			detail = LabelFrame(win_login,text="Your personal Banking Details Are .!!",bg='orange',font=("halvatica", 30,"bold"))
			detail.grid(row=3,columnspan=3,padx=100,pady=100)
			
			try:
				
				query = 'select * from bank where Account_number=%s'
				val=(acc,)
				cursor.execute(query,val)
				a=cursor.fetchone()
				if(a[11]==pswd):
					print('Successfully Login...')
					data = ["Account Number		-	","First Name		-	","Last Name		-	","Date Of Birth		-	","Address			-	","Pin Code			-	","Mobile number		-	","Email ID			-	","Available Balance (INR)	-	","Account Type		-"	,"Gender			-	"]
					for j in range(len(data)):
						attribute = Label(detail,text=data[j],fg="blue",bg='orange',font=("Times New Roman", 12)).grid(row=j+3,column=0,sticky='w')
					
					
					for i in range(len(a)-1):
						actual_data = Label(detail,text=a[i],fg='red',bg='orange',font=("Times New Roman", 12)).grid(row=i+3,column=1,sticky='w')
#-------------------------------------Deposit--------------------------------------------------------------------------------------------						
					def dep():
						win_login.destroy()
						transaction = Toplevel(win)
						transaction.geometry("1200x600+10+10")
						data = StringVar()
						d1 = Label(transaction,text="How Much Does Customer Wants To Deposit ? ",font=("halvatica", 30,"bold"),fg="blue").pack(pady=100)
						d = Entry(transaction,width=10,textvariable=data).pack()
						
						def Deposit():
							try:
								dat=float(data.get())
								bal=a[8]
								amount=bal+dat
								q3="UPDATE bank set Deposit=%s where Account_number=%s"
								q4=(amount,acc,)
								cursor.execute(q3,q4)
								conn.commit()
								m_box.showinfo("Transaction","Balance Updated",parent=transaction)
								win_login.destroy()
								validate()
								transaction.destroy()
							except:
								m_box.showwarning('Error','only digits.....!!',parent=transaction)						
								print("Failed")						
						s = Button(transaction,text="Submit",command=Deposit).pack()
#----------------------------------------------Withdraw---------------------------------------------------------------------------						
					def wd():
						win_login.destroy()
						transaction = Toplevel(win)
						transaction.geometry("1200x600+10+10")
						data = StringVar()
						d1 = Label(transaction,text="How Much Does Customer Wants To Withdraw ? ",fg='blue',font=("halvatica", 30,"bold")).pack(pady=100)
						d = Entry(transaction,width=10,textvariable=data).pack()
						
						def Deposit():
							try:
								dat=float(data.get())
								bal=a[8]
								amount=bal-dat
								if amount<0:
									m_box.showwarning('Low Balance',"Balance is Too Low for Transaction",parent=transaction)
								else:
									balance = amount	
								q3="UPDATE bank set Deposit=%s where Account_number=%s"
								q4=(balance,acc,)
								cursor.execute(q3,q4)
								conn.commit()
								m_box.showinfo("Transaction","Balance Updated",parent=transaction)
								win_login.destroy()
								validate()
								transaction.destroy()
							except:
								m_box.showwarning('Error','only digits.....!!',parent=transaction)
								print("Failed")						
						s = Button(transaction,text="Submit",command=Deposit).pack()
						
							
						
					btn1 = Button(detail,text='Log Out',command=win.destroy,font=("Times New Roman", 12)).grid(row=len(a)+3,column=3,sticky='w')	
					btn2 = Button(detail,text='Deposit',command=dep,font=("Times New Roman", 12)).grid(row=len(a)+3,column=2,sticky='w')
					btn3 = Button(detail,text='WithDraw',command=wd,font=("Times New Roman", 12)).grid(row=len(a)+3,column=1,sticky='e')
					m_box.showinfo('title','Successfully Login.....!!',parent=win_login)					
				else:
					m_box.showwarning('title','Wrong Password.....!!')
					win_login.destroy()
					login()
					start()

			
			except:
				m_box.showwarning('title','Wrong Data.....!!')
				win_login.destroy()
				login()
				start()
					

	btn = Button(login_frame,text='Login',command=validate,font=("Times New Roman", 12)).grid(row=7,column=1,sticky='e')

	
	

# Main Program Execution--------------------------------------------------------------------------------
def start():
	
	
	
	title = Label(win,text='Welcome To DK Bank...We are Happy To Serve You...!!!',bg="light green",fg="red")
	title.grid(row = 2,columnspan =3,padx=20)
	Label.config(title,font=("Times New Roman", 30,"bold"))


	login_button = Button(win,text='Login',command=login,bg="pink",width=12,height=2,fg="black",font=("halvatica", 30,"bold"))
	login_button.grid(row=4,column=0,padx=5,pady=40)

	create_button = Button(win,text='Create Account',command=create,bg="pink",width=12,height=2,font=("halvatica", 30,"bold"))
	create_button.grid(row=5,column=0,padx=5,pady=40)

	btn1 = Button(win,text='Exit',command=lambda: win.destroy(),bg="pink",width=12,height=2,font=("halvatica", 30,"bold")).grid(row=6,column=0,padx=5,pady=40)
	
	





start()
win.mainloop()

conn.commit()
conn.close()
