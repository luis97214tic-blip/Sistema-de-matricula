curso = int(input("Curso en que se desea inscribir: "))

def nuevo_curso(cantidad):
    return cantidad > 0

if nuevo_curso(curso):
    print("Cantidad de cursos válida")
else:
    print("Cantidad de cursos no válida")