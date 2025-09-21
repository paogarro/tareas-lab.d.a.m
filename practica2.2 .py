#El gobierno ha establecido un sistema de impuestos progresivos sobre el salario de los
#trabajadores. Como parte de un sistema de nómina en una empresa, debes desarrollar un
#programa que calcule el impuesto a pagar de un empleado según su salario mensual. El
#cálculo del impuesto sigue estas reglas:
#➢ Si el salario es menor o igual a $700.000, no se paga impuesto.
#➢ Si el salario es mayor a $700.000 y menor o igual a $900.000, se paga el 10% del
#salario como impuesto.
#➢ Si el salario es mayor a $900.000, se paga el 20% del salario como impuesto.

salario = float(input("ingrese el salario: "))
porcentaje1 = salario*0.10
porcentaje2 = salario*0.20

if salario <= 700.000:
    print("No se paga impuesto")
elif salario > 700.000 and salario >= 900.000:
    print(f"Se paga el 10 porciento del salario como impuesto, en toltal es: {porcentaje1}%")
elif salario > 900.000:
    print(f"Se paga el 20 porciento del salario como impuesto, en toltal es: {porcentaje2}% ")