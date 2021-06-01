import wmi
import time
import os
import csv
from datetime import datetime

tglf=str(datetime.now().strftime('%Y-%m-%d@%H-%M-%S'))
c = wmi.WMI()
t = wmi.WMI(moniker = "//./root/wmi")
batts1 = c.CIM_Battery(Caption = 'Portable Battery')

header0="""
<!DOCTYPE html>
<html>
<head>
<title>Log Parameter Baterai</title>
<meta http-equiv="refresh" content="2" >
</head>
<body style="background-color:#000000;">
<div style="font-size:15px;color:#F5FFFA;">
"""

tutup0="""
</div>
</body>
</html>
"""


header1="""
<!DOCTYPE html>
<html>
<head>
<title>Monitoring</title>
<meta http-equiv="refresh" content="2" >
<style>
h1 {text-align: center;}
p {text-align: center;}
div {text-align: center;}
</style>
</head>
<body style="background-color:#000000;">
<h1 style="font-size:50px;color:blue;text-alignment=center">Webpage Monitoring Baterai</h1>
<div style="font-size:30px;color:#F8F8FF;">
"""

tutup1="""
</div>
</body>
</html>
"""

def logbat():
    for i, b in enumerate(batts1):
        print('Battery %s Design Capacity: %s mWh' % (i, b.DesignCapacity or 0))

    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        print ('Battery %d Fully Charged Capacity: %d mWh' % (i, b.FullChargedCapacity))

    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    for i, b in enumerate(batts):
        print("Sedang Logging")
      
    onln=str(b.PowerOnline)
    volt=str(b.Voltage/1000)
    kap=str(b.RemainingCapacity/1000)
    a=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    tgl=str(datetime.now().strftime('%Y-%m-%d'))
    jam=str(datetime.now().strftime('%H:%M:%S'))
    f = open("battery_log.html", "a")
    f.write(header0+"Waktu : "+jam+"<br>Charging : "+onln+"<br>Voltage : "+volt+" Volt<br>Sisa power (Wh) : "+kap+"<br><br>"+tutup0)
    f.close
    f = open("battery_log.txt", "a")
    f.write("Log : "+a+"\nCharging : "+onln+"\nTegangan Baterai : "+volt+" Volt \nSisa kapasitas : "+kap+" Wh\n")
    f.close
    f = open("batt_curr_stat.html", "w")
    f.write(header1+"<br>Waktu : "+jam+"<br>Charging : "+onln+"<br>Voltage : "+volt+" Volt<br>Sisa Kapasitas : "+kap+" Wh<br>"+tutup1)
    f.close()
    
    with open(tglf+'.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jam, onln, volt, kap])

def log():
    try:
        while True:
            logbat()
            time.sleep(5)
            
    except KeyboardInterrupt:
        print('Dihentikan')   
        
def main1():
    with open(tglf+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["WAKTU", "STAT-CHG", "VOLTAGE(v)", "CAPACITY-REMAIN(Wh)"])
    if os.path.exists("battery_log.txt"):
        os.remove("battery_log.html")
        os.remove("battery_log.txt")
        log()
    else:
        log()  
        
if __name__ == '__main__':  
    main1()