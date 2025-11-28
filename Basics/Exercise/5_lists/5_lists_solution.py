monthly_expenses = [2200, 2350, 2600, 2130, 2190]
print(monthly_expenses[1] - monthly_expenses[0])
print(sum(monthly_expenses[:3]))
print(monthly_expenses.__contains__(2000))
monthly_expenses.append(1980)
print(monthly_expenses)
monthly_expenses[3] -= 200
print(monthly_expenses)

heros=['spider man','thor','hulk','iron man','captain america']
print("The length of heros ist : " + str(len(heros)) )
heros.append('black panther')
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3] = ['doctor strange']
print(heros)
heros.sort()
print(heros)


