class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        inicio=0
        fin= len(lista) -1
        while inicio < fin:
            lista[inicio],lista[fin]=lista[fin],lista[inicio]
            inicio += 1
            fin -= 1
        return lista
        
        pass
    
    def buscar_elemento(self, lista, elemento):
        for i in range (len(lista)):
            if lista [i] == elemento:
                return i
            return -1
        pass
    
    def eliminar_duplicados(self, lista):
        resultados=[]
        for ele in lista:
            if ele not in resultados:
                resultados.append(ele)
            return resultados
        pass    
    def merge_ordenado(self, lista1, lista2):
        pass


    
    def rotar_lista(self, lista, k):
   
        pass
    
    def encuentra_numero_faltante(self, lista):
 
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
 
        pass
    
    def implementar_pila(self):
 
        pass
    
    def implementar_cola(self):
  
        pass
    
    def matriz_transpuesta(self, matriz):
 
        pass