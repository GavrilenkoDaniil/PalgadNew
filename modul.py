def spisok()->str:
	"""Из файла делаем список
	"""
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	return palgad,inimesed

#1
def ad():
	"""Добавление человека и зарплаты в список
	"""
	nimi=input("Siseta nimi: ") #ввод имени
	palk=input("Siseta palgad: ") #ввод зарплаты
	with open("inimesed.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	#добавление имени в файл
	with open("palgad.txt", "a") as palga:
		palga.write(palk+"\n") #добавление зарплаты

#2
def kustuta():
	"""Удаление человека и зарплаты
	"""
	palgad,inimesed=spisok() #Открытие и использование списка
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed: #Проверка человека в списке
		print("Kas sa tahad lisa nimi") #Если отсутствует - предлагаем добавить
		a=input("Y-jah, N-ei")
		if a.upper=="Y":
			ad() #функция добавления человека в список
	else:
		b=inimesed.index(nimi) #поиск индекса человека
		inimesed.pop(a) #удаляем по индексу
		palgad.pop(a) #удаляем по индексу
	f=open("inimesed.txt", "w")
	for c in inimesed:
		f.write(c+"\n")
	f.close()
	d=open("palgad.txt", "w")
	for i in palgad:
		d.write(i+"\n")
	d.close()

#3
def suurimpalk(inimesed:list,palgad:list):
	"""Вычисление самой большой зарплаты
	"""
	p1=[]
	for e in palgad:
		p1.append(int(e)) #Добавляет все из списка в int формате
	suurim=max(p1) #поиск максимальной из p1 списка
	print(suurim)
	b=p1.index(suurim) #приравнивание переменной к индексу
	kellel=inimesed[b] 
	print(kellel)
	return suurim,kellel

#4
def vaiksempalk():
	"""Вычисление самой маленькой зарплаты
	"""
	palgad,inimesed=spisok()#открытие и использование списка
	palgadS=palgad.copy()#скопирует текстовый файл
	palgadS.sort()#Сортирует зарплаты
	a=palgadS[0]
	print(a)
	b=palgad.index(a)#Приравниваем переменную к индексу
	print(inimesed[b])
	

#5
def otsi():
	"""Поиск зарплаты по человеку
	"""
	palgad,inimesed=spisok()#открытие и использование списка
	nimi=input("Siseta nimi: ")#Ввод имени
	j=[]
	for l in inimesed:
		if l==nimi:
			n=inimesed.count(nimi)#находит кол-во с таким именем
			b=0
			for i in range(n):
				k=inimesed.index(nimi,b)
				palk=palgad[k]
				b+=k+1
				j.append(nimi+" "+str(palk))
	print(j)

