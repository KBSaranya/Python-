#Employee Management System in Python for getting the credentials of the employee and validating it 
#Author : Saranya
#Created Date: 16-Aug-2021

import re
import datetime

def qualify(arg):
    switcher={
        1 :  "BTech Information Technology",2:"BE Computer Science",3:"BE Mechanical",4:   "BE Automobile",5:" BE EEE",6 :  "BE ECE",7 :  "BTech BioMedical",
        8 :  "Others"
    }
    return switcher.get(arg)

def isrepeated(ename):
    for i in range (0,len(ename)-2):
           if ename[i]==ename[i+1] and ename[i+1]==ename[i+2]:
               return True
    return False

def findage(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def validatesalary():
    while True:
        sal=input('Enter your Salary:')
        
        if (not(sal.isdigit())):
            print('Sorry :( ! Salary should be in numeric. Try Again')
            continue
        elif int(sal)==0:
             print('Oh-no! salary should not be null. Retry')
             continue
       
        elif int(sal)<1000 or int(sal) >10000000:
            print("Sorry :( ! Salary range should be between 1000 and 1 crore. Re-attempt")
            continue
        else:
            return sal
            
  
def qualification():
    print("select your qualifiction:")
    print("Option 1 :  BTech Information Technology")
    print("Option 2 :  BE Computer Science")
    print("Option 3 :  BE Mechanical")
    print("Option 4 :  BE Automobile")
    print("Option 5 :  BE EEE")
    print("Option 6 :  BE ECE")
    print("Option 7 :  BTech BioMedical")
    print("Option 8 :  Others")
    qual=int(input("Select one of the options:"))
    while qual<1 or qual>8:
        print("Oops! choose a valid number between 1 and 8. Retry")
        qual=int(input())
    q=qualify(qual)
    if(q=='Others'):
        p=input('Enter your qualification:')
        return p
    else:
        return q
      
def validateemployeeID():
    while True:
        ID=input('Enter your Employee ID:')
        EmpID= 'ACE'+ID
        if (not(ID.isdigit())):
            print('Oops :( ! ID should be in numeric. You got an another chance')
            continue
        elif int(ID)==0:
            print('Oh-no! Employee ID cannot be null. Please enter  valid ID')
            continue
        elif len(ID)!=4:
            print('Oh-no! Employee ID contain must 4 characters. Enter zeroes if it is a single ,double or triple digit number')
            continue
        else:
            return EmpID
            

def validateemployeename():
    while True:
        empname=input("Enter your Name:")
        if (not(empname.isalpha())):
            print('Oops! Name should be in alphabets.Try again')
            continue
        elif len(empname)<=2:
            print('Sorry! The Name you entered is too short. Please enter a valid Name')
            continue            
        elif (not(empname.isalpha())):
           print('Oh no :( ! The Name you entered contains digit. Please enter a valid Name')
           continue
        elif isrepeated(empname):
            print('Sorry! The Name you entered has repeated alphabets. Please enter a valid Name')
            continue
        elif ' ' in empname:
            print('Sorry! The Name you entered has space between first and last name. Please enter without space')
            continue
        else:
            return empname
            

def validatemobileno():
    while True:
         mobno=input('Enter your Mobile Number:')
         
         if (not(mobno.isdigit())):
            print('Oh-no! Mobile number should be in numeric.Give it an another try')
            continue
  
         elif len(mobno)!=10:
             print('Sorry! The Mobile Number you entered is below or above 10 digits. Please enter a valid Number')
             continue
         elif mobno.startswith(('0' , '1' , '2', '3', '4', '5')):
             print('Oops :( ! The Mobile Number you entered cannot start with 0 or 1 or 2 or 3 or 4 or 5. Please enter a valid Number')
             continue
         else:
             return mobno
             
    
def validateemail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
     
        email=input('Enter email:')
        if(re.fullmatch(regex, email)):
            return email
            
        else:
            print("Oops! Enter a valid email ID.Attempt again")
            continue
  
def validatedob():
    try:
        dob1=input('Enter your DOB in the format YYYY-MM-DD:')
        dob= datetime.datetime.strptime(dob1, '%Y-%m-%d')
        age=findage(dob)
        if age<0:
            print("Oh-no! you have entered a future date")
        elif age<18 and age>=0:
            print('You are too young. You have time to come again')
        elif age>60:
            print("Thanks for your Splendid Service.Happy to bid you bye")
        else:
            return age,dob1
    except:
        print("Oh-no! The date entered is invalid. Try again")
        validatedob()


def validatedoj():
    try:
        doj1=input('Enter your DOJ in the format YYYY-MM-DD:')
        doj= datetime.datetime.strptime(doj1, '%Y-%m-%d')
        exp=findage(doj)
        if exp<0:
            print("Oops! you have entered a future date.Retry")
        else:
            return str(exp),doj1
    except:
        print("Sorry! The date entered is invalid. Try again")
        validatedoj()

def printinfo(eid,ename,eno,eemail,edob,edoj,equalify,esalary,eempdob,eempdoj):
    print("\nEMPLOYEE DETAILS\n")
    print('Employee ID      : '+eid)
    print('Employee Name    : '+ename)
    print('Mobile Number    : '+ eno)
    print('Email ID         : '+eemail)
    print('D.O.B            : '+eempdob)
    print("Age              : you are {} years and We are happy to have you here".format(edob))
    print('D.O.J            : '+eempdoj)
    print("Experience       : "+edoj)
    print('Qualification    : '+equalify)
    print("Salary           : Rs."+esalary)



if __name__ == '__main__':
    while True:
        print('\nWelcome to the Employee managament system.\nPlease enter your credentials\n')
        EMPLOYEEID=validateemployeeID()
        EMPLOYEENAME=validateemployeename()
        EMPLOYEENUMBER=validatemobileno()
        EMPLOYEEEMAIL=validateemail()
        EMPLOYEEAGE,EMPDOB=validatedob()
        EMPLOYEEEXP,EMPDOJ=validatedoj()
        EMPLOYEEDOBQUALIFICATION=qualification()
        EMPLOYEESALARY=validatesalary()
        printinfo(EMPLOYEEID,EMPLOYEENAME, EMPLOYEENUMBER,EMPLOYEEEMAIL,EMPLOYEEAGE,EMPLOYEEEXP,EMPLOYEEDOBQUALIFICATION,EMPLOYEESALARY,EMPDOB,EMPDOJ)
        final=input('\nDo you you want to enter another employee record?(Y/N)')
        if final=='Y':
            continue
        else:
            print('\nThank You\n')
            break
        


