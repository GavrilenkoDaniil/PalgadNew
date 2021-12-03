from modul import *
inimesed,palgad=spisok()
while True:
	a=input("lisa-1, kastuta-2, suurim palk-3, vähim palk-4, otsing-5: ")
	if a=="1":
		ad()
	elif a=="2":
		kustuta()
	elif a=="3":
		suurim,kellel=suurimpalk(inimesed,palgad)
	elif a=="4":
		vaiksempalk()
	elif a=="5":
		otsi()
	else:
		print("Sisesta number 1-5")