# Pal-ndromo
Palíndromo es una palabra o frase que se lee igual en un sentido que en otro, ejemplo: ANA, OSO...
mensaje_1 = "===================================="
mensaje = "Ejercicio de palíndromo"
mensaje_2 = "===================================="
print('\033[92m'"\n\t", mensaje_1.center(50, "="),""'\033[0m')
print('\033[92m'"\t", mensaje.center(50, "="),""'\033[0m')
print('\033[92m'"\t", mensaje_2.center(50, "="),"\n"'\033[0m')

print('\n''\033[92m'"\t", "ingresa 10 palabras para ver cual de ellas es palíndromo:",""'\033[0m''\n')
lista = []
for y in range (10):
    string = input('\t'"Ingresa una palabra: ")
    lista.append(string)
#print(lista)
lista_2 = []
for x in lista:
    indice = x[::-1]
    lista_2.append(indice)
#print(lista_2)
if lista[0] == lista_2[0]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[0],'\033[0m')
if lista[1] == lista_2[1]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[1], '\033[0m')
if lista[2] == lista_2[2]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[2], '\033[0m')
if lista[3] == lista_2[3]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[3], '\033[0m')
if lista[4] == lista_2[4]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[4], '\033[0m')
if lista[5] == lista_2[5]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[5], '\033[0m')
if lista[6] == lista_2[6]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[6], '\033[0m')
if lista[7] == lista_2[7]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[7], '\033[0m')
if lista[8] == lista_2[8]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[8], '\033[0m')
if lista[9] == lista_2[9]:
    print('\033[92m'"\t","La palabra palíndromo es: ", lista[9], '\033[0m')    
else:
    print('\n''\033[93m'"\t","no hay más coincidencias", '\033[0m''\n')
