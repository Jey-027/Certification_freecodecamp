'''
una hora de inicio en formato de reloj de 12 horas (terminando en AM o PM)
un tiempo de duración que indique el número de horas y minutos
(opcional) un día de la semana de inicio, sin distinción entre mayúsculas y minúsculas
'''

def add_time(start_time, duration_time, day_week=""):
    # LIsta de dias de la semana
    day_lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Diviendo la variable start_time y la variable duration_time
    x_hour = start_time.find(':')
    x_min = start_time.find(' ')
    y_hour = duration_time.find(':')
    
    # Variables
    hour = int(start_time[:x_hour])             # Extrayendo la hora inicial y casteando a INT
    minute = int(start_time[x_hour+1:x_min])    # Extrayendo los minutos iniciales y casteando a INT
    add_hour = int(duration_time[:y_hour])      # Extrayendo las horas a sumar y casteando a INT
    add_min = int(duration_time[y_hour+1:])     # Extrayendo los minutos a sumar y casteando a INT
    horario = start_time[x_min+1:]              # Extrayendo 
    days = 0                                    # Contador de dias trascurridos
    dia = 0                                     # pocision de dia de la semana trascurrido
    final_hour = ""                             # variable concatenando el resultado
    day_week = day_week.capitalize()            # Transformando el dia de la semana a capitalize
    
    print(horario)
    
    #Valida si la hora es 'AM' o 'PM'
    if horario == 'PM':
        # Transforma las horas en formato 24 hrs si es formato 'PM'
        hour += 12
        # Suma las horas a adicionar
        hour += add_hour
        
        # Si la suma de las horas supera el formato 24 horas 
        if hour > 23:
            while hour > 24:
                hour -= 24
                days += 1
            
            if hour > 12:
                hour -= 12
            else:
                horario = 'AM'
                
        else:
            hour -= 12
            
    elif horario == 'AM':
        hour += add_hour
        
        while hour > 24:
            hour -= 24
            days += 1
        
        if hour > 12:
            hour = hour - 12
            horario = 'PM'
            
    
    # Validamos y sumamos los minutos
    minute += add_min
    if minute > 59:
        minute -= 60
        
        if hour + 1 == 12 and horario == 'AM':
            horario = 'PM'
        elif hour + 1 == 12 and horario == 'PM':
            horario = 'AM'
        
        hour += 1
        
        if hour == 12 and horario == 'AM':
            days += 1

        if minute < 10:
            minute = "0" + str(minute)
    else:
        if minute < 10:
            minute = "0" + str(minute)
        
    # Valida si viene el parametro dia, y si se adicionaron dias entonces calcula el dia que queda 
    for day in range(len(day_lst)):
        if day_lst[day] == day_week:
            dia = day + days
            if dia > 6:
                dia = dia - 7
                while dia >= 7:
                    dia = dia - 7
                
    # Concatena el resultado esperado
    if days == 1:
        if len(day_week) > 0:
            final_hour = str(hour) + ":" + str(minute) + " " + horario + ", " + day_lst[dia] + " (next day)"
        else:
            final_hour = str(hour) + ":" + str(minute) + " " + horario + " (next day)"
            
    elif days > 1:
        if len(day_week) > 0:
            final_hour = str(hour) + ":" + str(minute) + " " + horario + ", " + day_lst[dia] + " ({} days later)".format(days)
        else:
            final_hour = str(hour) + ":" + str(minute) + " " + horario + " ({} days later)".format(days)
            
    else:
        if len(day_week) > 0:
            final_hour = str(hour) + ":" + str(minute) + " " + horario + ", "  + day_week
        else:
            final_hour = str(hour) + ":" + str(minute) + " " + horario 
            
    return final_hour

# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))

# print(add_time("6:30 PM", "205:12"))
# print(add_time("7:30 AM", "205:12", "sunday"))

# print(add_time("11:06 PM", "2:02"))
# print(add_time("8:16 PM", "466:02", "tuesday"))

# print(add_time("11:43 AM", "00:20"))
# print(add_time("11:40 AM", "0:25"))