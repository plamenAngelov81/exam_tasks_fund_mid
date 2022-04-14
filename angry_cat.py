price_ratings = input().split(", ")
price_ratings_digit = list(map(int, price_ratings))
entry_point = int(input())
type_of_items = input()

left_items = price_ratings[0: entry_point]
left_items_digit = list(map(int, left_items))


right_items = price_ratings[entry_point + 1:]
right_items_digits = list(map(int, right_items))

sum_left = 0
sum_right = 0
if type_of_items == "cheap":
    for i in left_items_digit:
        if i < price_ratings_digit[entry_point]:
            sum_left += i

    for y in right_items_digits:
        if y < price_ratings_digit[entry_point]:
            sum_right += y

elif type_of_items == "expensive":
    for j in left_items_digit:
        if j >= price_ratings_digit[entry_point]:
            sum_left += j

    for k in right_items_digits:
        if k >= price_ratings_digit[entry_point]:
            sum_right += k

if sum_left >= sum_right:
    print(f"Left - {sum_left}")
elif sum_left < sum_right:
    print(f"Right - {sum_right}")
