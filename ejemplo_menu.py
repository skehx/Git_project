menu ="""
Bienvenidos al registro de usuarios, llene los campos que usted prefiera a continuacion selecionando un numero del 1 al 3:
[1] Digitar su Nombre
[2] Digitar su Edad
[3] Dgitiar su Correo electronico

"""


print(menu)
opcion = input('Digite una opcion entre 1 y 3: ')
if opcion =='1':
    nombre= input ('Digita tu nombre: ')
    if nombre.isalpha():
     print('Tu nombre es {}'.format(nombre))
    else:
     print("Has digitado un nombre no valido.. ") 
elif opcion =='2':
    edad=input('Digita tu edad: ')
    if edad.isnumeric():
      print('Tu edad es: {}'.format(edad))
    else:
      print('Has digitado un dato invalido..')
elif opcion =='3':
    email=input('Digita tu email: ')
    if email.find('@')>=0 and email.find('.')>=0:
        print("Tu email es: {}".format(email))
    else:
        print('Has digitado un email no valido.. ')
else: 
    print('Debes digitar un numero entre 1 y 3')
    print('=-=')*20

     
