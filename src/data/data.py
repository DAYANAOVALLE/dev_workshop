class Data:
    
    def invertir_lista(self, lista):
        return lista[::-1]
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        return list(dict.fromkeys(lista))
    
    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultados = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultados.append(lista1[i])
                i += 1
            else:
                resultados.append(lista2[j])
                j += 1
        resultados.extend(lista1[i:])
        resultados.extend(lista2[j:])
        return resultados
    
    def rotar_lista(self, lista, k):
        if not lista:
            return []
        k = k % len(lista)
        return lista[-k:] + lista[:-k]

    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        sumatotal = n * (n + 1) // 2
        sumalista = sum(lista)
        return sumatotal - sumalista
 
    def es_subconjunto(self, conjunto1, conjunto2):
        return all(ele in conjunto2 for ele in conjunto1)
    
    def implementar_pila(self):
        pila = []

        def push(elemento):
            pila.append(elemento)

        def pop():
            if not is_empty():
                return pila.pop()
            return None

        def peek():
            if not is_empty():
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }


    def implementar_cola(self):
        cola = []

        def enqueue(elemento):
            cola.append(elemento)

        def dequeue():
            if not is_empty():
                return cola.pop(0)
            return None

        def peek():
            if not is_empty():
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
