def validar_modulo(n):
    if not isinstance(n, int):
        raise ValueError("n debe ser un número entero (ej: 7).")
    if n < 2:
        raise ValueError("n debe ser >= 2 (ej: 2, 3, 5...).")
    return True

def validar_elemento(a, n):
    if not isinstance(a, int):
        raise ValueError("El número debe ser un entero (ej: 3).")
    if a < 0 or a >= n:
        raise ValueError(f"El número debe estar entre 0 y {n-1} para Z_{n}.")
    return True

def egcd(a, b):
    a0, b0 = abs(a), abs(b)
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b0:
        q = a0 // b0
        a0, b0, x0, x1, y0, y1 = b0, a0 - q * b0, x1, x0 - q * x1, y1, y0 - q * y1
    return a0, x0, y0

def inverso_modular(a, n):
    validar_modulo(n)
    if not isinstance(a, int):
        raise ValueError("a debe ser un entero.")
    a = a % n
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

def suma_modular(a, b, n):
    validar_modulo(n)
    a = a % n
    b = b % n
    return (a + b) % n

def producto_modular(a, b, n):
    validar_modulo(n)
    a = a % n
    b = b % n
    return (a * b) % n

def division_modular(a, b, n):
    validar_modulo(n)
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a y b deben ser enteros.")
    a = a % n
    b = b % n
    inv_b = inverso_modular(b, n)
    if inv_b is None:
        raise ValueError(f"{b} NO tiene inverso en Z_{n} → la división no existe.")
    return (a * inv_b) % n

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

def cuadrados_perfectos(n):
    validar_modulo(n)
    cuadrados = set()
    for x in range(n):
        cuadrado = (x * x) % n
        cuadrados.add(cuadrado)
    return sorted(list(cuadrados))

def potencia_modular(base, exponente, n):
    validar_modulo(n)
    if not isinstance(base, int) or not isinstance(exponente, int):
        raise ValueError("base y exponente deben ser enteros.")
    base = base % n
    if exponente >= 0:
        return pow(base, exponente, n)
    inv = inverso_modular(base, n)
    if inv is None:
        raise ValueError(f"La base {base} no tiene inverso en Z_{n}; exponente negativo imposible.")
    return pow(inv, -exponente, n)

CARACTERES = "a b c d e f g h i j k l m n o p q r s t u v w x y z á é í ó ú ü esp ! ? A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Á É Í Ó Ú Ü"
LISTA_CARACTERES = CARACTERES.split(' ')
MAPA_CARACTERES = {c: i for i, c in enumerate(LISTA_CARACTERES)}
N_ALFABETO = len(LISTA_CARACTERES)

def cifrar_afin(mensaje, a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a y b deben ser enteros.")
    g, _, _ = egcd(a, N_ALFABETO)
    if g != 1:
        raise ValueError(f"El coeficiente 'a' ({a}) NO es primo relativo con {N_ALFABETO}. No se podrá descifrar.")
    resultado = []
    for ch in mensaje:
        token = 'esp' if ch == ' ' else ch
        if token not in MAPA_CARACTERES:
            raise ValueError(f"Carácter '{ch}' no está en el alfabeto")
        posicion = MAPA_CARACTERES[token]
        cifrado_pos = (a * posicion + b) % N_ALFABETO
        resultado.append(LISTA_CARACTERES[cifrado_pos])
    return ''.join(resultado)

def descifrar_afin(mensaje_cifrado, a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a y b deben ser enteros.")
    inv_a = inverso_modular(a, N_ALFABETO)
    if inv_a is None:
        raise ValueError(f"El coeficiente 'a' ({a}) NO es primo relativo con {N_ALFABETO}. No se puede descifrar.")
    tokens = []
    i = 0
    L = len(mensaje_cifrado)
    while i < L:
        if mensaje_cifrado.startswith('esp', i):
            tokens.append('esp')
            i += 3
        else:
            tokens.append(mensaje_cifrado[i])
            i += 1
    resultado = []
    for token in tokens:
        if token not in MAPA_CARACTERES:
            raise ValueError(f"Token '{token}' en el mensaje cifrado no está en el alfabeto.")
        pos = MAPA_CARACTERES[token]
        pos_orig = (inv_a * (pos - b)) % N_ALFABETO
        orig_token = LISTA_CARACTERES[pos_orig]
        resultado.append(' ' if orig_token == 'esp' else orig_token)
    return ''.join(resultado)

def pedir_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor introduce un número entero válido.")

def main():
    try:
        while True:
            print("\n--->> CALCULADORA DE OPERACIONES MODULARES <<---")
            print("1. Suma modular")
            print("2. Producto modular")
            print("3. División modular")
            print("4. Inverso modular")
            print("5. Potencia modular")
            print("6. Raíces cuadradas modulares")
            print("7. Cuadrados perfectos")
            print("8. Cifrado Afín")
            print("9. Descifrado Afín")
            print("10. Salir")

            opcion = input("Seleccione una opción: ").strip()

            try:
                if opcion == '1':
                    a = pedir_int("a = ")
                    b = pedir_int("b = ")
                    n = pedir_int("n = ")
                    print(f"Resultado: {suma_modular(a, b, n)}")

                elif opcion == '2':
                    a = pedir_int("a = ")
                    b = pedir_int("b = ")
                    n = pedir_int("n = ")
                    print(f"Resultado: {producto_modular(a, b, n)}")

                elif opcion == '3':
                    a = pedir_int("a = ")
                    b = pedir_int("b = ")
                    n = pedir_int("n = ")
                    print(f"Resultado: {division_modular(a, b, n)}")

                elif opcion == '4':
                    a = pedir_int("a = ")
                    n = pedir_int("n = ")
                    inv = inverso_modular(a, n)
                    if inv is None:
                        print(f"{a} NO tiene inverso en Z_{n}.")
                    else:
                        print(f"Inverso de {a} en Z_{n}: {inv}")

                elif opcion == '5':
                    base = pedir_int("Base = ")
                    exp = pedir_int("Exponente = ")
                    n = pedir_int("n = ")
                    print(f"Resultado: {potencia_modular(base, exp, n)}")

                elif opcion == '6':
                    a = pedir_int("a = ")
                    n = pedir_int("n = ")
                    print(f"Raíces cuadradas de {a} en Z_{n}: {raices_cuadradas(a, n)}")

                elif opcion == '7':
                    n = pedir_int("n = ")
                    print(f"Cuadrados perfectos en Z_{n}: {cuadrados_perfectos(n)}")

                elif opcion == '8':
                    mensaje = input("Mensaje: ")
                    a = pedir_int("a = ")
                    b = pedir_int("b = ")
                    print(f"Mensaje cifrado: {cifrar_afin(mensaje, a, b)}")

                elif opcion == '9':
                    mensaje_cifrado = input("Mensaje cifrado: ")
                    a = pedir_int("a = ")
                    b = pedir_int("b = ")
                    print(f"Mensaje descifrado: {descifrar_afin(mensaje_cifrado, a, b)}")

                elif opcion == '10':
                    print("Todo bien 👋")
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

            except ValueError as e:
                print(f"Error: {e}")

    except KeyboardInterrupt:
        print("\nInterrumpido. Todo bien 👋")

if __name__ == "__main__":
    main()
