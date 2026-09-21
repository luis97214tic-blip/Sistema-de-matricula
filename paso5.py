curso = int(input("Curso en que se desea inscribir: "))

def nuevo_curso(curso):
    if curso > 0:
        return True
    else:
        return False

if nuevo_curso(curso):
    print("Cantidad de cursos válida")
else:
    print("Cantidad de cursos no válida")