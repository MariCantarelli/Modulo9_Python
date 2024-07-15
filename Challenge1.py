input = int(input("What is the temperature of the meat?"))

if(input <= 48):
    print('Rare')

elif(input <= 54 and input > 49):
    print('Medium rare')

elif(input <= 60 and input > 55):
    print('Medium')

elif(input <= 65 and input > 61):
    print('Medium well')

elif(input > 71):
    print('Well done')

else:
    print('Write again with numbers')