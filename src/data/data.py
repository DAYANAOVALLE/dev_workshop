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
        i,j = 0,0
        resultados=[]
        while i <len(lista1)and j<len(lista2):
            if lista1[i]<lista2[j]:
                resultados.append(lista1[i])
                i+= 1
            else: 
                resultados.append(lista2[j])
                j+= 1
        resultados.extend(lista1[i:])
        resultados.extend(lista2[j:])
        return resultados
        pass
    def rotar_lista(self, lista, k):
        n= len(lista)
        k= k%n
        return lista[-k: ] + lista[:-k]
   
        pass
    
    def encuentra_numero_faltante(self, lista):
        n= len(lista) + 1
        sumatotal= n*(n+1)//2
        sumalista=sum(lista)
        return sumatotal-sumalista
 
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for ele in conjunto1:
            if ele not in conjunto2:
                return False
            return True
 
        pass
    
    def implementar_pila(self):
        
 
        pass
    
    def implementar_cola(self):
  
        pass
    
    def matriz_transpuesta(self, matriz):
 
        pass