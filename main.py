import requests

d1 = list(input('Введите с какого числа делать выборку и по какое в формате месяц-день-день в рамках 1 месяца, к примеру 07-01-31: '))
#d2 = list(input('Введите по какое число делать выборку в формате месяц-день в рамках 1 месяца, к примеру 07-11: '))
room = input('Укажите ID комнаты http://joxi.ru/GrqpjdvTRQqKlA, к примеру 85257:mktimursolovyev или 85257:mktimur-solovyev: ')
token = '' #здесь токен с бизона
time1 = input('В какое время был веб, к примеру если в 15:00, то указать 15:00: ')
time = time1.replace(':', '%3A')
room = room.replace(':', '%3A')
time1 = list(time1)
time1 = time1[0]+time1[1]
m1 = d1[0]+d1[1]
d2 = d1[6]+d1[7]
d1 = d1[3]+d1[4]
d1 = int(d1)
d2 = int(d2)
myall = 0
while d1 <= d2:
    if d1 < 10:
        response = requests.get('https://online.bizon365.ru/api/v1/webinars/reports/getviewers?webinarId={room}'
                                '*2021-{m1}-0{d2}T{time}%3A00&skip=0&limit=1000'.format(m1=m1, d2=d1, room=room, time=time),
                                headers={'x-token': '{token}'.format(token=token)})

        my = response.json()
        file = open("D:\\Users\\users-"+str(m1)+"-"+str(d2)+"-"+"time-"+str(time1)+".csv","a") #путь сохранения файла
        myall = myall + my.get('total')
        for u in my.get('viewers'):
            file.write(u.get('username')+';'+u.get('phone')+';'+u.get('email')+'\n')
            print(u.get('username')+';'+u.get('phone')+';'+u.get('email'))
        file.close()
        mytext = str(my.get('total'))
        m5 = str(m1)
        d5 = str(d1)
        d1 += 1
    else:
        response = requests.get('https://online.bizon365.ru/api/v1/webinars/reports/getviewers?webinarId={room}'
                                '*2021-{m1}-{d2}T{time}%3A00&skip=0&limit=1000'.format(m1=m1, d2=d1, room=room, time=time),
                                headers={'x-token': '{token}'.format(token=token)})
        my = response.json()
        file = open("D:\\Users\\users-"+str(m1)+"-"+str(d2)+"-"+"time-"+str(time1)+".csv","a") #путь сохранения файла
        myall = myall + my.get('total')
        for u in my.get('viewers'):
            file.write(u.get('username')+';'+u.get('phone')+';'+u.get('email')+'\n')
            print(u.get('username')+';'+u.get('phone')+';'+u.get('email'))
        file.close()
        mytext = str(my.get('total'))
        m5 = str(m1)
        d5 = str(d1)
        print('За 2021-'+ m5 +'-'+ d5 +' было пользователей на вебе:'+ mytext)
        d1 += 1
file = open("D:\\Users\\users-"+str(m1)+"-"+str(d2)+"-"+"time-"+str(time1)+".csv","a")
file.write('Всего пользователей было на вебинарах за указанные даты: '+str(myall))
file.close()
print('Всего пользователей было на вебинарах за указанные даты: ' + str(myall))
