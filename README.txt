http://www.pythondiario.com/2019/12/crea-tu-primera-reverse-shell-en-python.html

�Qu� es una Shell Inversa?:
Una shell es un programa inform�tico que puede servir como interfaz con los servicios del sistema que �ste nos proporcione.
A shell is a programm that can work as an interface with the system and the services that it provides us.

There are 2 kinds of connections to make a succesful attack, reverse and direct connection.
Hay dos tipos de conexiones para lograr un ataque exitoso, el inverso y el directo.

El inverso es recomendable y lo tocaremos en este art�culo, aunque dando una sencilla explicaci�n "es cuando la victima se conecta a nosotros",
mientras que el directo, es el proceso contrario, tendremos que conectarnos a la m�quina victima.
Una conexi�n directa es un poco m�s f�cil, ya que lo �nico que tenemos que hacer es conectarnos cuando lo deseemos.

We also need to understand what network sockets and file descriptors are.

Sockets are internal endpoints for sending or receiving data within a node on a computer. A socket is defined by a couple of IP addresses (local and remote), a transport protocol and a couple of port numbers (also local and remote).

Ahora hablemos de los descriptores de archivo.
Hay tres flujos en la Entrada y Salida (E/S o en Ingl�s I/O), estos son llamados:

STDIN (Standard Input): Es la entrada de los datos. Puede ser enviada por un teclado o por cualquier dispositivo f�sico o electr�nico que desea comunicarse con el programa en espera.
STDOUT (Standard Ouput): Es la salida de los datos, c�mo el resultado de una operaci�n mayormente exitosa.
STDERR (Standard Error): Es la salida de los datos, pero est� vez cuando es causada por un error.

