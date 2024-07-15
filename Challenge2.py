yields = int(input('Enter the yield:'))
height = int(input('Enter the height:'))
width = int(input('Enter the width: '))

def calculation_paint():
    area = (height * width) / yields
    return print(f'You need cans {area} of paint.')
    
calculation_paint()
