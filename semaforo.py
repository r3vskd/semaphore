#se importa la libreria de threading y time para las pausas
import threading
import time
# esta funcion de semaphore es la que monitorea cuantos threads funcionan al mismo tiempo
semaphore = threading.Semaphore(1)

def f1():

    semaphore.acquire()
    #el sleep es muy importante para poder remarcar el funcionamiento del semaforo al ejecutar
    time.sleep(3)
    print(semaphore)
    print("%s acquired lock." % (threading.current_thread().name))
    print(semaphore._value)
    semaphore.release()
    print("%s released lock." % (threading.current_thread().name))
    print(semaphore._value)
#este es el total de threads existentes en el codigo
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f1)
t3 = threading.Thread(target=f1)
t4 = threading.Thread(target=f1)
t5 = threading.Thread(target=f1)
t6 = threading.Thread(target=f1)
t7 = threading.Thread(target=f1)
t8 = threading.Thread(target=f1)
t9 = threading.Thread(target=f1)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()

print("Main thread exited. ", threading.main_thread())
