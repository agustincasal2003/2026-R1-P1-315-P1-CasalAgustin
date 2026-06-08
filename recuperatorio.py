# Lista de productos
productos = []

# -------- FUNCIONES DE VALIDACIÓN --------
def validar_codigo(codigo):
    repetido = False
    for prod in productos:
        if prod[0] == codigo:
            repetido = True
    return repetido

def validar_precio():
    correcto = False
    while correcto == False:
        entrada = input("Precio (>0): ")
        # Contadores
        punto = 0
        valido = True
        for c in entrada:
            if c == ".":
                punto += 1
                if punto > 1:
                    valido = False
            elif c < "0" or c > "9":
                valido = False
        if valido == True and entrada != "":
            precio = float(entrada)
            if precio > 0:
                correcto = True
                return precio
            else:
                print("El precio debe ser mayor a 0")
        else:
            print("Error: el precio debe ser un número")


def validar_stock():
    correcto = False
    while correcto == False:
        entrada = input("Stock (>=0): ")
        valido = True
        for c in entrada:
            if c < "0" or c > "9":
                valido = False
        if valido == True and entrada != "":
            stock = int(entrada)   # recién acá convierto
            if stock >= 0:
                correcto = True
                return stock
            else:
                print("El stock no puede ser negativo")
        else:
            print("Error: el stock debe ser un número entero")


# -------- FUNCIONES PRINCIPALES --------

def cargar_producto():
    print("---- Cargar producto ----")
    codigo = input("Código: ")
    if validar_codigo(codigo):
        print("Código repetido, no se carga.")
    else:
        nombre = input("Nombre: ")
        precio = validar_precio()
        stock = validar_stock()
        producto = [codigo, nombre, precio, stock]
        productos.append(producto)
        print("Producto cargado correctamente")


def mostrar_productos():
    print("---- Mostrar productos ----")
    if len(productos) == 0:
        print("No hay productos cargados.")
    else:
        for prod in productos:
            print("Código:", prod[0], "- Nombre:", prod[1], "- Precio:", prod[2], "- Stock:", prod[3])

def buscar_producto():
    print("---- Buscar producto ----")
    buscado = input("Código a buscar: ")
    encontrado = False
    for prod in productos:
        if prod[0] == buscado:
            print("Encontrado:", prod[1], "Precio:", prod[2], "Stock:", prod[3])
            encontrado = True
    if encontrado == False:
        print("No existe ese producto")

#revision esta funcion
def ordenar_por_precio():
    print("---- Ordenar por precio ----")
    numero = len(productos)
    for i in range(numero-1):
        for j in range(numero-1-i):
            if productos[j][2] > productos[j+1][2]:
                auxiliar = productos[j]
                productos[j] = productos[j+1]
                productos[j+1] = auxiliar
    print("Productos ordenados por precio")




def menor_stock():
    print("---- Menor stock ----")
    if len(productos) > 0:
        menor = productos[0]
        for prod in productos:
            if prod[3] < menor[3]:
                menor = prod
        print("Menor stock:", menor[1], "(", menor[3], "unidades )")
    else:
        print("No hay productos cargados")

def valor_total_inventario():
    print("---- Valor total inventario ----")
    if len(productos) > 0:
        total = 0
        for prod in productos:
            total = total + (prod[2] * prod[3])
        print("Valor total:", total)
    else:
        print("No hay productos cargados")



# -------- MENÚ PRINCIPAL --------
opcion = "0"

while opcion != "7":
    print("")
    print("==============================")
    print(" SUPERMERCADO PYTHON MARKET")
    print("==============================")
    print("1. Cargar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por código")
    print("4. Ordenar productos por precio (burbuja)")
    print("5. Mostrar producto con menor stock")
    print("6. Calcular valor total del inventario")
    print("7. Salir")
    opcion = input("Elegí una opción: ")

    match opcion:
        case "1":
            cargar_producto()
        case "2":
            mostrar_productos()
        case "3":
            buscar_producto()
        case "4":
            ordenar_por_precio()
        case "5":
            menor_stock()
        case "6":
            valor_total_inventario()
        case "7":
            print("Gracias por usar Python Market")
            
        case _:
            print("Opción inválida , hay 7 opciones,vuelve a ingresar opcion")

#problema cuarta opcion no me lo ordena
