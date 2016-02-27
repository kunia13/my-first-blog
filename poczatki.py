print('Hello, Django girls!')
if 3>2:
    print('To dziala!')
if 5>2:
     print('5 jest jednak większe od 2')
else:
     print('5 nie jest większe od 2')
name='Miska'
if name=='Ola':
    print('Hej Ola')
elif name=='Miska':
    print('Hej Miska')
else:
    print('Hej nieznajoma!')
volume = 57
if volume < 20:
    print("Prawie nic nie slychac.")
elif 20 <= volume < 40:
    print("O, muzyka leci w tle.")
elif 40 <= volume < 60:
    print("Idealnie, moge uslyszec wszystkie detale")
elif 60 <= volume < 80:
    print("Dobre na imprezy")
elif 80 <= volume < 100:
    print("Troszeczke za glosno!")
else:
    print("Ojoj! Moje uszy! :(")
def hej():
    print('Hej!')
    print('Jak się masz?')
hej()
def hej(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Miska':
        print('Hej Miska!')
    else:
        print('Hej nieznajoma!')

hej("Aga")
def hej(imie):
    print('Hej ' + imie + '!')

hej("Rachel")
dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for imie in dziewczyny:
    hej(imie)
    print('Kolejna dziewczyna')
for i in range(1, 6):
    print(i)

SHORT_FUR = 'krotkie'
LONG_FUR = 'dlugie'
class Cat(object):
    def __init__(self, fur_length):
            self.fur_len = fur_length
    def meow(self, count):
            for i in range(count):
                print('meow', 'my fur length is', self.fur_len)

kitty = Cat(SHORT_FUR)
print(kitty.fur_len)
kitty.meow(1)

kitty2 = Cat(LONG_FUR)
print(kitty2.fur_len)
kitty2.meow(3)
