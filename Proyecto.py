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
