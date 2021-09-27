import datetime

def add(moment):
	time = datetime.datetime()
	print(time)
	pass

add(datetime.datetime("1999"))

# datetime class
# example = datetime.time(YEAR, MONTH, DAY)
# E podemos aceder a cada um destes conteudos ou a todos
# Para o ano: example.year
# Para o mes: example.month
# Para o dia: example.day
# A data inteira: example
# 
# Formatos para a funcao date da classe datetime
# DAY-NAME - MONTH-NAME - YEAR
# example.strftime("%A, %B %d, %Y") %A = fullname of day %B = fullname of month
# %d = dia do mes %Y = year
# 
# time object 
# example = datetime.time(HOUR, MINUTE, SECOND)
# Para a hora: example.hour
# Para a minute: example.minute
# Para a second: example.second
# A data inteira: example
#
# example_date = datetime.date(2017, 3, 30)
# example_time = datetime.time(22, 27, 0) Horas, minutos e segundos
# example_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
# 
#
#
#
#
#
#