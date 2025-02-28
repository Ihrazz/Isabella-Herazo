print("Ingrese cinco calificaciones para calcular el promedio:")

nota1 = 70
nota2 = 60
nota3 = 90
nota4 = 80
nota5 = 85

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f"Promedio: {promedio:.2f}")

if promedio >= 60:
    print("Aprobado")
elif 40 <= promedio < 60:
    print("En recuperación")
else:
    print("Reprobado")