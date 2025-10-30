# 1) Valida que n sea un módulo válido (entero >= 2)
def validar_modulo(n):
    if not isinstance(n, int):
        raise ValueError("n debe ser un número entero (ej: 7).")
    if n < 2:
        raise ValueError("n debe ser >= 2 (ej: 2, 3, 5...).")
    return True

# 2) Valida que un número esté en 0..n-1
def validar_elemento(a, n):
    if not isinstance(a, int):
        raise ValueError("El número debe ser un entero (ej: 3).")
    if a < 0 or a >= n:
        raise ValueError(f"El número debe estar entre 0 y {n-1} para Z_{n}.")
    return True

# 3) Algoritmo extendido de Euclides (devuelve gcd, x, y para a*x + b*y = gcd)
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

# 4) Inverso multiplicativo en Z_n (si existe)
def inverso_modular(a, n):
    validar_modulo(n)
    if not isinstance(a, int):
        raise ValueError("a debe ser un entero.")
    a = a % n
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

# 5) Suma modular: (a + b) mod n
def suma_modular(a, b, n):
    validar_modulo(n)
    validar_elemento(a, n)
    validar_elemento(b, n)
    return (a + b) % n

# 6) Producto modular: (a * b) mod n
def producto_modular(a, b, n):
    validar_modulo(n)
    validar_elemento(a, n)
    validar_elemento(b, n)
    return (a * b) % n

# 7) División en Z_n: a / b = a * b^{-1} (si b tiene inverso)
def division_modular(a, b, n):
    validar_modulo(n)
    validar_elemento(a, n)
    validar_elemento(b, n)
    inv_b = inverso_modular(b, n)
    if inv_b is None:
        raise ValueError(f"{b} NO tiene inverso en Z_{n} → la división no existe.")
    return (a * inv_b) % n

# 8) Raíces cuadradas: lista de x tales que x^2 ≡ a (mod n)
def raices_cuadradas(a, n):
    validar_modulo(n)
    if not isinstance(a, int):
        raise ValueError("a debe ser un entero.")
    a = a % n
    resultado = []
    for x in range(n):
        if (x * x) % n == a:
            resultado.append(x)
    return resultado

# 9) Cuadrados perfectos en Z_n: lista de a tales que a = x^2 (mod n) para algún x
def cuadrados_perfectos(n):
    validar_modulo(n)
    cuadrados = set()
    for x in range(n):
        # Calcula x^2 mod n
        cuadrado = (x * x) % n
        cuadrados.add(cuadrado)
    # Convierte el set a una lista ordenada para la presentación
    return sorted(list(cuadrados))

# 10) Potencia modular: (base ** exponente) mod n
def potencia_modular(base, exponente, n):
    validar_modulo(n)
    # Validamos que la base esté en Z_n
    validar_elemento(base, n) 
    if not isinstance(exponente, int):
        raise ValueError("El exponente debe ser un entero.")
    # El exponente puede ser >= n o negativo; 'pow' lo maneja eficientemente.
    # pow(base, exponente, n) calcula (base ** exponente) % n
    return pow(base, exponente, n)

# 11) Cifrado Afín: C = (a*x + b) mod m
def cifrar_afin(mensaje, a, b):
    CARACTERES = "a b c d e f g h i j k l m n o p q r s t u v w x y z á é í ó ú ü esp ! ? A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Á É Í Ó Ú Ü"
    LISTA_CARACTERES = CARACTERES.split(' ') # Split por espacio para manejar 'esp'
    MODULO_CIFRADO = len(LISTA_CARACTERES)
    # m es el tamaño del alfabeto (MODULO_CIFRADO)
    n = MODULO_CIFRADO
    
    # 1. Validar 'a': debe ser coprimo con n para que exista el inverso para descifrar
    g, _, _ = egcd(a, n)
    if g != 1:
        raise ValueError(f"El coeficiente 'a' ({a}) NO es coprimo con {n}. No se podrá descifrar.")
    
    # 2. Validar 'b' y 'a' como enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Los coeficientes 'a' y 'b' deben ser enteros.")

    mensaje_cifrado = ""
    for char in mensaje:
        if char == ' ':
            # El espacio en blanco es la palabra clave 'esp'
            posicion = LISTA_CARACTERES.index('esp')
