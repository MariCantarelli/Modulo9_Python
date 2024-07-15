height = float(input('What is your height in cm?')) #ALTURA
weight = float(input('What is your weight in kg?')) #PESO

IMC = weight / ((height/100)**2)

if IMC < 18.5:
    print('thinness') 
elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')
elif IMC  >= 25.0 and IMC < 29.9:
    print('overweight')
elif IMC >= 30.0 and IMC < 29.9:
    print('obesity')
else: 
    print('grave of obesity')



