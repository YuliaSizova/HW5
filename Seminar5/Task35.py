# # Семинар 5. Рекурсия и алгоритмы
# # Задача No35. Общее обсуждение
# # Напишите функцию, которая принимает одно число и
# # проверяет, является ли оно простым
# # Напоминание: Простое число - это число, которое
# # имеет 2 делителя: 1 и n(само число)
# # Input: 5
# # Output: yes

n= int(input('Введите число N:'))
for i in range(2,(n//2)+1):
    if n % 1 ==0:
        print('Число составное')
    else:
        print('Число простое')

# number=int(input('Введите число: '))
# import math
# def is_simple(number: int)-> bool:
#     if number % 2==0:
#         return False
#     elif number in [1,2,3]:
#         return True
#     else:
#         for div in range(3,int(math.sqrt(number))+1,2):
#             if number% div:
#                 return False
#     return True

# print(is_simple(number))