##Servidor
from tkinter import *
import threading
import IP
import socket
import time
import math
import sys
import os

tk = Tk()


canvas = Canvas (tk, width=700, height=400, bd=0, highlightthickness=0)
canvas.pack()

### Funcion para calcular la posicion del cubo
def polarec(m,a,x,y):
    x1 = m*math.cos(math.radians(a)) + x
    y1 = m*math.sin(math.radians(a)) + y
    return (x1,y1,x,y)
### Extraer la IP 
hots_ip = (socket.gethostbyname(socket.gethostname()))

l = ["inicio"]
### Implemetacion del Socket
class Servidor():
    def __init__(self, host = hots_ip, port=8181):
        ### Crear el socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ### Generar la conexion IP/PORT
        self.sock.bind((str(host), int(port)))
        ### Cantidad de usuarios permitidos
        ### para la conexion
        self.sock.listen(40)
        ### Threadin para ejecutar el conexion
        hilo3 = threading.Thread(target=self.ace_conx)
        
        hilo3.start()
            
    def ace_conx(self):
        ### Aceptar conexion de un usuario
        self.conn, self.addr = self.sock.accept()
        print("IP,PUERTO:",self.addr) 
        while True:
            try:
                ### Recibir datos desde el ususario
                datos = self.conn.recv(20).decode()
                mensaje = datos
                print(datos)
                ### Guardar datos recibidos en la lista L
                l.insert(0,mensaje)
                ### Fichero para almacenar los datos entrantes   
                file_app = open("C:/Users/JHONATAN CALDERON/Desktop/PROYECTOS PYTHON/Parcial Corte I/DATABASE.txt", "a")
                file_app.write(mensaje + "//")
                file_app.close()
         
            except:
               pass
### Clase que permite crear el cubo 
class Cubo():
    def __init__ (self,m,a,x,y):
        
        self.l =list()
        self.lm = list()
        self.m,self.a,self.x,self.y = m,a,x,y

      
    ### Crear el cubo
    def dibujar(self):
        for i in range(3):
            self.l.append(canvas.create_line(polarec(self.m,self.a+120*i,self.x,self.y)))
            self.lm.append(polarec(self.m,self.a+120*i,self.x,self.y))
               
        self.px=self.lm[0][0]
        self.py=self.lm[0][1]

        for i in(2,1):
            self.l.append(canvas.create_line(polarec(self.m,self.a+120*i,self.px,self.py)))
            self.lm.append(polarec(self.m,self.a+120*i,self.px,self.py))
        self.px=self.lm[1][0]
        self.py=self.lm[1][1]

        for i in(2,3):
            self.l.append(canvas.create_line(polarec(self.m,self.a+120*i,self.px,self.py)))
            self.lm.append(polarec(self.m,self.a+120*i,self.px,self.py))
            
        self.px=self.lm[2][0]
        self.py=self.lm[2][1]

        for i in range(2):
            self.l.append(canvas.create_line(polarec(self.m,self.a+120*i,self.px,self.py)))
            self.lm.append(polarec(self.m,self.a+120*i,self.px,self.py))

        canvas.update()
         
    ### Mover arriba cubo
    def ir_arr(self):
        for x in range(0,12):
            canvas.move(x,0,-0.2)
            tk.update()
    ### Mover abajo el cubo                  
    def ir_abj(self):
        for i in range(0,12):
            canvas.move(i,0,0.2)
            tk.update()       
    ### Mover a la derecha el cubo
    def ir_der(self):
        for i in range(0,12):
            canvas.move(i,0.2,0)
            tk.update()
    ### Mover a la izquierda el cubo        
    def ir_izq(self):
        for i in range(0,12):
            canvas.move(i,-0.2,0)
            tk.update()                
        

def cubo():
    ### Creal el objeto cubo
    cub = Cubo(100,30,200,200)
    cub.dibujar()
    ### Mover el cubo segun los parametro
    # recibidos por el socket
    def mover():
        try:
            while True :
                
                if l[0] == 'izquierda':
                    cub.ir_izq()
                    
                if l[0] == 'arriba':
                    cub.ir_arr()
                    
                if l[0] == 'abajo':
                    cub.ir_abj()
                    
                if l[0]== 'derecha':
                    cub.ir_der()                             
        except:
            pass      
    mover()
    
### Crear el objeto del socket   
def soket():       
    ser = Servidor()
       
   
if __name__ == "__main__":
    tk.geometry("710x405")
    tk.configure(background =  "#006")
    ### Mostrar la cantidad de Threards en ejecucion
    print("Hilos activos:",threading.active_count())
    IP.ip()
    soket()
    cubo()
    
      
    

   
   
    
        

    
