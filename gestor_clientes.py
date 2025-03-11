import os

# Definir el directorio donde se almacenarán los archivos de clientes
DIRECTORIO_CLIENTES = "archivos"
os.makedirs(DIRECTORIO_CLIENTES, exist_ok=True)

# Tabla hash (diccionario) para asociar nombres de clientes con sus archivos
clientes_hash = {}

# Cargar clientes existentes en la tabla hash al iniciar el programa
def cargar_clientes():
    global clientes_hash
    clientes_hash.clear()
    for archivo in os.listdir(DIRECTORIO_CLIENTES):
        if archivo.endswith(".txt"):
            nombre_cliente = archivo.replace(".txt", "")
            clientes_hash[nombre_cliente] = os.path.join(DIRECTORIO_CLIENTES, archivo)

# Función para crear un nuevo cliente
def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ").strip()
    
    if nombre in clientes_hash:
        print("El cliente ya existe. Use la opción de actualizar.")
    else:
        descripcion = input("Ingrese la descripción del servicio solicitado: ").strip()
        archivo = os.path.join(DIRECTORIO_CLIENTES, f"{nombre}.txt")
        with open(archivo, "w") as f:
            f.write(f"Cliente: {nombre}\n")
            f.write(f"Descripción del servicio: {descripcion}\n")
        clientes_hash[nombre] = archivo  # Actualizar tabla hash
        print("Cliente creado exitosamente.")

# Función para actualizar un cliente existente
def actualizar_cliente():
    nombre = input("Ingrese el nombre del cliente a actualizar: ").strip()
    
    if nombre in clientes_hash:
        descripcion = input("Ingrese la nueva descripción del servicio solicitado: ").strip()
        with open(clientes_hash[nombre], "a") as f:
            f.write(f"Descripción adicional: {descripcion}\n")
        print("Cliente actualizado exitosamente.")
    else:
        print("El cliente no existe. Use la opción de crear.")

# Función para listar todos los clientes
def listar_clientes():
    if clientes_hash:
        print("Clientes disponibles:")
        for nombre in clientes_hash:
            print(nombre)
    else:
        print("No hay clientes registrados.")

# Función para buscar un cliente por nombre
def buscar_cliente():
    nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
    
    if nombre in clientes_hash:
        with open(clientes_hash[nombre], "r") as f:
            print(f.read())
    else:
        print("El cliente no existe.")

# Función para borrar un cliente
def borrar_cliente():
    nombre = input("Ingrese el nombre del cliente a borrar: ").strip()
    
    if nombre in clientes_hash:
        os.remove(clientes_hash[nombre])
        del clientes_hash[nombre]  # Eliminar de la tabla hash
        print("Cliente eliminado exitosamente.")
    else:
        print("El cliente no existe.")

# Cargar clientes existentes antes de iniciar el menú
cargar_clientes()

# Menú principal
while True:
    print("\n=== GESTOR DE CLIENTES AXANET ===")
    print("1. Crear nuevo cliente")
    print("2. Actualizar cliente existente")
    print("3. Listar todos los clientes")
    print("4. Buscar cliente por nombre")
    print("5. Borrar cliente")
    print("6. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        crear_cliente()
    elif opcion == "2":
        actualizar_cliente()
    elif opcion == "3":
        listar_clientes()
    elif opcion == "4":
        buscar_cliente()
    elif opcion == "5":
        borrar_cliente()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

