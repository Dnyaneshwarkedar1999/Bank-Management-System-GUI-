acc = list(range(1001,1500))
acc_no=[]
balance=[]
name=[]
sname=[]
a_type=[]
contact=[]
dob=[]
ct=[]
#----------------------------------------------- Creation of account---------------------------------
def create(acc_no):
    nam=input("Enter Your First Name : ")
    name.append(nam)
    surname=input("Enter Your last Name : ")
    sname.append(surname)
    mob=input("Enter Your Mobile Number : ")
    contact.append(mob)
    db=input("Date of Birth DD/MM/YYYY : "  )
    dob.append(db)
    city=input("Enter Your city : ")
    ct.append(city)
    ac_type=input("Account type [C/S] : ")
    if ac_type=='c' or ac_type=='C':
        a_type.append("Current")
    elif ac_type=='s' or ac_type=='S':
        a_type.append("Savings")
    else:
        print("Invalid Account Type choosen")
    money=input("How much do you want To Deposit : " )
    balance.append(money)
    print(f"Your Account Number is : {acc[len(acc_no)]}")
    acc_no.append(acc[len(acc_no)])
    #print(f"Your Account Number is : {acc[len(acc_no)]}")
    
# ---------------------------------------------------Deposit---------------------------------------
def deposit(acc_no):
    n=int(input("please Enter Your Account Number : "))
    if n in acc_no:
        pos=acc_no.index(n)
        old_bal=balance[pos]
        dep=input("How much did you want to Deposit In Your Bank Account : ")
        total=float(old_bal)+float(dep)
        balance[pos]=total
        
        print(f"Your Updated Balance is : {total}")
    else:
        print("Wrong Account Number")


#---------------------------------------Withdrawal -------------------------------------------------        
def withdrawal(acc_no):
    n=int(input("please Enter Your Account Number from which You want to withdraw : "))
    if n in acc_no:
        pos=acc_no.index(n)
        old_bal=balance[pos]
        withdraw=input("How much want to Withdraw From Account : ")
        total=float(old_bal)-float(withdraw)
        balance[pos]=total
        
        print(f"Your Updated Balance is : {total}")
    else:
        print("Wrong Account Number")


# ------------------------------Show Balance-------------------------------------------------------        
def show():
    n=int(input("Enter Account Number : "))
    if n in acc_no:
        pos=acc_no.index(n)
        print(f"\t '{name[pos]} {sname[pos]}' , {a_type[pos]} Account '{acc_no[pos]}' Holds {balance[pos]} INR")
        ch=input("Do you want to see whole Bank Details[y/n]")
        if ch == 'y' or ch=='Y':        
            print(f"\n \t Account Number : {acc_no[pos]}")
            print(f"\t Account Holder Name : {name[pos]} {sname[pos]}")
            print(f"\t Account Type : {a_type[pos]}")
            print(f"\t Balance : {balance[pos]} INR")        
            print(f"\t Contact : {contact[pos]}")
            print(f"\t Account Holder city : {ct[pos]}")
            print(f"\t Date of Birth : {dob[pos]}")
      
    else:
        print("Wrong account Number")


#----------------------------------Simple Interest----------------------------------------------
def simple_Interest():
    n=int(input("Enter Your Account Number : "))
    if n in acc_no:
        ch = input("Would You like check Simple Interest On your Deposit [Y/N]")
        if ch=="y" or ch =="Y":
            pos=acc_no.index(n)
            bal=balance[pos]
            r=6.0
            t=input("Enter Time Period in years : ")
            t=float(t)
            bal=float(bal)
            SI=(bal*r*t)/100
            print(f"You will Get {SI} INR as  Interest on Your Amount \n and after {t} years {SI+bal} INR")
        elif ch=="n" or ch =="N":
            
            bal=input("enter amount for calculating SI : ")
            r=6.0
            t=input("Enter Time Period in years: ")
            t=float(t)
            bal=float(bal)
            SI=(bal*r*float(t))/100
            print(f"You will Get {SI} INR as  Interest on Your Amount \n And after {t} years {SI+bal} INR")
        else:
            pass
    else:
        print("Wrong Account Number")


#---------------------------------------Starting of the code------------------------------------
def intro():
    print("--------MENU---------")
    print("\t 1. Create Account")
    print("\t 2. Display Account Details")
    print("\t 3. Deposit")
    print("\t 4. Withdraw")
    print("\t 5. Check Simple Interest")
    print("\t 6. Exit")
    
    
intro()
ch=''
while(ch!=6):
    ch = input("Enter your Choice from Above List : ")
    if ch=='1':
        create(acc_no)
        print("\n\n")
        
    elif ch=='2':
        show()
        print("\n\n")
    elif ch=='3':
        deposit(acc_no)
        print("\n\n")
    elif ch=='4':
        withdrawal(acc_no)
        print("\n\n")
    elif ch=='5':
        simple_Interest()
        print("\n\n")
    elif ch=='6':
        break
    else:
        print("Wrong Choice Please Enter Correct choice from Above Menu")
        
    again=input("Do you want to continue.......: [y/n]").lower()
    if(again=='y'):
        intro()
    else:
        break


  

# Thank You !   :) :)


        
    