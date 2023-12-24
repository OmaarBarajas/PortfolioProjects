#BMI(IMC)Calculator

measure= input("Please select mesurement style ENG or Metric: ")
if measure == 'Metric':

    height = float(input("Por favor ingresa tu estatura en metros: "))
    weight = int(input("Por favor ingresa tu peso en kilogramos: "))
    BMI =  round(weight/(height**2),2)

    print('Tu IMC es:', BMI)

    if BMI<18.5:
        print('Estas bajo de peso')
    elif BMI<25.0:
        print('Estas en un peso normal')
    elif BMI<30.0:
        print('Estas en sobrepeso ')
    else:
        print('Estas obseso')
else:
    height = float(input("Please insert your height in inches: "))
    weight = int(input("Please insert your weight in pounds: "))
    BMI =  round((weight/(height**2))*703,2)

    print('Your BMI is:', BMI)

    if BMI<18.5:
        print('You are underweight')
    elif BMI<25.0:
        print('You are normal weight')
    elif BMI<30.0:
        print('You are normal overweight')
    else:
        print('You are normal obese')