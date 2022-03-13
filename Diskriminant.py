# ikinci dereceden bir denklemin koklerini bulmak icin yapılmıştır
import math
print("ikinci dereceden bir denklemin kokunu bulmak icin asagidaki degerleri girin")
print()

a = int(input("A icin bir deger girin : "))
b = int(input("B icin bir deger girin : "))
c = int(input("C icin bir deger girin : "))

diskriminant = (b * b) - (4 * a * c)
# https://caylakyazilimci.com/post/if-else-ifadeleri-python-101-3
# math.sqrt - sqaure root demek yani karekök
if(diskriminant > 0):
    kok1 = (-b + math.sqrt(diskriminant)) / (2 * a)
    kok2 = (-b - math.sqrt(diskriminant)) / (2 * a)
    print()
    print("Iki farkli gercek kok var: kok1 = %.2f and kok2 = %.2f" %(kok1, kok2))
elif(diskriminant == 0):
    kok1 = kok2 = -b / (2 * a)
    print()
    print("Iki esit gercek kok var: kok1 = %.2f and kok2 = %.2f" %(kok1, kok2))
elif(diskriminant < 0):
    kok1 = kok2 = -b / (2 * a)
    imaginary = math.sqrt(-diskriminant) / (2 * a)
    print()
    print("Iki farklı karmasik kok var: kok1 = %.2f+%.2f and kok2 = %.2f-%.2f" %(kok1, imaginary, kok2, imaginary))
