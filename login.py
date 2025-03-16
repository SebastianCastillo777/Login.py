print("-------REGISTRO-------")
    
while True:
        usuario_registrado=input("Registrar, por favor ingrese su nombre de usuario:    ")
        print("")

        if  usuario_registrado== "" or usuario_registrado.isspace():
             print("El nombre de usuario no debe contener espacios vacios ej.Seba777 ")
             print("")
        elif usuario_registrado.isalpha():
            print("El nombre de usuario  debe contener aun que sea un caracter especial o digito ej.Seba777")
            print("")
        elif usuario_registrado.isdigit():
            print("El nombre de usuario debe contener aunque sea una letra ej.Seba777")
            ("")
        elif len(usuario_registrado) <=6:
            print("El nombre de usuario debe tener igual a 7 o mas caracteres ej.Seba777")
            print("")
        else:
            break





while True:
        contraseña_registrado=input("Contraseña:    ")
        print("")
        if contraseña_registrado== "" or contraseña_registrado.isspace():
            print("La contraseña no debe contener espacios vacios ej.Seba777")
            print("")
        elif contraseña_registrado.isalpha():
            print("La contraseña debe contener aun que sea un caracter especial o digito ej.Seba777")
            print("")
        elif contraseña_registrado.isdigit():
            print("La contraseña debe contener aunque sea un caracteres especial ej.Seba777 ")
            print("")
        elif len(contraseña_registrado) <=6:
            print("La contraseña debe tener igual a 7 o mas caracteres ej.Seba777")
            print("")
        else:
            print("-------USUARIO REGISTRADO-------")
            print("")
            break

while True :
        ("-------INICIAR SESION-------")
        usuario=input("Iniciar sesion, ingrese usuario:     ")
        print("")
        contraseña=input("Contraseña:    ")
        print("")
        
        if usuario != usuario_registrado or contraseña!= contraseña_registrado:
            print("Usuario o contraseña incorrecta, ingrese nuevamente ")
            print("")

        else:
            print("-------INICIANDO SESION-------")
            break
        
        
     









    
    

