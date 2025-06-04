class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArbolBin:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        self.raiz = self.insertarecursiva(self.raiz, valor)

    def insertarecursiva(self, node, valor):
        if node is None:
            return Nodo(valor)

        if valor < node.valor:
            node.left = self.insertarecursiva(node.left, valor)
        else:
            node.right = self.insertarecursiva(node.right, valor)

        return node

    def buscar(self, valor):
        return self.buscarrecursiva(self.raiz, valor)

    def buscarrecursiva(self, node, valor):
        if node is None:
            return False

        if node.valor == valor:
            return True

        if valor < node.valor:
            return self.buscarrecursiva(node.left, valor)
        else:
            return self.buscarrecursiva(node.right, valor)

    def recorridoinorden(self, node):
        if node is not None:
            self.recorridoinorden(node.left)
            print(node.valor, end=" ")
            self.recorridoinorden(node.right)

tree = ArbolBin()  # Instancia de árbol binario

# Insertando datos en un árbol binario de búsqueda
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Buscando valores en el árbol
print(tree.buscar(4))  # True
print(tree.buscar(9))  # False

print("Recorrido en orden:")  # Imprimiendo en recorrido inorden
tree.recorridoinorden(tree.raiz)
