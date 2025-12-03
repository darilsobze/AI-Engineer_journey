import numpy as np
import math
populations = {
    "China" : 143,
    "India" : 136,
    "USA" : 32,
    "Pakistan" : 21
}

while True:
    user_input = input("Enter an input: ")
    if user_input == "print":
        for population in populations:
            print(f"{population}==>{populations[population]}")
    if user_input == "add":
        country_input = input("Enter your Country: ")
        if country_input in populations:
            print(f"{country_input} already exists! ")
        else:
            pop_input = input("Enter then his population: ")
            populations[country_input] = pop_input
            #for population in populations:
                #print(f"{population}==>{populations[population]}")
    if user_input == "remove":
        remove_country = input("Which Country to remove? ")
        if remove_country in populations:
            populations.pop(remove_country)
            #for population in populations:
                #print(f"{population}==>{populations[population]}")
        else:
            print(f"That Country {remove_country} didn't exist!")
    if user_input == "query":
        query_country = input("Which Country to query? ")
        if query_country in populations:
            print(f"{query_country} has {populations[query_country]} people")
        else :
            print(f"{query_country} didn't exist yet!")

    if user_input == "exit" :
        print("Finished!!")
        break


#exo2


stocks = {
    "info" : [600,630,620],
    "ril" : [1430,1490,1567],
    "mtl" : [234,180,160]
}


while True :
    user_operation = input("Enter an Operation: ")
    if user_operation == "print":
        for stock in stocks:
            print(f"{stock} ==> {stocks[stock]} ==> avg: {np.average(stocks[stock])}")
        continue

    if user_operation == "add":
        stock_input = input("Enter the Stock: ")
        price_input = int(input("Enter the Price: "))
        if stock_input in stocks:
            stocks[stock_input] += [price_input]
        else :
            stocks[stock_input] = [price_input]

    elif user_operation == "exit":
        print("Finished!!")
        break
    else:
        print("uncorrected Input")

#exo3
def circle_calc(radius):
    area = math.pi * (radius**2)
    return area

def main():
    radius_input = int(input("Enter the radius: "))
    area = circle_calc(radius_input)
    print(f"The area of this circle is : {area}")

if __name__ == "__main__":
    main()