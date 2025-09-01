nombre= input("Ingre su nombre completo: ")
edad= input("Edad: ")
promedio= float(input("Ingrese su promedio (entre 0 y 10): "))
ingresos= float(input("Ingresos mensuales:"))

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
