import MySQLdb
 
conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='971012',db='test',charset="utf8") #Connect to mysql database
cursor = conn.cursor() #Get the cursor to query
 
 ##########Create a data table to store user information ###########
sql = '''CREATE TABLE IF NOT EXISTS userinfoes (
         user  VARCHAR(20),
         password  VARCHAR(6),
         age VARCHAR(3),  
         sex VARCHAR(5),
         mobile VARCHAR(11),
         balance FLOAT(12,2))'''
cursor.execute(sql)
sql = '''INSERT INTO userinfoes(user,
         password,age,sex,mobile,balance)
         VALUES ('luu','123456','19','woman','12345678900',10000)'''
cursor.execute(sql)

def login():
         ##########Judge Username##########    
         print ('Please enter your username:')
         k=3 #Record the number of errors
while k:
        global username
        username = raw_input()
        userinfoes = "SELECT * FROM userinfoes WHERE user='%s'"%username 
        #Query whether the user exists
j = cursor.execute(userinfoes) #The number of data that meet the condition
 
if username == (''):
                         print ('user name cannot be empty! ')
elif j == 0:
            k-=1
            if k!=0:
                                 print ('The username is wrong, please re-enter:')
            else:
                print ('You have entered incorrectly three times! ')
                conn.close()
                cursor.close()
                exit()
else:
    #break
        
         ##########Judge Password##########
    print ('Please enter your password:')
k = 3
while k:
        password = raw_input()
userinfoes = "SELECT * FROM userinfoes WHERE user='%s' and password='%s'"%(username,password) #Query whether the entered password matches the user
j = cursor.execute(userinfoes)
        
if password == '':
    print ('password cannot be empty! ')
elif j == 0:
            k-=1
            if k!=0:
                                 print ('The password is wrong, please re-enter:')
            else:
                                 print ('You have typed incorrectly three times! ')
conn.close()
cursor.close()
exit()
#else:
print ('Congratulations, login is successful! ')
#break

def enroll():
         print ('Please enter the username (length<=20):' )
         #Username
while 1:
        username = raw_input()
        userinfoes = "SELECT * FROM userinfoes WHERE user='%s'"%username #Query whether the user exists
        j = cursor.execute(userinfoes) #The number of data that meet this condition
        if j==1:
                         print ('The username already exists, please re-enter! ')
        elif username=='':
                         print ('user name cannot be empty! ')
        else:
            break
        
def judge():
        while(1):
            password = raw_input()
            if len(password)!=6:
                                 print ('length is incorrect, please re-enter:')
            else:
                break
        return password    
                
while 1:
                 print ('Please enter the password (length=6):')
p = judge()
print ('Please confirm the password again:')
q = judge()
if p!=q:
                         print ('The passwords entered twice are not equal, please enter again! ')
else:
#break
    
                        print ('Please enter your age:')
while 1:
        age = raw_input()
        if age=='':
                         print ('age cannot be empty, please re-enter! ')
        elif len(age)>3:
                         print ('Please enter a valid age! ')
        else:
            break
    
print ('Please enter your gender (man/woman):')
while 1:
        sex = raw_input()
        if sex!='man' and sex!='woman':
                         print ('Please enter the correct information! ')
        else:
            break
    
print ('Please enter your phone number:')
while 1:
        mobile = raw_input()
        j=0
        for i in mobile:
            if i<'0' or i>'9':
                j+=1
        if len(mobile)!=11 or j!=0:
                         print ('Please enter valid information! ')
        else:
            break
        
sql = "INSERT INTO userinfoes(user,password,age,sex,mobile,balance)VALUES('%s','%s','%s','%s','%s','%f')" % (username,p,age,sex,mobile,5000.00)
try:
        cursor.execute(sql)
        conn.commit()
        print ('registered successfully, get 5000 yuan balance! ')
        judge1()
        
except:
        conn.rollback()
        conn.close()
cursor.close()
conn.close()
cursor.close()

print("Welcome to FNB Bank ATM")

import datetime

