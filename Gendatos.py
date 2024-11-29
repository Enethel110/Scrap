import csv

# Datos modificados con algunos registros de dos nombres y otros con uno
datos = [
    [1, "María José", "Lopez", "Hernández", "F", "mlopez@example.com", "Arte"],
    [2, "Carlos", "Gómez", "Ramírez", "M", "cgomez@example.com", "Salud"],
    [3, "Laura Isabel", "Morales", "Díaz", "F", "lmorales@example.com", "Educación"],
    [4, "José Luis", "Fernández", "García", "M", "jfernandez@example.com", "Construcción"],
    [5, "Sofía", "Pérez", "Sánchez", "F", "sperez@example.com", "Finanzas"],
    [6, "Luis Miguel", "Martínez", "Castro", "M", "lmartinez@example.com", "Comercio"],
    [7, "Ana María", "Rodríguez", "Herrera", "F", "arodriguez@example.com", "Arte"],
    [8, "Diego", "Hernández", "Mendoza", "M", "dhernandez@example.com", "Tecnología"],
    [9, "Elena", "Torres", "López", "F", "etorres@example.com", "Salud"],
    [10, "Francisco Javier", "Ramírez", "Reyes", "M", "framirez@example.com", "Educación"],
    [11, "Paula", "Gutiérrez", "Silva", "F", "pgutierrez@example.com", "Construcción"],
    [12, "Andrés", "Vargas", "Campos", "M", "avargas@example.com", "Finanzas"],
    [13, "Isabella", "Ortiz", "Jiménez", "F", "iortiz@example.com", "Comercio"],
    [14, "Ricardo", "Sánchez", "Flores", "M", "rsanchez@example.com", "Arte"],
    [15, "Valeria", "Castillo", "Núñez", "F", "vcastillo@example.com", "Tecnología"],
    [16, "Fernando", "Ruiz", "Rojas", "M", "fruiz@example.com", "Salud"],
    [17, "Lucía", "Cruz", "Espinoza", "F", "lcruz@example.com", "Educación"],
    [18, "Adrián", "Navarro", "Aguilar", "M", "anavarro@example.com", "Construcción"],
    [19, "Daniela", "Bautista", "Pacheco", "F", "dbautista@example.com", "Finanzas"],
    [20, "Miguel Ángel", "Lara", "Luna", "M", "mlara@example.com", "Comercio"],
]

# Escribir datos en un archivo CSV
with open("datos.csv", mode="w", newline="", encoding="latin-1") as archivo:
    escritor = csv.writer(archivo)
    # Encabezados
    escritor.writerow(["ID", "Nombres", "Apellido Paterno", "Apellido Materno", "Sexo", "Email", "Rubro"])
    # Filas
    escritor.writerows(datos)

print("Archivo CSV creado exitosamente como 'datos.csv'")
