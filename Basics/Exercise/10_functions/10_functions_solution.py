def calculate_area(base, height, shape) :
    area = 0
    if shape == "rectangle":
        area = base * height
    else:
        area = (1/2)* base * height

    return area

def print_pattern(num):
    for i in range(num):
        result = ""
        for j in range(i+1):
            result = result + "*"
        print(result)

def main():
    print_pattern(5)

if __name__ == "__main__":
    main()