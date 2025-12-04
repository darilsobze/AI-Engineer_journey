letter = ""
while True:
    user_input = input("Enter your input: ")
    try:
        grade_input = int(user_input)
        if 90<=grade_input<=100:
            letter = "A"
        elif 80<=grade_input<=89:
            letter = "B"
        elif 70<=grade_input<=79:
            letter = "C"
        elif 60<=grade_input<=69:
            letter = "D"
        elif 0<=grade_input<=60:
            letter = "F"
        elif 0<grade_input> 100:
            raise ValueError("Invalid Grade")

    except ValueError as v :
        print("ValueError: Your Grade should be a number!")

    if user_input == "exit":
        print("Finished!!")
        break

    print(letter)
