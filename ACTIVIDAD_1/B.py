#realizado por Yovany Ferney Toro Botero
edad = int(input("Por favor ingrese la edad: "))
punt_evaluacion = int(input("Por favor ingrese en un rango de 0 a 100 sus puntos de evaluación: "))
if edad>=18 and edad<=22 and punt_evaluacion < 80:
    print("Usted pasa para el programa de LIGA SEMIPROFESIONAL")
else :
    if edad>=18 and edad<=22 and punt_evaluacion >= 80:
        print("Usted pasa para el programa de LIGA PROFESIONAL DE FUTBOL")
    else :
        print("Usted no aplica para el programa")
