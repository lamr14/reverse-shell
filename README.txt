http://www.pythondiario.com/2019/12/crea-tu-primera-reverse-shell-en-python.html

¿Qué es una Shell Inversa?:
Una shell es un programa informático que puede servir como interfaz con los servicios del sistema que éste nos proporcione.

Hay dos tipos de conexiones para lograr un ataque exitoso, el inverso y el directo.
El inverso es recomendable y lo tocaremos en este artículo, aunque dando una sencilla explicación "es cuando la victima se conecta a nosotros",
mientras que el directo, es el proceso contrario, tendremos que conectarnos a la máquina victima.
Una conexión directa es un poco más fácil, ya que lo único que tenemos que hacer es conectarnos cuando lo deseemos.

Ahora hablemos de los descriptores de archivo.
Hay tres flujos en la Entrada y Salida (E/S o en Inglés I/O), estos son llamados:

STDIN (Standard Input): Es la entrada de los datos. Puede ser enviada por un teclado o por cualquier dispositivo físico o electrónico que desea comunicarse con el programa en espera.
STDOUT (Standard Ouput): Es la salida de los datos, cómo el resultado de una operación mayormente exitosa.
STDERR (Standard Error): Es la salida de los datos, pero está vez cuando es causada por un error.

