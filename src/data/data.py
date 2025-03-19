class Data:
    
    def invertir_lista(self, lista):
        inicio=0
        fin= len(lista) -1
        while inicio < fin:
            lista[inicio],lista[fin]=lista[fin],lista[inicio]
            inicio += 1
            fin -= 1
        return lista
        
    
    def buscar_elemento(self, lista, elemento):
        for i in range (len(lista)):
            if lista [i] == elemento:
                return i
            return -1
    
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
    
    def rotar_lista(self, lista, k):
        n= len(lista)
        k= k%n
        return lista[-k: ] + lista[:-k]

    
    def encuentra_numero_faltante(self, lista):
        n= len(lista) + 1
        sumatotal= n*(n+1)//2
        sumalista=sum(lista)
        return sumatotal-sumalista
 
    def es_subconjunto(self, conjunto1, conjunto2):
        for ele in conjunto1:
            if ele not in conjunto2:
                return False
            return True

    
    def implementar_pila(self):
        pila=[]
        def push(elemento):
            pila.append(elemento)
        def pop():
            if not vacio():
                return pila[-1]
            return None
        def cima():
            if not vacio():
                return pila[-1]
            return None
        def vacio():
            return len(pila)==0
        return{
            "push":push,
            "pop":pop,
            "cima":cima,
            "vacio":vacio
        }
    
    def implementar_cola(self):
        cola=[]
        def enqueue(elemento):
            cola.append(elemento)
        
        def dequeue():
            if not vacio():
                return cola.pop(0)
            return None
        def cima():
            if not vacio():
                return cola[0]
            return None
        def vacio():
            return len(cola)==0
        return{
            "dequeue":dequeue,
            "enqueue":enqueue,
            "cima":cima,
            "vacio":vacio
        }
 
    def matriz_transpuesta(self, matriz):
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]