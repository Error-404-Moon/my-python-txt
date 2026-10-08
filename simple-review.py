from operator import itemgetter

main_database = [
    {"id": 1, "name": "mohsen amiri", "balance": 1000000000, "card": "6037708122214321", "sheba": "IR0987654321", "hesab": "77665544332211"},
    {"id": 2, "name": "hosein rezaaei", "balance": 1000000000, "card": "6037691234567890", "sheba": "IR0123466789", "hesab": "11223344556677"}
]

users = [
    {"user": "AmirAkhlagh", "pass": "1234", "card": "603770812221409", "account_no": "77665543457211", "sheba_no": "IR0987654321", "name": "Amir", "last": "Akhlaghdost",'balance':'8000000000'},
    {"user": "Amir", "pass": "1234", "card": "6037998481299222", "account_no": "11223344556677", "sheba_no": "IR0123456789", "name": "Mahfam", "last": "Mohammadi", "balance": '8000000000'}
]

banks = {
    '603799': 'بانک ملی',
    '603770': 'بانک صادرات',
    '603769': 'بانک کشاورزی',
    '589210': 'بانک سپه',
    '610433': 'بانک ملت',
    '628023': 'بانک مسکن',
    '627648': 'بانک توسعه صادرات',
    '627961': 'بانک صنعت و معدن',
    '627353': 'بانک تجارت',
    '589463': 'بانک رفاه',
    '639347': 'بانک پاسارگاد',
    '627412': 'بانک اقتصاد نوین',
    '622106': 'بانک پارسیان',
    '627488': 'بانک کارآفرین',
    '621986': 'بانک سامان',
    '639346': 'بانک سینا',
    '639607': 'بانک سرمایه',
    '502806': 'بانک شهر',
    '502938': 'بانک دی',
    '627381': 'بانک انصار',
    '639599': 'بانک قوامین'
}




def transfer (users, user):
    flag = False
    while flag != True:
        card_number = input('Enter the card number :')
        flag_for_len = False
        flag_for_numbers = False
        first_numbers = card_number[0:6]
        if len(card_number) ==16:
            flag_for_len = True
            
            if  first_numbers  in banks:
                bank = banks[first_numbers]
                flag_for_numbers = True
                flag = True
                print("bank name true")
                break
            else:
                flag_for_numbers = False                    
                print("The card number is false. \n please try agane.")
        if flag_for_len != True:
            print("Your card number too long/too short.\n pleas enter 16 digits.")          
        if flag_for_numbers == True:
               for detas in main_database:
                    if card_number == detas["card"]:
                        print(f"card number is ecceptable. benk name is{bank}, and owner is {detas['name']}")
                        flag = True
                        break
                    elif not flag:
                        print("The card number is not ecceptable.\n please try agane.")
    amount = int(input("Please enter the amount:"))
    if balance(user) < amount:
        print("Your balance id low!")
        return 
    if amount<= 10000000:
        flag_amount = False
        for detas in main_database:
            if card_number == detas["card"]:
                if bank == 'بانک ملی':
                    flag_amount = True
                    user['balance'] = str(int(user['balance'])  - amount ) 
                    user['balance'] = str(int(user['balance'])  - 47)
                    detas["balance"] = str(int(detas["balance"]) + amount)
                    print("The transiton is done!")
                    print(main_database)
                    print(detas)
                    return
                else:
                    flag_amount = True
                    user['balance'] = str(int(user['balance'])  - amount )
                    user['balance'] = str(int(user['balance'])  - 90)
                    detas["balance"] = str(int(detas["balance"]) + amount)
                    print("The transiton is done!")
                    return
            elif not flag_amount:
                print("Error! the final cardnumber not found. Try agane.")
    else:
        print("Your amount is more than 10 milion. \n You have two ways to transfer. \n 1. Using Account number \n 2.Using sheba number.")
        way = input("Wich way? ")
        if way == "1":
            try_acount_nom = 0
            while try_acount_nom < 3 :
                accont_nimber = input("Enter your account nimber : ")
                for detas in main_database:
                    if accont_nimber == detas["hesab"]:
                        user['balance'] = str(int(user['balance'])  - amount )
                        user['balance'] = str(int(user['balance'])  - 25)
                        detas["balance"] = str(int(detas["balance"]) + amount)
                        print("The transiton is done!")
                        return
                    else:
                        print(f"Error! the account number is wrong. {try_acount_nom} times of 3. please try agane.")  
                        try_acount_nom +=1
            if try_acount_nom == 3:
                print(" You're wrong 3 times. You can not try agane. Go to your home. bye")
                exit()
        elif way == "2":
            try_sheba = 0
            while try_sheba < 3 :
                sheba_number = input("Enter your sheba number : ")
                sheba_flag = False
                for detas in main_database:
                    if sheba_number == detas["sheba"]:
                        sheba_flag = True
                        user['balance'] = str(int(user['balance'])  - amount )
                        user['balance'] = str(int(user['balance'])  - 90)
                        detas["balance"] = str(int(detas["balance"]) + amount) 
                        print("The transiton is done!")
                        return
                    elif not sheba_flag:
                        try_sheba +=1
                        print(f"Error! the sheba number is wrong. {try_sheba} times of 3. please try agane.")
            if try_sheba >= 3:
                print(" You're wrong 3 times. You can not try agane. Go to your home. bye")
                exit()
                              
                    
def log_in (users):
    try_times = 0
    while try_times < 3 :
        user_name = input(" Please enter your user name :")
        founded_user = None
        founded_password = None
        for i in users :
            if user_name == i['user']:
                founded_user = i 
                break
        if founded_user == None :
            try_times += 1
            print(f" User name not found. {try_times} times of 3. please try agne")
            if try_times == 3 :
                print(" You're wrong 3 times. you can not try agane. go to your home. bye")
                exit()
        else:
            password_timer = 0
            while password_timer < 3:
                password = input("Enter your password : ")
                if password == founded_user["pass"]:
                    print (f" Welcome dear {founded_user["name"]}.")
                    return founded_user
                else:
                    password_timer += 1
                    print(f" Password is wrong. {password_timer} times of 3. please try agne")
            if password_timer == 3:       
                print(" You're wrong 3 times. You can not try agane. Go to your home. bye")
                exit()    
                
def setting_portal():
    print("Hi! Welcome. First of all lets login")
    login_user = log_in(users)
    while True:
        print("""So... What can i do for you? \n
                          1.Give balanse\n
                          2.Transfer\n
                          3.Exit""")
        functionn = input("Chose the number : ")
        if functionn == "1":
            print(f"Your balance is {login_user['balance']}") 
        if functionn == "2":
            transfer(users, login_user)
        if functionn == "3" :
            print("Have a good day. bye!")
            exit()

setting_portal()