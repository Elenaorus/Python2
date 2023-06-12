#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#Программа должна возвращать сумму и произведение* дробей.
#Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
import math
num1 = input("Введите дробь: ")
num2 = input("Введите дробь: ")


symbol1 = num1.find('/')
symbol2 = num2.find('/')

znam1 = int(num1[:symbol1])
chisl1 = int(num1[symbol1+1:])
znam2 = int(num2[:symbol2])
chisl2 =int(num2[symbol2+1:])

if chisl1 != chisl2:
  nok = math.lcm(chisl1, chisl2)
  delz1 = nok // chisl1
  znam1 *= delz1
  delz2 = nok // chisl2
  znam2 *= delz2
  sumch = nok
 
else:
  sumch = chisl1

sumz = znam1 + znam2
nodsum = math.gcd (sumz, sumch)

if nodsum > 1:
  sumz //= nodsum
  sumch //= nodsum
rez_sum = str(sumz) + '/' + str(sumch)
frsum = Fraction(num1) + Fraction(num2)

print(num1, '+', num2, '=', rez_sum, '; check in Fraction():',  frsum)

prz = znam1 * znam2
prch = chisl1 * chisl2

nodpr = math.gcd (prz, prch)

if nodpr > 1:
  prz //= nodpr
  prch //= nodpr
rez_pr = str(prz) + '/' + str(prch)
frpr = Fraction(num1) * Fraction(num2)

print(num1, '*', num2, '=', rez_pr, '; check in Fraction():',  frpr)



  

