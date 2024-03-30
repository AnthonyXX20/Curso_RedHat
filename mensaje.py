class mensaje:
    mensaje = ""
    list_ABC = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    lista_Encriptada = ["!","#","$","%","&","/","(",")",".","|","<",">","¿","?","[","]","_","-","♦","◘","♥","♫","▲","▼","@","☺","♠","d","r","7","5","9","↓","↨","x","6","○"    ]    

    def __init__(self, in_Message):
        self.mensaje = in_Message

    def codificar (self, in_Mensaje):
        lista_Caracteres = list(in_Mensaje)
        cantidad_Caracteres = len(lista_Caracteres)
        palabra_Codificada = ""
        for i in range (0, cantidad_Caracteres):
            caracter = lista_Caracteres[i]
            for y in range(0, len(self.lista_Encriptada)):
                if (caracter == self.list_ABC[y]):
                    palabra_Codificada = palabra_Codificada + self.lista_Encriptada[y]
        return palabra_Codificada            

    def decodificar (self, in_Mensaje):
        lista_Caracteres = list(in_Mensaje)
        cantidad_Caracteres = len(lista_Caracteres)
        palabra_Decodificada = ""
        for i in range (0, cantidad_Caracteres):
            caracter = lista_Caracteres[i]
            for y in range(0, len(self.lista_Encriptada)):
                if (caracter == self.lista_Encriptada[y]):
                    palabra_Decodificada = palabra_Decodificada + self.list_ABC[y]
        return palabra_Decodificada