from datetime import date, datetime

date_now = date.today()

print(f'{date_now.year}{date_now.month}')

str_data = '1998-11-23'

date_nova = datetime.strptime(str_data, '%Y-%m-%d').date()
print(type(date_nova))

print(date_nova.strftime('%Y%m'))

# from datetime import date
#
# date_now = date.today().strftime('%Y%m')
#
# print(date_now)