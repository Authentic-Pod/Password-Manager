import utils
import pwdGenerator

#needs built in encryption key generation
pwd = input('Please enter the correct encryption key: ')
print('Welcome to this password manager! Type "h" for help')
while True:
    cmd = input('> ')
    if cmd == 'h':
        print('''List of commands
        h - Display a list of commands
        f - Fetch an existing password 
        g - Generate a new password
        n - Enter a new password
        q- Quit this program''')
    elif cmd == 'q':
        exit()
    elif cmd == 'n':
        utils.newPass(pwd)
    elif cmd == 'f':
        utils.fetchPass(pwd)
    elif cmd == 'g':
        pwdGenerator.generatePass()
