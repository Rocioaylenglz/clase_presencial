import pygame as py

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes



personaje_quieto = [py.image.load(r"Recursos\0.png")]
personaje_camina_derecha = [py.image.load(r"Recursos\1.png"),
                            py.image.load(r"Recursos\2.png")]
personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta = [py.image.load(r"Recursos\3.png")]