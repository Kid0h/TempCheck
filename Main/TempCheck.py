import colorama
from colorama import Fore
from colorama import Style
import time

delay = int(input("Set the delay between each check: "))
Temp = int(input("Set the tempreture which you want to be notified at: "))

f = open("Temps.txt", "a")
f.write('\n|-------------------------|')
f.write('\n'+time.ctime())
f.write('\n|-------------------------|')


while True:
    times = 0
    f = open("Temps.txt", "a")
    tmpFile = open('/sys/class/thermal/thermal_zone0/temp' )
    cpu_temp_raw = tmpFile.read()
    tmpFile.close()
    cpu_temp = round(float(cpu_temp_raw)/1000, 1)
    if cpu_temp >=Temp:
        print(Fore.RED + str( cpu_temp), '--', '(Exceeded)' + Style.RESET_ALL)
        f.write("\n"+time.ctime()+ ' -- '+ str( cpu_temp)+ ' -- (Exceeded)')
    else:
        print(Fore.GREEN + str( cpu_temp) + Style.RESET_ALL)
        f.write("\n"+str(cpu_temp)+" (Normal)")
    f.close()
    time.sleep(delay)