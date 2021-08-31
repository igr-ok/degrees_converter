


print("Что переводим?: дес.градусы в гр.мин.сек жми 1,\nгр.мин.сек. в дес.град. жми 0")
vibor = input()




if vibor == "0":
    print('Сколько градусов?: ')
    gradusov = input()
    minut = input('Сколько минут?: ')
    sekund = input('Сколько секуд?Если есть дробные, через точку : ')
    desResult = (int(minut) / 60) + (float(sekund) / 3600)
    finalRes = int(gradusov) + desResult

    print ('Результат перевода в десятичные градусы =  ' + str(finalRes) + "град")

elif vibor == "1":
    celihGrad = input('Сколько целых градусов?: ')
    doleiGrad = input('Сколько долей градуса? Ввод начинайте с 0.итд : ')
    resultGr = (float(doleiGrad) * 60) 
    resultMi = int(resultGr)
    resultSe = (float(resultGr) - int(resultGr)) * 60

    print ('Результат перевода в гр.мин.сек. =  '+ celihGrad + "град" + str(resultMi) + "мин" + str(resultSe) + "сек")



input()
