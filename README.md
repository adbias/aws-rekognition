# aws-rekognition
Aplicación de prueba en Python para la suite de AWS Rekognition.

## Librerias
- boto3
- logging

```
pip install boto3
```

## Modo de uso
La idea es tener imágenes de prueba dentro de la carpeta `images` de la aplicación e ingresar
en la línea de comandos el nombre del archivo y lo que dice la imagen para
comparar si el reconocimiento se hizo de forma correcta.

Ejemplo:
```
tarea-rekognition> python .\tarea_rekognition.py
----------------------------------------------------------------------------------------
Tarea Rekognition Adbias Palacios
----------------------------------------------------------------------------------------
Name of the image: text.png
Text of the image: it's monday but keep smiling
Detecting text in text.png...
true
Done.
Press enter to continue.
----------------------------------------------------------------------------------------
```

## Objetos de prueba

Las imágenes de prueba están en la carpeta `images`.

## Máximo de carácteres

Calculado con la imagen `length.png`, es de 300 carácteres.

## Archivo de registro

El log de ejecución de las pruebas está en el archivo `log.txt`.