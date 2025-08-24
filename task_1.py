times_string = '1h 45m,360s,25m,30m 120s,2h 60s'
times_list = times_string.replace(',', ' ').split(' ')
minutes_sum = 0

for time in times_list:
    if 'h' in time:
        minutes_sum += int(time.replace('h',''))*60
    elif 's' in time:
        minutes_sum += int(time.replace('s',''))//60
    elif 'm' in time:
        minutes_sum += int(time.replace('m',''))
                          
print(f'Сумма временных значений [{times_string}] составляет {minutes_sum} минут(ы)')