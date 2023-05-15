def largest_number(num):
    if len(num) == 0:
        return None

    highest_num  = num[ 0 ]

    for number in num:

        if number > highest_num:
            highest_num = number

    return highest_num

nums_list = [12, 2, 3, 32]
highest_num = largest_number(nums_list)
print("The largest number in the is:", highest_num)
