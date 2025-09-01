# Ejercicio 3 — Evaluación de crédito bancario
#Enunciado
#Un banco necesita evaluar créditos personales. El sistema pedirá:
#1.Nombre y apellido.
#2.CUIT (validado).
#3.Ingresos mensuales.
#4.Antigüedad laboral (en años).
#5.Historial crediticio: bueno / regular / malo.
#Condiciones:
#Si historial = malo → rechazo inmediato.
#Si ingresos < $200.000 → rechazo.
#Si ingresos ≥ $200.000 y antigüedad < 2 años → solo puede pedir hasta $500.000.
#Si ingresos ≥ $200.000 y antigüedad ≥ 2 años:
#oHistorial regular → hasta $1.000.000.
#oHistorial bueno → hasta $3.000.000.

nombre= input("Ingrese su nombre y apellido: ")
cuit=  input("Nro de CUIT/CUIL(11 digitos): ")
if not (cuit.isdigit() and len(cuit)== 11):
    print("El cuit no es valido")
    exit()
ingresos= float(input("Ingrese sus ingresos mensuales: $"))
antiguedad= float(input("Ingrese su antiguedad laboral (en años): "))
historial= input("Su historial crediticio es (bueno/ regular/ malo) ").lower()

if historial == "malo" :
    print("Rechazo por mal historial crediticio.")
elif ingresos < 200000 :
    print("Rechazo ingresos insufisientes.")
else:
    if ingresos >= 200000 and antiguedad < 2:
        monto= 500000
    else:
     if historial == "regular":
         monto= 1000000
     elif historial == "bueno" :
         monto = 3000000
     else:
         print("datos ingresados no son correctos")
         exit()

    print(f"{nombre}, el monto aprovado es de: ${monto}")     


#Ejercicio 1 — Sistema de becas estudiantiles
#Enunciado
#La universidad desea automatizar la postulación a becas. El programa debe pedir al usuario:
#1.Nombre y apellido.
#2.Edad (validada).
#3.Promedio general (0–10, validado).
#4.Ingresos familiares mensuales (validado).
#Condiciones:
#Si el promedio es menor a 6 → automáticamente rechazado.
#Si el promedio es 6 o más:
#oSi los ingresos familiares < $300.000 → beca completa.
#oSi los ingresos entre $300.000 y $600.000 → media beca.
#oSi los ingresos > $600.000 → rechazado.
#Ejemplo de salida
#✔ Juan Pérez, 20 años
#Promedio: 8.2
#Ingresos: $250000
#Resultado: Beca completa

nombre= input("Ingre su nombre completo: ")
edad= input("Edad: ")
promedio= float(input("Ingrese su promedio (entre 0 y 10): "))
ingresos= input("Ingresos mensuales:")

if promedio < 6:
    resultado= "Rechazado"
elif ingresos < 300000:
    resultado= "Beca completa"
elif ingresos <= 600000:
    resultado= "Media beca"
else:
    resultado= "Rechazado"
    print(f"""✔ {nombre}, {edad} años
          Promedio: {promedio}
Ingresos: ${ingresos}
Resultado {resultado}""")
