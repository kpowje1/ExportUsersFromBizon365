import requests

d1 = list(input('Введите с какого числа делать выборку и по какое в формате месяц-день-день в рамках 1 месяца, к примеру 07-01-31: '))
room = input('Укажите ID комнаты http://joxi.ru/GrqpjdvTRQqKlA, к примеру 85257:mktimursolovyev или 85257:mktimur-solovyev: ')
token = '' #здесь токен с бизона
time1 = input('В какое время был веб, к примеру если в 15:00, то указать 15:00: ')
time = time1.replace(':', '%3A')
room = room.replace(':', '%3A')
m1 = d1[0]+d1[1] #забираем из ввода данные о месяца
d2 = d1[6]+d1[7] #забираем из ввода данные о том, с какого числа делать выгрузку
d1 = d1[3]+d1[4] #забираем из ввода данные о том, по какое число делать выгрузку
d1 = int(d1)
d2 = int(d2)
myall = 0
while d1 <= d2:
        response = requests.get('https://online.bizon365.ru/api/v1/webinars/reports/getviewers?webinarId={room}'
                                '*2021-{m1}-{d2:02}T{time}%3A00&skip=0&limit=1000'.format(m1=m1, d2=d1, room=room, time=time),
                                headers={'x-token': '{token}'.format(token=token)})
        my = response.json()
        file = open("D:\\Users\\users-"+str(m1)+"-"+str(d2)+"-"+"time-"+str(time1)+".csv","a") #путь сохранения файла
        myall = myall + my.get('total')
        for u in my.get('viewers'):
            file.write(u.get('username')+';'+u.get('phone')+';'+u.get('email')+'\n')
            print(u.get('username')+';'+u.get('phone')+';'+u.get('email'))
        file.close()
        mytext = str(my.get('total'))
        # m5 = str(m1)
        # d5 = str(d1)
        d1 += 1
file = open("D:\\Users\\users-"+str(m1)+"-"+str(d2)+"-"+"time-"+str(time1)+".csv","a")
file.write('Всего пользователей было на вебинарах за указанные даты: '+str(myall))
file.close()
print('Всего пользователей было на вебинарах за указанные даты: ' + str(myall))


