cars = input().split(">>")

total = 0
for car in cars:

    mount = car.split(" ")
    if mount[0] == "family":
        tax = int(mount[2]) // 3000 * 12 + (50 - int(mount[1]) * 5)
        total += tax
        print(f"A family car will pay {tax:.2f} euros in taxes.")

    elif mount[0] == "heavyDuty":
        tax = int(mount[2]) // 9000 * 14 + (80 - int(mount[1]) * 8)
        total += tax
        print(f"A heavyDuty car will pay {tax:.2f} euros in taxes.")

    elif mount[0] == "sports":
        tax = int(mount[2]) // 2000 * 18 + (100 - int(mount[1]) * 9)
        total += tax
        print(f"A sports car will pay {tax:.2f} euros in taxes.")

    else:
        print("Invalid car type.")



print(f"The National Revenue Agency will collect {total:.2f} euros in taxes.")