# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    pass
    tens = 10 ** ndigits
    big_number = number * tens
    if big_number % 1 < 0.5:
        return (big_number // 1) / tens
    else:
        return (big_number // 1 + 1) / tens


print(my_round(2.1234567, 5))


 # Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    pass
    t_list = [int(i) for i in list(str(ticket_number))]
    return sum(t_list[:len(t_list) // 2]) == sum(t_list[-1 * (len(t_list) // 2):])  


print(lucky_ticket(123006))
print(lucky_ticket(123001))
print(lucky_ticket(12321))
print(lucky_ticket(436751))