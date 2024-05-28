from random import randint
import modul_array55
while True:

   N = int(input('Введите размер исходного массива (не больше 15): '))

   if 0 < N <= 15: break

A = [randint(0,100) for i in range(N)]

print('Исходный массив:',A)
print(modul_array55.f(A))

