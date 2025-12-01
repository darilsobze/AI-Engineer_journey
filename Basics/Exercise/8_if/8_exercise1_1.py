india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("Enter a city name: ")
answer = ""
if city in india :
    result = "India"
elif city in pakistan :
    result = "Pakistan"
elif city in bangladesh :
    result = "Bangladesh"
print(answer)

#exo9
results = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
num_heads = 0
for result in results :
    if result == "heads" :
        num_heads += 1
print(num_heads)

#exo10
for i in range(1,11):
    if i % 2 == 0 :
        print(i)

expense_list = [2340, 2500, 2100, 3100, 2980]
my_expense = int(input("Enter your expense: "))
for i in range(len(expense_list)):
    if my_expense == expense_list[i]:
        print(f"The expense occured in {i}. month")
    else:
        print("You didn't spend",my_expense,"in any month")
