#Solicitar al usuario su edad y, si tiene 18 años o más, imprima un mensaje 
#"¡Podés votar!", y si tiene menos de 18 años, "Lo siento, no podés votar aún."

edad = int(input("Ingrese su edad: "))

if edad >=18:
    print("¡Podés votar!") 
else:
    print("Lo siento, no podés votar aún")