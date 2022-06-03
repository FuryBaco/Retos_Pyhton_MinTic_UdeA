edad = float(input("Indicar la edad del paciente:"))
peso = float(input("Indicar el peso del paciente en kilogramos:")) 
desnutricion = 'A' 
sobrepeso = 'B'
estado_max = 'C'     
dieta_a = 101.9  
dieta_b = 31.04
dieta_c = 2.6    
peso_ideal = 0
peso_maximo = 0 
dias = 0
        

if edad < 5 or edad > 17:
        print( "Edad fuera del rango")
else:
        if edad >= 5 and edad <= 10:
            if peso < 16:
                peso_ideal = 22
                dias = ((peso_ideal - peso) / dieta_a)        
                print (f'El estado nutricional del paciente es ', desnutricion, ' y se requieren ', dias, ' días de dieta para que alcance un peso saludable')        
            elif peso > 28:
                peso_ideal = 24
                dias = ((peso - peso_ideal) / dieta_b)
                print ('El estado nutricional del paciente es ', sobrepeso, ' y se requieren ', dias, ' días de dieta para que alcance un peso saludable')
            else:
                peso_maximo = 28
                dias = ((peso_maximo - peso) / dieta_c)
                print (f'El estado nutricional del paciente es ', estado_max, ' y se requieren ', dias, ' días de dieta para que alcance el peso máximo')
        elif edad > 10 and edad <= 13:
            if peso < 30:
                peso_ideal = 32
                dias = ((peso_ideal - peso) / dieta_a) 
                print (f'El estado nutricional del paciente es ', desnutricion, ' y se requieren ', dias, ' días de dieta para que alcance un peso saludable')
            elif peso > 50:
                peso_ideal = 43
                dias = ((peso - peso_ideal) / dieta_b) 
                print (f'El estado nutricional del paciente es ', sobrepeso, ' y se requieren ', dias, ' días de dieta para que alcance un peso saludable')
            else:
                peso_maximo =   50
                dias = ((peso_maximo - peso) / dieta_c)
                print (f'El estado nutricional del paciente es ', estado_max, ' y se requieren ', dias, ' días de dieta para que alcance el peso máximo')
        elif edad > 13 and edad <= 17:
            if peso < 51:
                peso_ideal = 56
                dias = ((peso_ideal - peso) / dieta_a)
                print (f'El estado nutricional del paciente es ', desnutricion, ' y se requieren ', dias, ' días de dieta para que alcance un peso saludable')
            elif peso > 63:
                peso_ideal = 58
                dias = ((peso - peso_ideal) / dieta_b)
                print (f'El estado nutricional del paciente es ', sobrepeso, ' y se requieren ', dias, ' días de dieta para que alcance un peso saludable')
            else:
                peso_maximo = 63
                dias = ((peso_maximo - peso) / dieta_c)
                print (f'El estado nutricional del paciente es ', estado_max, ' y se requieren ', dias, ' días de dieta para que alcance el peso máximo')