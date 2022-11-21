mas=(input('Введите ваш массив:\n').split())
n=len(mas)
def bubble_sort(mas):
    changed=False
    for run in range(len(mas)-1):
        for i in range(len(mas)-1-run):
            if mas[i]>mas[i+1]:
                changed=True
                mas[i],mas[i+1]=mas[i+1],mas[i]
        if changed==False:
            return mas
    return mas
print(bubble_sort(mas))
