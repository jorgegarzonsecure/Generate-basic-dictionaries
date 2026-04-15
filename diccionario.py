#nombres = ["familia", "gonzalez", "samudio", "rodriguez", "emilia", "lalo", "pili", "nando", "beni", "oro", "beniemilia"]
nombres = ["familia", "gonzalez", "samudio", "rodriguez", "emilia", "beni", "oro", "beniemilia"]
#nombres = ["familia", "gonzalez", "samudio", "rodriguez", "emilia", "lalo", "pili", "nando", "beni", "oro", "beniemilia", "luis", "jorge", "leidy", "gaby", "julio", "flores", "rosa", "hector", "pablo" ]
apodos = ["lalo", "pili", "nando", "beni", "oro", "beniemilia"]
mascotas = ["firulais", "pelusa", "max", "tison"]
años = [str(y) for y in range(1970, 2026)]
meses = [str(y) for y in range(1, 12)]
dias = [str(y) for y in range(1, 30)]
simbolos = ["!", "*", ".", "_", ",", "-", "+", "/", "\\", "$", "#", "@", "%", "&", "(", ")" ]

with open("diccionario_wifi.txt", "w") as f:
    for nombre in nombres:
        for año in años:
            for simbolo in simbolos:
                for mes in meses:
                    for dia in dias:
                        f.write(nombre + año + simbolo + "\n")
                        f.write(nombre.capitalize() + año + simbolo + "\n")
                        f.write(nombre + simbolo + año + "\n")
                        f.write(nombre.capitalize() + simbolo + año + "\n")
                        f.write(nombre + simbolo + año + simbolo + "\n")
                        f.write(nombre.capitalize() + simbolo + año + simbolo + "\n")
                        f.write(año + nombre + simbolo + "\n")
                        f.write(año + nombre.capitalize() + simbolo + "\n")
                        f.write(año + simbolo + nombre + "\n")
                        f.write(año + simbolo + nombre.capitalize() + "\n")
                        f.write(año + simbolo + nombre + simbolo + "\n")
                        f.write(año + simbolo + nombre.capitalize() + simbolo + "\n")
                        f.write(año + simbolo + nombre + simbolo + año + "\n")
                        f.write(año + simbolo + nombre.capitalize() + simbolo + año + "\n")

                        f.write(nombre + año + simbolo + mes + dia + "\n")
                        f.write(nombre.capitalize() + año + simbolo + mes + dia + "\n")
                        f.write(nombre + simbolo + año + mes + dia + "\n")
                        f.write(nombre.capitalize() + simbolo + año + mes + dia + "\n")
                        f.write(nombre + simbolo + año + simbolo + mes + dia + "\n")
                        f.write(nombre.capitalize() + simbolo + año + simbolo + mes + dia + "\n")
                        f.write(año + nombre + simbolo + mes + dia + "\n")
                        f.write(año + nombre.capitalize() + simbolo + mes + dia +"\n")
                        f.write(año + simbolo + nombre + mes + dia + "\n")
                        f.write(año + simbolo + nombre.capitalize() + mes + dia + "\n")
                        f.write(año + simbolo + nombre + simbolo + mes + dia + "\n")
                        f.write(año + simbolo + nombre.capitalize() + simbolo + mes + dia + "\n")
                        f.write(año + simbolo + nombre + simbolo + año + mes + dia + "\n")
                        f.write(año + simbolo + nombre.capitalize() + simbolo + año + mes + dia +"\n")

                        f.write(nombre + año + simbolo + dia + mes + "\n")
                        f.write(nombre.capitalize() + año + simbolo + dia + mes + "\n")
                        f.write(nombre + simbolo + año + dia + mes + "\n")
                        f.write(nombre.capitalize() + simbolo + año + dia + mes + "\n")
                        f.write(nombre + simbolo + año + simbolo + dia + mes + "\n")
                        f.write(nombre.capitalize() + simbolo + año + simbolo + dia + mes + "\n")
                        f.write(año + nombre + simbolo + dia + mes + "\n")
                        f.write(año + nombre.capitalize() + simbolo + dia + mes +"\n")
                        f.write(año + simbolo + nombre + dia + mes + "\n")
                        f.write(año + simbolo + nombre.capitalize() + dia + mes + "\n")
                        f.write(año + simbolo + nombre + simbolo + dia + mes + "\n")
                        f.write(año + simbolo + nombre.capitalize() + simbolo + dia + mes + "\n")
                        f.write(año + simbolo + nombre + simbolo + año + dia + mes + "\n")
                        f.write(año + simbolo + nombre.capitalize() + simbolo + año + dia + mes +"\n")
                
