N = int(input("Digite la cantidad de personas a encuestar: "))

cont_leer_6_9 = 0
cont_tv = 0

for i in range(1, N + 1, 1):
    print(f"\n--- Encuesta Persona {i} ---")

    print("Códigos Tiempo Libre: 1-Menos de 6h, 2-Entre 6 y 9h, 3-Más de 9h")
    tiempo_libre = int(input("Digite el código del tiempo libre: "))

    print("Códigos Actividad: 1-Leer, 2-Ver TV, 3-Hacer deporte, 4-Dormir")
    actividad = int(input("Digite el código de la actividad principal: "))

    if (tiempo_libre == 2 and actividad == 1):
        cont_leer_6_9 = cont_leer_6_9 + 1

    if (actividad == 2):
        cont_tv = cont_tv + 1

porcentaje_tv = (cont_tv / N) * 100

print("\n==============================================")
print("          INFORMACIÓN ESTADÍSTICA             ")
print("==============================================")
print("Personas con 6-9 horas libres que prefieren leer:", cont_leer_6_9)
print("Porcentaje de personas que prefieren ver televisión:", porcentaje_tv, "%")
    
