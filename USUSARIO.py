##Usuario
from tkinter import *
import threading
import socket
import sys
import os
ventana = Tk()
              
class Usuario():
    def __init__(self, host, port):
        #Crear socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conectar socket
        self.sock.connect((str(host), int(port))) 
    # Enviar el mesaje para mover arriba   
    def msg_arr(self):
        self.mensaje = ('arriba')
        self.sock.send(self.mensaje.encode())
    # Enviar mensaje para mover abajo    
    def msg_abaj(self):
        self.mensaje = ('abajo')
        self.sock.send(self.mensaje.encode())
    # Enviar mensaje para mover derecha   
    def msg_drc(self):
        self.mensaje = ('derecha')
        self.sock.send(self.mensaje.encode())
     # Enviar mensaje para mover izquierda   
    def msg_izq(self):
        self.mensaje = ('izquierda')
        self.sock.send(self.mensaje.encode())
# TK para recibir IP/SERVER        
ip_ent = Entry(ventana)
ip_ent.insert(0,"192.168.0.17")
ip_ent.place(x=100,y=10)
ip = Label(ventana, text= "IP" ).place(x=70,y=10)
puerto = Entry(ventana)
puerto.insert(0,"8181")
puerto.place(x=100,y=40)
puert = Label(ventana, text= "PORT" ).place(x=60,y=40)
# Crear botones para mover cubo en servidor
def usua():
    tk = Tk()
    tk.geometry("250x200")
    usu = Usuario(str(ip_ent.get()),eval(puerto.get()))
    def mov_arr():
        usu.msg_arr()
    boton = Button(tk, text="Up", command= mov_arr, bg='blue',width=10, height=3, anchor="center",cursor="crosshair" ).place(x=80,y=5)
    
    def mov_abaj():
        usu.msg_abaj()
    boton = Button(tk, text="Down", command= mov_abaj,bg='blue',width=10, height=3, anchor="center",cursor="crosshair" ).place(x=80,y=130)
    

    def mov_der():
        usu.msg_drc()
    boton = Button(tk, text="Right", command= mov_der,bg='blue',width=10, height=3, anchor="center",cursor="crosshair" ).place(x=130,y=70)
    

    def mov_izq():
        usu.msg_izq()
    boton = Button(tk, text="Left", command= mov_izq, bg='blue',width=10, height=3, anchor="center",cursor="crosshair" ).place(x=30,y=70)
    tk.mainloop()
    
def comenzar():
    usua()
    ventana.quit()
         
boton = Button(ventana, text="CONECTAR", command=comenzar,).place(x=220,y=70)

    
    
if __name__ == "__main__":
    ventana.geometry("300x100")
    ventana.mainloop()
    
        

    
    

     
