@ECHO OFF && ILOVEMATHEMATICS && color a
cls
color a
powershell write-host -fore Red Iki bilinmeyenli bir denklemin kokunu bulma [Matematik Projesi]
timeout 1 > nul
echo.
goto :DEVAM
:BASLANGIC
Diskriminant.py
:DEVAM
Diskriminant.py
echo. && timeout 3 > nul
echo ###################################################################
echo #           Tarayicinizda kaynagi goruntulemek icin 1,            #
echo #           Yeniden islem yapmak icin 2,                          #
echo #           Cikis yapmak icin herhangi bir tusa basin             #
echo ###################################################################
set /p choice=
if '%choice%'=='1' cls && goto KAYNAK
if '%choice%'=='2' cls && goto BASLANGIC
exit
:KAYNAK
explorer https://tr.wikipedia.org/wiki/Diskriminant 
explorer https://caylakyazilimci.com/post/if-else-ifadeleri-python-101-3
explorer https://www.geeksforgeeks.org/python-math-function-sqrt/
echo ###################################################################
echo # Yeniden islem yapmak için 1, cikis icin rastgele bir tusa basın #
echo ###################################################################
set /p choice=
cls
if '%choice%'=='1' goto BASLANGIC
:CIKIS
exit
