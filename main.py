num = int(input('Введите число от 1 до 999999: '))

s_num = str(num)
data_rub = ['рублей', 'рубль', 'рубля', 'рубля', 'рубля', 'рублей', 'рублей', 'рублей', 'рублей', 'рублей']
data_num_1 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
data_num_2 = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяноста']
data_num_3 = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
data_num_4 = ['тысяч', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч', 'семь тысяч', 'восемь тысяч', 'девять тысяч']
data_num_11_19 = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
out = ''

if num > 10 and num < 20:
    out = data_num_11_19[num % 10] + ' ' + 'рублей'

if len(s_num) == 1:
    out = data_num_1[num] + ' ' + data_rub[num]
elif len(s_num) == 2:
    if num % 10 == 0:
        out = data_num_2[num // 10] + ' ' + data_rub[num % 10]
    else:
        out = data_num_2[num // 10] + ' ' + data_num_1[num % 10] + ' ' + data_rub[num % 10]
elif len(s_num) == 3:
    if (num % 100) > 10 and (num % 100) < 20:
        out = data_num_3[num // 100] + ' ' + data_num_11_19[num % 10] + ' рублей'
    else:
        out = data_num_3[num // 100] + ' ' + data_num_2[(num % 100) // 10] + ' ' + data_num_1[(num % 100) % 10] + ' ' + data_rub[int(s_num[-1])]
elif len(s_num) == 4:
    if (num % 100) > 10 and (num % 100) < 20:
        out = data_num_4[num // 1000] + ' ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_11_19[num % 10] + ' рублей'
    else:
        out = data_num_4[num // 1000] + ' ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_2[(num % 100) // 10] + ' ' + data_num_1[(num % 100) % 10] + ' ' + data_rub[int(s_num[-1])]
elif len(s_num) == 5:
    if (num // 1000) > 10 and (num // 1000) < 20:
        if (num % 100) > 10 and (num % 100) < 20:
            out = data_num_11_19[(num // 1000) % 10] + ' тысяч ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_11_19[num % 10] + ' рублей'
        else:
            out = data_num_11_19[(num // 1000) % 10] + ' тысяч ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_2[(num % 100) // 10] + ' ' + data_num_1[(num % 100) % 10] + ' ' + data_rub[int(s_num[-1])]
    else:
        if (num % 100) > 10 and (num % 100) < 20:
            out = data_num_2[num // 10000] + ' ' + data_num_4[(num // 1000) % 10] + ' ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_11_19[num % 10] + ' рублей'
        else:
            out = data_num_2[num // 10000] + ' ' + data_num_4[(num // 1000) % 10] + ' ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_2[(num % 100) // 10] + ' ' + data_num_1[(num % 100) % 10] + ' ' + data_rub[int(s_num[-1])]
elif len(s_num) == 6:
    if ((num // 1000) % 100) > 10 and ((num // 1000) % 100) < 20:
        if (num % 100) > 10 and (num % 100) < 20:
            out = data_num_3[num // 100000] + ' ' + data_num_11_19[(num // 1000) % 10] + ' тысяч ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_11_19[num % 10] + ' рублей'
        else:
            out = data_num_3[num // 100000] + ' ' + data_num_11_19[(num // 1000) % 10] + ' тысяч ' + data_num_3[(num % 1000) // 100] +  ' ' + data_num_2[(num % 100) // 10] + ' ' + data_num_1[(num % 100) % 10] + ' ' + data_rub[int(s_num[-1])]
    else:
        if (num % 100) > 10 and (num % 100) < 20:
            out = data_num_3[num // 100000] + ' ' + data_num_2[(num // 1000) % 100 % 10] + ' ' + data_num_4[(num // 1000) % 100 % 10] + ' ' + data_num_3[(num % 1000) // 100] + ' ' + data_num_11_19[num % 10] + ' рублей'
        else:
            out = data_num_3[num // 100000] + ' ' + data_num_2[(num // 1000) % 100 // 10] + ' ' + data_num_4[(num // 1000) % 100 % 10] + ' ' + data_num_3[(num % 1000) // 100] +  ' ' + data_num_2[(num % 100) // 10] + ' ' + data_num_1[(num % 100) % 10] + ' ' + data_rub[int(s_num[-1])]

out = out.replace('  ', ' ')
print(out.capitalize())