"""
Se le solicita, crear un programa que permita a una compañía de encuestas, caracterizar a un
grupo de personas, por cada persona el programa debe solicitar el nombre, edad (número entero
mayor a 0) y sexo (Masculino - Femenino), además se le preguntará al usuario que escoja cuál es
su profesión de entre las siguientes (“Ingeniero”,” Abogado”, “Otra”) cada profesión además del
nombre, contempla el sueldo y un atributo que le permita almacenar la cantidad de personas
pertenecientes a esa profesión, la cantidad de personas a encuestar es indeterminada, por ende
al finalizar la captura de datos, debe preguntar si desea continuar con otra persona, en caso de
ingresar que no, usted desplegará por pantalla la cantidad de el porcentaje de ingenieros,
abogados y otra, así mismo el promedio de sueldo por profesión."""
from persona import Persona
from profesional import Profesional

profesionales = []
ingenieros = []
abogados = []
otros = []

def main():
    entrar = 0
    while entrar == 0:
        print("===================")
        print("Encuesta profesionales.")
        print("===================")
        print("1. Ingresar datos.")
        print("2. Revisar datos.")
        print("3. Cerrar programa.")
        op = int(input("Ingrese su opción: "))
        if op == 1:
            nombre = input("Ingrese el nombre: ")
            edad = int(input("Ingrese la edad: "))
            sexo = input("Ingrese el sexo (M/F): ")
            if sexo == "F":
                sexo = "Femenino"
            elif sexo == "M":
                sexo = "Masculino"
            profesion = input("Ingrese profesión (Ingeniero/Abogado/Otro): ")
            sueldo = int(input("Ingrese sueldo: "))
            profesional = Profesional(nombre, edad, sexo, profesion, sueldo)
            profesionales.append(profesional)
            if profesion == "Ingeniero":
                ingenieros.append(profesional)
            elif profesion == "Abogado":
                abogados.append(profesional)
            elif profesion == "Otro":
                otros.append(profesional)
            entrar = 0
        elif op == 2:
            if len(profesionales) == 0:
                print("Primero debe ingresar a una persona.")
                entrar = 0
            else:
                p_abog = None
                p_ing = None
                p_otro = None
                prom_sueldo_a = None
                prom_sueldo_i = None
                prom_sueldo_o = None

                for i in profesionales:
                    i = 0
                    sumatotal = i+1
                    if profesional.get_profesion() == "Ingeniero":
                        p = 0
                        s_ing = p + 1
                        p_ing = s_ing/sumatotal
                    elif profesional.get_profesion() == "Abogado":
                        u = 0
                        s_abog = u + 1
                        p_abog = s_abog/sumatotal
                    elif profesional.get_profesion() == "Otro":
                        q = 0
                        s_otro = q + 1
                        p_otro = s_otro/sumatotal
                for i in abogados:
                    i = 0
                    sumatotal = i+1
                    a = profesional.get_sueldo()
                    inicio_suma = 0
                    sum_sueldo = inicio_suma + a
                    prom_sueldo_a = sum_sueldo/sumatotal
                for i in ingenieros:
                    i = 0
                    sumatotal = i+1
                    a = profesional.get_sueldo()
                    inicio_suma = 0
                    sum_sueldo = inicio_suma + a
                    prom_sueldo_i = sum_sueldo/sumatotal
                for i in otros:
                    i = 0
                    sumatotal = i+1
                    a = profesional.get_sueldo()
                    inicio_suma = 0
                    sum_sueldo = inicio_suma + a
                    prom_sueldo_o = sum_sueldo/sumatotal
                if p_abog == None or prom_sueldo_a == None:
                    print("===================")
                    print("No hay abogados registrados")
                    print("===================")
                else:
                    print("===================")
                    print("Abogados")
                    print("===================")
                    print("Promedio de abogados:",p_abog)
                    print("Sueldo promedio: ",prom_sueldo_a)
                if p_ing == None or prom_sueldo_i == None:
                    print("===================")
                    print("No hay ingenieros registrados")
                    print("===================")
                else:
                    print("===================")
                    print("Ingenieros")
                    print("===================")
                    print("Promedio de ingenieros:",p_ing)
                    print("Sueldo promedio: ",prom_sueldo_i)
                if p_otro == None or prom_sueldo_o == None:
                    print("===================")
                    print("No hay otros profesionales registrados")
                    print("===================")
                else:
                    print("===================")
                    print("Otros")
                    print("===================")
                    print("Promedio de abogados:",p_otro)
                    print("Sueldo promedio: ",prom_sueldo_o)
                entrar = 0   
        elif op == 3:
            print("Hasta luego.")
            entrar = 1

main()
                
                   