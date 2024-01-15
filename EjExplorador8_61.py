# -*- coding: utf-8 -*-
"""EjExplorador8_61.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10aNup75_QKITqbNm1QJ4WMFK4O50N60q
"""

#Nomina

empleados = int(input("Ingrese la cantidad de empleados: "))
gasto_menor_300 = 0
gasto_mayor_300 = 0

for _ in range(empleados):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    if 100 <= sueldo <= 300:
        gasto_menor_300 += 1
    elif sueldo > 300:
        gasto_mayor_300 += 1

print(f"Empleados que cobran entre $100 y $300: {gasto_menor_300}")
print(f"Empleados que cobran más de $300: {gasto_mayor_300}")
print(f"Gasto total en sueldos: {gasto_menor_300 * 300 + gasto_mayor_300 * 500}")