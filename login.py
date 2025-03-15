while True:
    
    usuario_registrado=input("Registrar, por favor ingrese su nombre de usuario:    ")
    print("")
    contraseña_registrado=input("Contraseña:    ")

    if  usuario_registrado== "" or usuario_registrado.isspace():
        print("El nombre de usuario no debe contener espacios vacios ej.Seba777 ")
        print("")
    elif contraseña_registrado== "" or contraseña_registrado.isspace():
      print("La contraseña no debe contener espacios vacios ej.Seba777")
      print("")
    elif usuario_registrado.isalpha():
        print("El nombre de usuario  debe contener aun que sea un caracter especial o digito ej.Seba777")
        print("")
    elif contraseña_registrado.isalpha():
        print("La contraseña debe contener aun que sea un caracter especial o digito ej.Seba777")
        print("")
    elif usuario_registrado.isdigit():
        print("El nombre de usuario debe contener aunque sea una letra ej.Seba777")
        print("")
    elif contraseña_registrado.isdigit():
        print("La contraseña debe contener aunque sea un caracteres especial ej.Seba777 ")
        print("")
    elif len(usuario_registrado) <=6:
        print("El nombre de usuario debe tener igual a 7 o mas caracteres ej.Seba777")
        print("")
    elif len(contraseña_registrado) <=6:
        print("La contraseña debe tener igual a 7 o mas caracteres ej.Seba777")
        print("")
    
    else:
       print("Usuario registrado exitosamente!")
       break


print("")
usuario=input("Iniciar sesion, ingrese usuario:     ")
print("")
contraseña=input("Contraseña:    ")
print("")

while True :
    if usuario != usuario_registrado or contraseña!= contraseña_registrado:
        print("Usuario o contraseña incorrecta, ingrese nuevamente ")
        print("")
        usuario=input("Ingrese usuario:     ")
        print("")
        contraseña=input("Ingrese contraseña:    ")
    else:
        print("Iniciando sesion!")
        break
     









    
    

