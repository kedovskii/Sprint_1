def digit_root(num):
    temp_d_root = num
    for i in range(len(str(num))): # for поскольку нет while. Максимум len(str(num)) итераций хватит для выхода к одной цифре
        d_root = 0
        for digit in str(temp_d_root):
            d_root += int(digit)
        if d_root < 10:
            return d_root
        temp_d_root = d_root 