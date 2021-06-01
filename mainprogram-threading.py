from threading import Thread
import subprocess
import time
import socket

IP=socket.gethostbyname(socket.gethostname())
PORT = 8800
print("HTTP Server berjalan pada http://{}:{}".format(IP,PORT))
print("Masukkan /sekarang untuk monitoring baterai")
print("Masukkan /log untuk membuka log baterai")
    
try :
    t1 = Thread(target=subprocess.run, args=(["python", "l1infobatt.py"],))
    t2 = Thread(target=subprocess.run, args=(["python", "l2simplehttpserv.py"],))
    t3 = Thread(target=subprocess.run, args=(["python", "l3cbtele2.py"],))

    t1.start()
    time.sleep(3) #delay menunggu file log
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
      
except KeyboardInterrupt:
    print("Semua thread dihentikan, harap tunggu")
    time.sleep(3)
    exit()