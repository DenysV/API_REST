# -*- coding: utf-8 -*-
import re

def encode(in_str):
    """
    Esta función debe devolver el string codificado de la siguiente manera:
    Por cada grupo de caracteres alfabéticos (de la A a la Z sin incluir la Ñ y sin distinguir mayúsculas
    de minúsculas) iguales consecutivos, se incluira dicho caracter en mayúsculas seguido del número de repeticiones.
    Por ejemplo para la entrada "aaAabaccCBb", la salida debe ser "A4B1A1C3B2"
    :param in_str: string de entrada. Estará formado por letras de la A a la Z sin incluir la Ñ
    :return: string codificado como se describe más arriba
    """
    pattern = re.compile("[A-Za-z]+")
    if pattern.fullmatch(in_str) is not None:
        res = ''
        k = 1
        in_str = in_str.upper()
        for i in range(1, len(in_str)):
            if in_str[i] == in_str[i-1]:
                k += 1
            else:
                res += in_str[i-1] + str(k)
                k = 1
        if res[-2] != in_str[-2]:
            res += in_str[-2] + str(k)
        return res
    else:
        return 'Word %s has spanish letters.' %  in_str
