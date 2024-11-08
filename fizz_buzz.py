def counting_sheep(number_int, mult, tracker):

    to_check = number_int * mult
    to_check = str(to_check)

    for char in to_check:
        if char not in tracker:
            tracker.append(char)

    if len(tracker) == 10:
        return to_check
    
    return counting_sheep(number_int, mult + 1, tracker)


def Beatrix(number):
    desired_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    digits = []
    mult = 0
    for i in range(20):
        mult += 1
        print('N * ', mult, ' = ', number*mult)
        for digit in list(str(number * mult)):
            if int(digit) not in digits:
                digits.append(int(digit))
        print(digits)
        digits.sort()
        if digits == desired_digits:
            break
        else:
            print("INSOMNIA ??")

with open('result.txt', 'w') as fr:
    with open('A-large-practice.in', 'r') as f:
        for line in f.readlines():
            number_int = int(line.replace('\n', '').strip())

            if number_int == 0:
                fr.write(str('INSOMNIA'))

            print(number_int)
            Beatrix(number_int)

# f = open()
# f.close()


def FizzBuzz(nbr):
    if nbr%3 and nbr%5:
        return 'FizzBuzz'
    elif nbr%3:
        return 'Fizz'
    elif nbr%5:
        return 'Buzz'
    return nbr

# def sort_custom(list_number):
#     list_number_sorted = []

#     for elm in list_number:
#         is_inserted = False
#         print(list_number_sorted)
#         for idx, item in enumerate(list_number_sorted):
#             if elm < item:
#                 list_number_sorted.insert(idx, elm)
#                 is_inserted = True
#                 break
        
#         if not is_inserted:
#             list_number_sorted.append(elm)
#             print(list_number_sorted)

#     return list_number_sorted

# fibonacci_cache = {0: 0, 1: 1}

# def fibo(n):
#     if n not in fibonacci_cache:
#         fibonacci_cache[n] = fibo(n-1) + fibo(n-2)
#     return fibonacci_cache[n]

# def fibo(n, results=None):

#     if not results:
#         results = {}
    
#     if results.get(n): # renvoie result[n] et None si ce dernier n'existe pas
#         return results[n]
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         fibo_calc = fibo(n-1, results) + fibo(n-2, results)
#         results[n] = fibo_calc
#         return fibo_calc 
    
#def main() -> str:

    # 1, 1, 2, 3, 5, 8, 13, 21...
    # print(fibo(34))

    # list_number = [33, 6, 9, 12, 90, 34, 56]
    
    #print(sort_custom(list_number))
    
    # list_number.sort()
    # list_number = [{"value" : 33}, {"value": 6}, {"value":9}]

    # list_number.sort(key=lambda x: x["value"])

    # res = filter(lambda x: x < 12, list_number)

    # print(list(res))

    # result = []
    # for elm in list_number:
    #     if elm < 12:
    #         result.append(elm)
    
    # print(result)

    # for elm in list_number:
    #     print(FizzBuzz(elm))

    # try:
    #     n: int = int(input())
    # except ValueError as error:
    #     print('Enter a digit')
    #     #raise ValueError('Enter a digit') 

    # print(type(n))
    # result = FizzBuzz(n)
    # print(result)

# if __name__ == '__main__':
#     main()


