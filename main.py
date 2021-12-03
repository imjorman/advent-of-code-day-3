def power_con_report():
    with open("day-3-input.txt") as file:
        numbers = file.readlines()

    gamma = ""
    epsilon = ""
    for c in range(len(numbers[0]) - 1):
        zeros = 0
        ones = 0
        for reading in range(len(numbers)):
            if numbers[reading][c] == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    power_consumption = int(gamma, 2) * int(epsilon, 2)
    print(f"The power consumption rating is: {power_consumption}.")

def life_support_rating():
    with open("day-3-input.txt") as file:
        numbers = file.readlines()

    bigger_list = numbers
    while len(bigger_list) != 1:
        for c in range(len(numbers[0]) - 1):
            zero_list = []
            one_list = []

            for reading in bigger_list:
                if reading[c] == "0":
                    zero_list.append(reading)
                else:
                    one_list.append(reading)
            if len(zero_list) > len(one_list):
                bigger_list = zero_list
            else:
                bigger_list = one_list

    fewer_list = numbers

    for c in range(len(numbers[0]) - 4):
        zero_list = []
        one_list = []

        for reading in fewer_list:
            if reading[c] == "0":
                zero_list.append(reading)
            else:
                one_list.append(reading)

        if len(zero_list) <= len(one_list):
            fewer_list = zero_list
        else:
            fewer_list = one_list

    co2_scrubber_rating = int(fewer_list[0], 2)
    oxygen_generator_rating = int(bigger_list[0], 2)
    print(f"The life support rating is {oxygen_generator_rating * co2_scrubber_rating}.")


power_con_report()
life_support_rating()
