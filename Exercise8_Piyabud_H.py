usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput == ("admin") and passwordInput == ("abc"):
    print("Login Sucess")
    print("Welcome To Bekery Shop")
    print("################################")
    print("Menu")
    print("################################")
    print("1.Orange Cake","1 piece","60 Bath")
    print("2.Chocolate Cake", "1 piece", "80 Bath")
    print("3.Thai Tea Cake", "1 piece", "50 Bath")
    print("4.Strawberry Short Cake", "1 piece", "70 Bath")
    print("5.Cancle")
    print("################################")
    userSelected = int(input(">>>What would you like to order? (Choose Product Number)<<<"))
    if userSelected == 1:
        orange_cake = int(input("How many pieces of orange cake do you want? : "))
        sum = orange_cake*60
        print("Total_sum",sum)
    elif userSelected == 2:
        choco_cake = int(input("How many pieces of chocolate cake do you want? : "))
        sum = choco_cake*80
        print("Total_sum =", sum)
    elif userSelected == 3:
        thaitea_cake = int(input("How many pieces of thai tea cake do you want? : "))
        sum = thaitea_cake*50
        print("Total_sum =", sum)
    elif userSelected == 4:
        straw_cake = int(input("How many pieces of Strawberry Short cake do you want? : "))
        sum = straw_cake*70
        print("Total_sum =", sum)
    elif userSelected == 5:
        print("See you next time")
        print("################################")
    else:
        print("Try again")
    print (">>>Thx you<<<")
    print("See you next time")
    print("################################")
else:
    print("username or password incorrect")