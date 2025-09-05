def even_numbers(numbers):
    even_list = []
    for a in numbers:
        if a%2 == 0:
            even_list.append(a)
    return even_list

number_list=[3,5,9,2,6,5,8,4,7,6]
result_list=even_numbers(number_list)
print(number_list)
print(result_list)
