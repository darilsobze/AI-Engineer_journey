
results= ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
num_heads = 0
for result in results:
    if result == "heads":
        num_heads += 1

print(num_heads)

for i in range(1,11):
    print(i ** 2)

expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter your Expense: "))
answer = ""
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        answer = f"U spent {expense} in {i+1}.Month"
    elif expense not in expense_list:
        answer = f"u didn't spend {expense} in a month"
print(answer)

result2 = ""
for i in range(1,6):
    answer2 = input("Are u already tired ? ")
    if answer2 == "Yes":
        result2 = "you didn't finish the race!"
        break
    elif answer2 == "No":
        result2 = "Congratulations! You finished the Race "
        continue

print(result2)

for i in range(5):
    for j in range(i+1):
        print("*",end="")
        if j == i:
            print("\n")