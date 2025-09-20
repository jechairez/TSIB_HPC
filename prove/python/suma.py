import sys
 
# Verificar que el usuario dio al menos un argumento
if len(sys.argv) < 2:
    print("Recuerda que debes incluir un valor")
    sys.exit(1)
 
# Tomar el primer argumento (argv[1]) y convertirlo a entero
N = int(sys.argv[1])
 
# Calcular la suma de 1 hasta N
suma = sum(range(1, N+1))
 
print(f"Suma de 1 hasta {N} = {suma}")
