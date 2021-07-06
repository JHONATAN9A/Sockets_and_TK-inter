from tkinter import*
import socket
ventana = Tk()
ventana.geometry("300x100")
hots_ip = (socket.gethostbyname(socket.gethostname()))
### Mostrar la IP/PORT al usuario
def ip():
    ip = Label(ventana, text= "IP SERVER >" + hots_ip)
    ip.place(x=80,y=20)
    puerto = Label(ventana, text= "PORT > 8181" )
    puerto.place(x=100,y=40) 


