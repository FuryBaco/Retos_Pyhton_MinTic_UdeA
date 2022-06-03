def solucion(edad, peso):
    edad = int(input('Indicar la edad del paciente: '))
    peso = float(input('indicar el peso del paceinte el kilogramos: '))
    estado_nutricional = 'A'
    valor_objetivo = 65
    complemento = 1
    frase = 'un peso saludable'
    if (5 <= edad <= 10) :
        if peso < 16:
            estado_nutricional = 'A'
            valor_objetivo = 22
        elif peso > 28:
            estado_nutricional = 'B'
            valor_objetivo = 24
        else:
            estado_nutricional = 'C'
            valor_objetivo = 28
    elif (10 < edad <= 13) :
        if peso < 30:
            estado_nutricional = 'A'
            valor_objetivo = 32
        elif peso > 50:
            estado_nutricional = 'B'
            valor_objetivo = 43
        else:
            estado_nutricional = 'C'
            valor_objetivo = 50
    elif (13 < edad <= 17) :
        if peso < 51:
            estado_nutricional = 'A'
            valor_objetivo = 56
        elif peso > 63:
            estado_nutricional = 'B'
            valor_objetivo = 58
        else:
            estado_nutricional = 'C'
            valor_objetivo = 63
    if estado_nutricional == 'A':
        complemento = (2*60.1) + (2*(-24.4)) + (1*30.5)
    elif estado_nutricional == 'B':
        complemento = (0.6*60.1) + (4*(-24.4)) + (1*30.5)
    elif estado_nutricional == 'C':
        frase = 'el peso maximo'
        complemento = (0.5*60.1) + (2*(-24.4)) + (0.7*30.5)
    dias_dieta = int((valor_objetivo-peso)/(complemento*0.001)) + ((valor_objetivo-peso)%(complemento*0.001) != 0)
    print ('El estado nutricional del paciente es %s y se requieren %s dias de dieta para que alcance %s' %(estado_nutricional, dias_dieta, frase))
    

solucion(0,0)

    #print ('El estado nutricional del paciente es %s y se requieren %s dias de dieta para que alcance %s' )


