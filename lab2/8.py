current_sum=0
current_valuta=0

def balans():
    global current_sum
    global current_valuta
    valuta='tenge'
    if current_valuta==1:
        valuta='dollars'
    print(f'Ваш баланс на данный момент   {current_sum} {valuta}')

def popolnit(x):
    global current_sum
    current_sum+=x

def snyat(x):
    global current_sum
    current_sum-=x

def valuta():
    global current_sum
    global current_valuta
    if current_valuta==0:
        current_sum//=450
        current_valuta=1
    else:
        current_sum*=450
        current_valuta=0
while True:
    balans()
    print('Какую операцию хотите выполнить: 1 пополнить,2 снять,3 поменять валюту,4 закончить сеанс')
    vybor=int(input())
    if vybor==1:
        x=int(input('Сколько вы хотите внести    '))
        popolnit(x)
    elif vybor==2:
        x=int(input('Сколько вы хотите снять    '))
        snyat(x)
    elif vybor==3:
        print('Вы изменили валюту баланса')
        valuta()
    elif vybor==4:
        print('Спасибо что использовали наш банк )')
        exit()
