import math
import os

count = 0
while count < 5:
    os.system('title 2 bilinmeyenli bir denklemin kökünü bulma')
    os.system('color a') # yeşil rengi sağlar
    os.system('powershell write-host -fore Red Iki bilinmeyenli bir denklemin kokunu bulma [Matematik Projesi]')

    print()
    print("ikinci dereceden bir denklemin kokunu bulmak icin asagidaki degerleri girin")
    print()

    a = int(input("A icin bir deger girin : "))
    b = int(input("B icin bir deger girin : "))
    c = int(input("C icin bir deger girin : "))

    diskriminant = (b * b) - (4 * a * c)

    if(diskriminant > 0):
        kok1 = (-b + math.sqrt(diskriminant)) / (2 * a)
        kok2 = (-b - math.sqrt(diskriminant)) / (2 * a)
        print()
        print("2 farkli gercek kok var: kok1 = %.2f and kok2 = %.2f" %(kok1, kok2))
    elif(diskriminant == 0):
        kok1 = kok2 = -b / (2 * a)
        print()
        print("2 esit gercek kok var: kok1 = %.2f and kok2 = %.2f" %(kok1, kok2))
    elif(diskriminant < 0):
        kok1 = kok2 = -b / (2 * a)
        imaginary = math.sqrt(-diskriminant) / (2 * a)
        print()
        print("2 farklı karmasik kok var: kok1 = %.2f+%.2f and kok2 = %.2f-%.2f" %(kok1, imaginary, kok2, imaginary))

    print()
    print("Yeniden yapmak icin rastgele bir tusa basin")
    os.system ('pause > nul') # input("Bir daha yapmak icin rastgele bir tusa basin...")
    os.system('cls' if os.name == 'nt' else 'clear')