now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
def Home_page_2():
print u'''===================Please enter your options ==================== =
 == 1: Check balance 2: Transfer 3: Withdraw 4: Deposit 5: Return to main menu 6: Exit ==
======================================================='''
##########Submenu##########
def judge2():
    while 1:
        Home_page_2()
        judge_2 = raw_input()
        
 If judge_2=='1':#balance
 Print u'Your balance is: %0.2f'%user_balance(username)
            continue
        
 Elif judge_2=='2': #transfer
 Print u'Please enter the user name of the other party:'
            while 1:
                other_username = raw_input()
 Userinfoes = "SELECT * FROM userinfoes WHERE user='%s'"%other_username #Query whether the user exists
 J = cursor.execute(userinfoes) #The number of data that meet the condition
            
                if other_username == '':
 Print u'Username cannot be empty! '
                elif j==0:
 Print u'The user name does not exist, please enter a valid user name;'
                else:
 Print u'Please enter the transfer amount:'
                    sum = float(raw_input())
                    M_balance = user_balance(username)
                    O_balance = user_balance(other_username)
                    if M_balance-sum >= 0:
                        sq1 = "UPDATE userinfoes SET balance=%0.2f WHERE user='%s'" % (M_balance-sum, username)
                        sq2 = "UPDATE userinfoes SET balance=%0.2f WHERE user='%s'" % (O_balance+sum, other_username)
                        try:
                            cursor.execute(sq1)
                            cursor.execute(sq2)
                            conn.commit()
 Print u'The transfer is successful! '
                        except:
                            conn.rollback()
 Print u'Transfer failed'
                    else:
 Print u'Transfer failed, your balance is insufficient! '
                break   
            continue
                    
 Elif judge_2=='3': #Withdraw money
 Print u'Please enter your withdrawal amount:'
            sum = float(raw_input())
            M_balance = user_balance(username)
            if M_balance-sum >= 0:
                sq1 = "UPDATE userinfoes SET balance='%0.2f' WHERE user='%s'"%(M_balance-sum, username)
                try:
                    cursor.execute(sq1)
                    conn.commit()
 Print u'The withdrawal was successful! '
                except:
                    conn.rollback()
            else:
 Print u'Your balance is insufficient! '
            continue
        
 Elif judge_2=='4': #deposit
 Print u'Please enter your deposit amount (amount<100,000,000.00):'
            sum = raw_input()
            if ',' in sum:
                sum = sum.replace(',','')
            sum = float(sum)
            sq1 = "UPDATE userinfoes SET balance=balance+'%0.2f' WHERE user='%s'"%(sum, username)
            try:
                cursor.execute(sq1)
                conn.commit()
 Print u'The deposit is successful! '
            except:
                conn.rollback()
 Print u'Deposit failed! '
            continue
        
 Elif judge_2=='5': #Return to main menu
            judge1()
            
 Elif judge_2=='6': #quit
 Print u'Thank you for using! '
            conn.close()
            cursor.close()
            exit()
        else:
 Print u'Please enter a valid number!'
            continue
        break
########## Balance###########
def user_balance(h):
    userinfoes = "SELECT * FROM userinfoes WHERE user='%s'"%h
    j = cursor.execute(userinfoes)
    k = cursor.fetchmany(j)
    for i in k:
        return i[5]
judge1() 

restart =('Y')
chances = 3
balance = 67.14

pin = input('Enter ATM Pin: ')
print(pin)
print('Please Press 1 For Your withdrawal\n')
print('Please Press 2 To Make a Deposit\n')
print('option 3 for COMPLAINT\n')
option = int(input('select option\n'))    
if option == 1:
 option1 =input('how much would you like to withdraw\n')
 print('Take your cash\n')
 restart = input('Would You you like to go back? ')
if restart in ('n','NO','no','N'):
 print('Thank You')


elif option ==2:
 Deposit = float(input('How much would you like to deposit?\ \nÂ£10/Â£20/Â£40/Â£60/Â£80/Â£100 for other enter 1:'))
if Deposit in [10, 20, 40, 60, 80, 100]:
 balance = balance + Deposit
print('\nYour Balance is now R',balance)
restart = input('Would You you like to go back? ')
if restart in ('n','NO','no','N'):
 print('Thank You')
       
elif option ==3:
 Complaint = input('What issue would you like to report?:')
 print(Complaint)
print ('Thank you for contacting us')
restart = input('Would You you like to go back? ')
if restart in ('n','NO','no','N'):
 print('Thank You')
