class Magic:

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        seq = [0, 1]
        for _ in range(n - 2):
            seq.append(seq[-1] + seq[-2])
        return seq
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        if n < 1:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        resultado = [[1]]
        for _ in range(filas - 1):
            nueva_fila = [1] + [resultado[-1][i] + resultado[-1][i + 1] for i in range(len(resultado[-1]) - 1)] + [1]
            resultado.append(nueva_fila)
        return resultado
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b) if a and b else 0
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        digitos = [int(d) for d in str(n)]
        potencia = len(digitos)
        return sum(d ** potencia for d in digitos) == n
    
    def es_cuadrado_magico(self, matriz):
        if not matriz or len(matriz) != len(matriz[0]):
            return False
        
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        for i in range(n):
            if sum(matriz[i]) != suma_objetivo or sum(matriz[j][i] for j in range(n)) != suma_objetivo:
                return False
            if sum(matriz[i][i] for i in range(n)) != suma_objetivo or sum(matriz[i][n - i - 1] for i in range(n)) != suma_objetivo:
                return False
            return True