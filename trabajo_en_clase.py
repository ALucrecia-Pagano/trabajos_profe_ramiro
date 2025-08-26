#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
#	30% de la calificación del examen final.
#	15% de la calificación de un trabajo final.

calificacion_a= float(input("Ingrese la primer calificacion: "))
calificacion_b= float(input("Ingrese la segunda calificacion: "))
calificacion_c= float(input("Ingrese la tercera calificacion: "))

promedio_calificacion= (calificacion_a + calificacion_b + calificacion_c) / 3
examen_final= float(input("Ingrese calificacion del examen final: " ))
trabajo_final= float(input("Ingrese calificacion del trabajo final: "))
calificacion_final= (promedio_calificacion * .55) + (examen_final * .30) + (trabajo_final * .15)
print("La calificacion final es: ", round(calificacion_final, 1))


#Ejercicio 7: Conversión de divisas
#Un programa que lea un monto en dólares y lo convierta a pesos colombianos, argentinos
#  y euros usando tasas de cambio fijas definidas en el código.

peso_colombiano= 4025
peso_argentino= 1359
euro= 0.86

dolares= float(input("Ingrese el monto en dolar que desea covertir: "))

colombiano= peso_colombiano * dolares
argentinos= peso_argentino * dolares
dolar_euro= euro * dolares

print(dolares, "USD equivalen a: ")
print(colombiano, " Pesos Colombianos")
print(argentinos, " Pesos Argentinos")
print(dolar_euro, " Euros")

#Ejercicio 8: Viaje en auto
#Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km y el precio de la gasolina por litro.
#El programa debe calcular:
#cuántos litros se necesitan,
#cuánto costará el viaje,
#y cuántas horas tardará si la velocidad promedio es de 90 km/h.

distancia= float(input("Ingrese distancia en km"))
precio_litro= float(input("Ingrese precio por litro del combustible"))

consumo= 8 / 100
velocidad= 90
litros= consumo * distancia
costo= round(precio_litro * litros, 2)
tiempo = round(distancia / velocidad, 1)

print(f"se necesitan  {litros}  litros de combustible")
print(f"El viaje costara ${costo} ")
print(f"Tardaran {tiempo} horas")

#Ejercicio 9: Préstamo bancario
#Un cliente solicita un préstamo que deberá pagar en 12 meses con interés fijo mensual del 2%.
#El usuario ingresa el monto solicitado, y el programa debe calcular:
#el monto total a devolver,
#el valor de cada cuota mensual.

solicitud= float(input("Ingrese el monto que desea solicitar: "))
interes=0.02
meses=12
total_a_devolver=round(solicitud*(1 + interes)** meses, 2)
valor_cuota= round(total_a_devolver / meses, 2)
print(f""" El total a devolver es de: ${total_a_devolver}
 El valor mensual de la cuota es de: ${valor_cuota}""")