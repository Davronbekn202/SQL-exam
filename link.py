from vazifa import *


def catalog():
    print("""
            0-chiqish
            1-kiritish
            2-oqish
            3-ochirish
            4-ozgartirish
            5-search""")
    while True:
        choice = int(input("Tanlang: "))
        if choice == 0:
            break
        elif choice == 1:
            name = input("Enter title: ")
            print("""
1 - Mechanic
2 - Automat""")
            name = input("Enter id in a screen: ")
            year = int(input("Enter year: "))
            price = int(input("Enter price: "))
            check = input("is that sold False/True: ").title()
            print(f"""\nyou added
title - {name}
year - {year}
price - {price}
check - {check}""")
        elif choice == 2:
            read_cars()
        elif choice == 3:
            ochirish = input("id kiriting: ")
            delete_car(ochirish)
        elif choice == 4:
            ozgar = input("qancha: ")
            ozgar2 = input("id kiriting: ")
            update_price(ozgar, ozgar2)
        elif choice == 5:
            pick_up = input("Enter the title: ")
            search(pick_up)
        else:
            print("hatolik qayta urining")


catalog()
