# exo1
field_length = 92.0
field_width = 48.8
area = field_length * field_width
print("The area of the field is : "+ str(area) + " m²")

#exo2
num_packets = 9
packet_price = 1.49
given_money = 20
change = given_money - (num_packets * packet_price)
print("The change is : "+ str(change) + " $")

#exo3
room_length = 5.5
tile_cost = 500
room_area = room_length * room_length
cost = room_area * tile_cost
print("The cost of the tiles is : "+ str(cost) + " $")

#exo4
num= 17
result = ""
while num > 0:
    rest = num % 2
    result = str(rest) + result
    num = num // 2

print(result)
