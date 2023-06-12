#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.

def num_system(number, system):
  num = number
  num_sys = ''
  if system == 'hex':
    while num > 0:
      num_ost = str(num % 16)
      if num_ost == '10':
        num_ost = 'a'
      elif num_ost == '11':
        num_ost = 'b'
      elif num_ost == '12':
        num_ost = 'c'
      elif num_ost == '13':
        num_ost = 'd'
      elif num_ost == '14':
        num_ost = 'e'
      elif num_ost == '15':
        num_ost = 'f'
      num_sys += num_ost
      num //= 16
  elif system == 'oct':
    while num > 0:
      num_ost = str(num % 8)
      num_sys += num_ost
      num //= 8
  elif system == 'bin':
    while num > 0:
      num_ost = str(num % 2)
      num_sys += num_ost
      num //= 2

  num_sys = num_sys[::-1]
  return num_sys

number = int(input('Введите число: '))
system = input('Выберите одну из систем bin, oct, hex: ')
if system == 'hex': 
  print(number,' = ', num_system(number, system) ,'; check in hex():', hex(number)[2:])
elif system == 'oct': 
  print(number,' = ', num_system(number, system) ,'; check in oct():', oct(number)[2:])
elif system == 'bin': 
  print(number,' = ', num_system(number, system) ,'; check in bin():', bin(number)[2:])
  
  
