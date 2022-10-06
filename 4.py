y = int(input("Введите количество лет"))
if y>=4:
    a = int(y/4)
    ex = int(((y-a)*365*8*60/5)+(a*365*8*60/5))
else:
    ex = int((y*365*8*60/5))
print('за', y  , 'лет Вы просмотрите',ex, 'экспонатов')
ex = int(input('сколько экспонатов  просмотрено? - '))
tmin = ex*5
tdn = round(tmin/(8*60))
if (tdn/365) >= 4:
    a = int(tdn/(365*4))
    tlet = round(((tdn - (366*a))/365)+ a)
else:
    tlet = round(tdn/365)
print('На просмотр',ex,'экспонатов вы потратите: ')
print(tmin,'минут')
print(tdn,'дней')
print(tlet,'лет')

