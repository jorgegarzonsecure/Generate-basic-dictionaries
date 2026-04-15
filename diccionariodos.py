from itertools import product

# Palabras base: nombres, apodos, mascotas, animales, diminutivos
bases = [
    # Adultos / apellidos
    "familia", "gonzalez", "samudio", "rodriguez", "emilia",
    "beni", "oro", "beniemilia",
    # Apodos
    "lalo", "pili", "nando",
    # Mascotas comunes
    "firulais", "pelusa", "max", "tison",
    # Nombres de niños y diminutivos
    "juanito", "pedrito", "carlitos", "anita", "luchito", "paulita",
    "nicolas", "camilo", "valen", "vale", "dani", "danielita",
    # Animales típicos
    "perro", "gato", "conejo", "loro", "tigre", "oso", "pollo"
]

# Años en formato de dos dígitos (ej. 70 → 99, 00 → 25)
años_2d = [f"{y:02d}" for y in range(70, 100)] + [f"{y:02d}" for y in range(0, 26)]

# Años completos de 1900 a 2026
años_4d = [str(y) for y in range(1900, 2027)]

# Meses y días en dos dígitos
meses = [f"{m:02d}" for m in range(1, 13)]
dias = [f"{d:02d}" for d in range(1, 32)]

# Símbolos comunes
simbolos = ["!", "*", ".", "_", ",", "-", "+", "/", "\\", "$", "#", "@", "%", "&", "(", ")"]

with open("diccionario_wifi.txt", "w") as f:
    for base in bases:
        # Combinaciones con años de 2 dígitos
        for año, mes, dia, simbolo in product(años_2d, meses, dias, simbolos):
            f.write(f"{base}{año}{mes}{dia}{simbolo}\n")
            f.write(f"{base.capitalize()}{año}{mes}{dia}{simbolo}\n")
            f.write(f"{año}{mes}{dia}{base}{simbolo}\n")
            f.write(f"{año}{mes}{dia}{base.capitalize()}{simbolo}\n")
            f.write(f"{base}{simbolo}{año}{mes}{dia}\n")
            f.write(f"{base.capitalize()}{simbolo}{año}{mes}{dia}\n")

        # Combinaciones con años de 4 dígitos
        for año, mes, dia, simbolo in product(años_4d, meses, dias, simbolos):
            f.write(f"{base}{año}{mes}{dia}{simbolo}\n")
            f.write(f"{base.capitalize()}{año}{mes}{dia}{simbolo}\n")
            f.write(f"{año}{mes}{dia}{base}{simbolo}\n")
            f.write(f"{año}{mes}{dia}{base.capitalize()}{simbolo}\n")
            f.write(f"{base}{simbolo}{año}{mes}{dia}\n")
            f.write(f"{base.capitalize()}{simbolo}{año}{mes}{dia}\n")
