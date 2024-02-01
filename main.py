import random
import time
newnot = str(input('Good day! Do you already have a login in here?')).strip().lower()
if newnot == 'yes':
    yes = str(input('So please enter your name:')).strip()
    password = str(input('Please enter your password:')).strip()
    time.sleep(3.5)
    print('Is this you?')
    print('Name:', yes)
    print('Password:', password)
    sure = str(input('If not enter here (no):')).strip()
    if sure == 'no':
        print()
if newnot == 'no':
    yesnt = str(input('Welcome outlander! Enter your name here:')).strip()
    npass = str(input('Enter your new password:')).strip()
    npassassu = str(input('Type it again for confirm:')).strip()
    print('Processing...')
    time.sleep(3.5)
    print('name:', yesnt)
    print('Password:', npass)
    sure0 = str(input('Everything is right in here?'))
    # I'm still new to all of this so i don't know how i add a database or make a verification system more efficient