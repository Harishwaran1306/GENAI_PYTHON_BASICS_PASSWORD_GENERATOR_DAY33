#Password Generator:
print('*'*30)
print('*****PASSWORD GENERATOR*****')
print('*'*30)

import random
import string


#Conditions to create a Random password:

Password_character = (string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

length = int (input('Enter the lenght of the passsword 8 -15:'))

Password  = ''

for i in range(length):
    Password = Password + random.choice(Password_character)
print('The Password is :',Password)


#User's_Password
New_Password = (input('Enter the New Password:'))

if len(New_Password) >= 8 and len(New_Password) <= 15:
    print('Strong Password')
elif len(New_Password) >=6 :
    print('Medium Password')
elif len(New_Password) <= 5:
    print('Weak Password')
else:
    print('Invalid Password')
    
