print('Hello, Django girls!')

if 3 > 2:
    print('¡Funciona!')

if 1 > 2:
    print('El primer número es mayor que el segundo')
else: 
    print('El primer número no es mayor que el segundo')

name = 'Lucas'
if name == 'Daniela':
    print('¡Hola Daniela!')
elif name == 'Lucas':
    print('¡Hola Lucas!')
else: 
    print('¡Hola anónimo!')

volume = 57
if volume < 20:
    print('Está un poco bajo')
elif 20 <= volume < 40:
    print('Está bien para música de fondo')
elif 40 <= volume < 60:
    print('Perfecto, puedo oír todos los detalles')
elif 60 <= volume < 80:
    print('¡Bueno para fiestas!')
elif 80 <= volume < 100:
    print('Un poco alto')
else:
    print('Está muy alto')

# Cambiar el volumen si está muy alto o muy bajo
volume = 10
if volume < 20 or volume > 80:
    print('¡Eso está mejor!')

def hi():
    print('¡Hola!')
    print('¿Cómo estás?')

hi()

def hi(name):
    if name == 'Daniela':
        print('¡Hola Daniela!')
    elif name == 'Lucas':
        print('¡Hola Lucas!')
    else:
        print('¡Hola anónimo!')
hi('Lucas')

def hi(name):
    print('¡Hola ' + name + '!')
hi('Carlos')

girls = ['Valentina', 'Valeria', 'Camila', 'Laura']
for name in girls:
    hi(name)
    print('Siguiente chica')

for i in range(1, 6):
    print(i)