# 🖥️ Control Remoto de Cubo 3D con Tkinter y Sockets

Este proyecto consiste en una aplicación de red entre dos PCs conectados en la misma red local. Utilizando Python con `Tkinter` y `sockets`, se implementa un sistema cliente-servidor donde un PC actúa como **servidor gráfico** mostrando un cubo 3D, y otro como **cliente** con una interfaz para controlarlo de forma remota.

## 🎯 Objetivo del Proyecto

Permitir el **control remoto de un cubo 3D** mediante comandos enviados por red desde una interfaz cliente, utilizando una conexión socket entre dos computadoras que comparten la misma red local.

---

## ⚙️ Tecnologías Utilizadas

- **Python 3**
- **Tkinter**: Para las interfaces gráficas de usuario.
- **Sockets (módulo socket)**: Para la comunicación TCP/IP entre cliente y servidor.
- **Canvas 3D/Tkinter Canvas (simulación básica de 3D)**: Para la representación del cubo.
- **Threading**: Para mantener la escucha del servidor sin bloquear la interfaz.

---

## 🌐 Comunicación entre los equipos

- El servidor escucha conexiones en un puerto específico.
- El cliente se conecta mediante la IP local del servidor.
- Los comandos se envían como texto plano y son interpretados por el servidor para mover el cubo en tiempo real.

---

## 🖼️ Vista de la Aplicación

*Reemplaza el siguiente enlace con tu imagen del proyecto:*

![Vista del Proyecto](https://github.com/JHONATAN9A/Sockets_and_TK-inter/blob/main/img_t_a.png)
