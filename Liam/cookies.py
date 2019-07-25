num_user_cookies = int(input("How many cookies do you have? "))

if num_user_cookies >= 1000:
    num_user_cookies -= 100
elif num_user_cookies >= 10:
    num_user_cookies += 5
else:
    num_user_cookies -= 5

print("Total cookies:", num_user_cookies)
