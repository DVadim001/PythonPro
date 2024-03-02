# Сумма двух чисел (в итоге получается такое, которое ввели)
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict1 = {}
#         for index, i in enumerate(nums):
#             num = target - i
#             if i in dict1:
#                 return [dict1[i], index]
#             else:
#                 dict1[num] = index


# Проверка на палиндром
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # Числа меньше 0 и числа, заканчивающиеся на 0 (кроме 0), не могут быть палиндромами
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
#
#         # Инициализация переменной для хранения перевёрнутой части числа
#         reversed_number = 0
#
#         # Цикл продолжается, пока исходное число больше перпевёрнутой части
#         while x > reversed_number:
#             # Получение последнеё цифры числа
#             digit = x % 10
#             # Добавление цифры к перевёрнутой части, "сдвигая" её на один разряд влево
#             reversed_number = reversed_number * 10 + digit
#             # Удаление последней цифры из исходного числа
#             x = x // 10
#         return x == reversed_number or x == reversed_number // 10
#
# """
# Проверка на палиндром:
# Случай для чисел с чётным количеством цифр: х должно равняться reversed_number
# Случай для чисел с нечётныным количеством цифр: необходимо "отбросить" центральную цифру в reversed_number,
# делением на 10, и сравнить с х
# Возвращается True, если число является палиндромом, и False в противном случае.
# """





