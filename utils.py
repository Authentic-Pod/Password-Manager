import encryptors

def newPass(pwd):
    description = input('Please enter a short description of your password: ')
    actualPwd = input('Please input the password: ')
    encryptedPwd = encryptors.encode(actualPwd, pwd)
    print(encryptedPwd)
    data = open("data.txt", 'a+')
    data.write(f'''{description}:{encryptedPwd} \n''')
    data.close()


def fetchPass(pwd):
    description = input('Please input the description of the password you want to fetch: ')
    data = open("data.txt", "a+")
    data.seek(0)
    listOfPwds = data.readlines()
    validDesc = False
    for i in range(len(listOfPwds)):
        details = listOfPwds[i]
        detailsPartitioned = details.partition(':')
        if detailsPartitioned[0] == description:
            validDesc = True
            passwdEncrypted = detailsPartitioned[2]
            passwd = encryptors.decode(passwdEncrypted, pwd)
    
    if validDesc:
        print(f"The password associated with that description is: {passwd}")


