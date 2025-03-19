class Strings:

    def es_palindromo(self, texto):
        textolim = "".join(c.lower() for c in texto if c.isalnum())
        return textolim == textolim[::-1]
    
    def invertir_cadena(self, texto):
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida
    
    def contar_vocales(self, texto):
        contador = 0
        for char in texto.lower():
            if char in "aeiou":
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        contador = 0
        for char in texto.lower():
            if char.isalpha() and char not in "aeiou":
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        def limpiar(texto):
            return "".join(c.lower() for c in texto if c.isalpha())

        return sorted(limpiar(texto1)) == sorted(limpiar(texto2))
    
    def contar_palabras(self, texto):
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):

        palabras = texto.split(" ")
        return " ".join(p.capitalize() for p in palabras)

    
    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio = False
        for char in texto:
            if char == " ":
                if not espacio:
                    resultado += char
                espacio = True
            else:
                resultado += char
                espacio = False
        return resultado
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] == '-':
            texto = texto[1:]
        return all(c in "0123456789" for c in texto)
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                inicio = ord('A') if char.isupper() else ord('a')
                resultado += chr(inicio + (ord(char) - inicio + desplazamiento) % 26)
            else:
                resultado += char
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            if texto[i:i + len_sub] == subcadena:
                posiciones.append(i)
        return posiciones
        pass