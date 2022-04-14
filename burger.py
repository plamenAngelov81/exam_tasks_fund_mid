number_of_towns = int(input())

profit = 0
rain = False

for i in range(1, number_of_towns + 1):
    area = input()
    income = float(input())
    expenses = float(input())
    rain = False

    if i % 5 == 0:
        rain = True

    if rain:
        income = income - income * 0.1
        money = income - expenses
        profit += money

        print(f"In {area} Burger Bus earned {money:.2f} leva.")

    else:
        if i % 3 == 0:
            expenses += expenses * 0.5
            money = income - expenses
            profit += money

            print(f"In {area} Burger Bus earned {money:.2f} leva.")

        else:
            money = income - expenses
            profit += money

            print(f"In {area} Burger Bus earned {money:.2f} leva.")


print(f"Burger Bus total profit: {profit:.2f} leva.")
