# Try - Except - Else - Finally
# 1
name = "Oguzhan"
try:
    print("User name : ", name)
except:
    print(" Variable is not defined ! ")
else:
    print("User is found successfully")
finally:
    print("Program executed successfully ")
print()


# 2
try:
    print(x)
except:
    print("Variable x is not defined ! ")
else:
    print(x * 10)
finally:
    print("Code is executed  ")
print()


# Raising an exception
# 3
total_money = 100
withdraw = input("Çekilecek bakiye miktarını giriniz : ")

try:
    withdraw = int(withdraw)
except ValueError:
    print(" Geçersiz girdi !!! ")
else:
    if withdraw > total_money:
        raise Exception("Çekilebilecek bakiye aşıldı ! ")
    else:
        print("Para çekme işlemi gerçekleştirildi")
        print("Kalan bakiye : ", total_money - withdraw)
finally:
    print(" >> Çıkış yapabilirsiniz ")
