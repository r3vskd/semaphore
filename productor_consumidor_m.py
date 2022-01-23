# Primero importamos las librerias que vamos a utilizar.
import time
import queue
import random
import logging
import threading
import signal

# matar a la tuberia con ctrl+C, posteriormente se usa la libreria signal para terminar el proceso
####exit_event=threading.Event()

# Creamos una funcion para matar si queremos el proceso de la tuberia.
#def do_this():
#    global dead
#
#    while(not dead):
#        pass
#
#def main():
#    global dead
#    dead=False
# Imprimir en pantalla con la libreria loggin y darle un formato (nombre del hilo y el mensaje a imprimir)
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

# Declaramos la queue o en español: cola, a la cual le asignamos la cantidad de elementos que puede guardar en memoria, en este caso 10.
queue = queue.Queue(maxsize=10)

# Iniciamos una nueva funcion productor que servira para generar un producto de manera aleatoria, almacenarlo y por ultimo comenzara nuevamente
def productor():
    while True:
        if not queue.full():
            item = random.randint(1,10)
            queue.put(item)

            logging.info(f'Genrando nuevo producto: {item}')

            time_to_sleep = random.randint(1, 4)
            time.sleep(time_to_sleep)


# Inniciamos una nueva funcion consumidor que servira para que tome productors uno por uno
def consumidor():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()


            logging.info(f'Producto enviado al consumidor: {item}')



            time_to_sleep = random.randint(1, 4)
            time.sleep(time_to_sleep)


#funcion para matar a la tuberia
def terminate():
    while True:
                kill=input("Si quiere parar el proceso presione enter")
                if kill == '':
                    productor.terminate()
                    consumidor.terminate()
                    print("tuberia muerta")



####            if exit_event.is_set():
####                break

# Los hilos o threads consumidor y productor comienzan a trabajar
if __name__ == '__main__':
    thread_productor = threading.Thread(target=productor)
    thread_consumidor = threading.Thread(target=consumidor)
    thread_terminate = threading.Thread(target=terminate)
    thread_productor.start()
    thread_consumidor.start()
    thread_terminate.start()





# Uso de la libreria para matar a la tuberia con ctrl+C

####def signal_handler(signum, frame):
####    exit_event.set()
####signal.signal(signal.SIGINT, signal_handler)

# para matar el proceso
#input("presione enter para matar el proceso")
#dead=True

# ruta para ejecutar el script C:\Users\Usuario\Documents\utils\USB\1.t\itm\3er semestre\Sistemas Operativos
