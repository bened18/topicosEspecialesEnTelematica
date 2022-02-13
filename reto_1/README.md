Yacurl se creó con la finalidad de estudiar la comunicación de dos procesos / aplicaciones en Internet para implementar un servicio distribuido como mecanismo para entender y dominar los estándares de la Web (HTTP, HTML y URLs). 

Utilizaremos Sockets como mecanismo de comunicación para el cliente yacurl y un Web Service cualquiera.

Pasos para utilizar el cliente yacurl:
    
    1. Instalar todas las librerías del archivo "requirements.txt"
    
    2. Puede ejecutar yacurl de 3 formas en una terminal:
        A. "$ python main.py yacurl" 
        B. "$ python main.py yacurl -h <HOST>"
        C. "$ python main.py yacurl -h <HOST> -p <PORT>"

    3. Opción A: El cliente yacurl iniciara y solicitará un HOST cualquiera a quien se realizara una petición, utilizar siempre el formato "www.eldominiodeseado.com" y presionar Enter para confirmar HOST.
    Seguidamente yacurl solicitara el puerto por el cual deberá crear la conexión, escribir el puerto por el que desee conectarse (80 o 443), si no se especifica un puerto yacurl tomará por defecto el puerto 80. Presionar Enter para confirmar.

    4. Opción B: después de -h deberá especificar el HOST al que desea conectarse y presionar enter. 
    Seguido yacurl preguntará el puerto deseado, si no se especifica tomará por defecto el puerto 80.

    5. Opción C: después de -h deberá especificar el HOST al que desea conectarse y después de -p deberá especificar el puerto igualmente y presionar enter para empezar la ejecución de yacurl.

    

Funcionamiento del cliente yacurl:

    1. yacurl iniciara la conexión con el HOST y puerto especificados anteriormente y realizara una solicitud GET / HTTP/1.1 y solicitara los archivos html de dicho HOST.

    2. Cuando yacurl reciba la respuesta del HOST (http response), entonces parseara la respuesta guardando el html en el archivo generado "parsing.html".
    
    3. Por ultimo en consola se observara el trafico generado con el protocolo TCP en el puerto especificado y se mostrarán todos los protocolos decodificados de el paquete http.request y http.response.
    
    4. yacurl cerrará la conexión con el HOST y el socket finalizara su ejecución.

Importante: 
    Si se esta utilizando el puerto 80 y se recibe respuesta con código 301 en el archivo "parsing.html", entonces cambiar el puerto 80 para ese HOST por el puerto 443 y viceversa.



Visita el repositorio del proyecto en: https://github.com/bened18/topicosEspecialesEnTelematica/tree/master/reto_1