person = {
  "nombre": "Juan",
  "apellido": "Perez",
  "edad": 34,
}


nacionalidad = input("Nacionalidad: ")

person["nacionalidad"] = nacionalidad

message = f"El nombre es: {person['nombre']} {person['apellido']}, tiene {person['edad']} años y es de nacionalidad {person['nacionalidad']}"

print(message)