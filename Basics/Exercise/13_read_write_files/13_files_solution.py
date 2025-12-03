from collections import Counter
import csv
"""
with open("poem.txt","r") as file:
    content = file.read()
    print(content)
    words = content.split(" ")
    print(words)
    max_counter = 0
    common_word = ""
    for word in words:
        counter = 0
        for word2 in words:
            if word == word2:
                counter +=1
        if counter > max_counter:
            max_counter = counter
            common_word = word
        print(f"{word} : {counter}")
    print(f"The common word1 is: {common_word} with {max_counter} words")

with open("poem.txt","r") as file2:
    content2 = file2.read()
    print(content2)
    words2 = content2.split(" ")
    words2_count = Counter(words2)
    common_word2 = words2_count.most_common(1)[0]
    #max_counter2 = words2_count.most_common(1)[1]

    print(f"The common word2 is: {common_word2}")
"""

#exo
with open("stocks.csv", "r") as file :
    with open("my_output.csv", "w") as output:
        output.write("Company Name,PE Ratio,PB Ratio\n")
        next(file)
        for line in file :
            contents = line.split(",")
            company_name = contents[0]
            price = float(contents[1])
            earning = float(contents[2])
            value = float(contents[3])
            pe_ratio = price / earning
            pb_ratio = price / value
            output.write(f"{company_name},{pe_ratio},{pb_ratio}\n")



