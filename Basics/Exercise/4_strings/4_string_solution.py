#exo1
street = "Steineckeweg 8"
city = "Darmstadt"
country = "Deutschland"
address = street + " " + city + ", " + country
print(address)
print(f"{street} {city}, {country}")
print(street + "\n" + city + "\n" + country)

#exo2
sentence = "Earth revolves around the sun"
print(sentence[slice(6,14)])
print(sentence[-3:])

#exo3
num_veggies = 10
num_fruits = 12
print(f"I eat {num_veggies} veggies and {num_fruits} fruits daily")

#exo4
print("maine 200 banana khaye".replace("200 banana", "20 samosa"))