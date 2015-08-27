# coding=utf-8

# Recuerda borrar los 'pass'. Pudes borrar si quieres los comentarios.
from collections import deque

class Commit:

    last_id = 1

    def __init__(self, message, changes=None, commit_padre=None):
        #############
        # COMPLETAR:
        # 'changes' es una lista de tuplas.
        # Puedes modificar esta clase a gusto tuyo.
        #############
        self.id = Commit.last_id
        Commit.last_id += 1
        self.message = message
        self.changes = changes
        self.commit_padre = commit_padre


class Branch:
    ############
    # COMPLETAR:
    # Crear __init__ con lo que consideres necesario
    ############
    def __init__(self, nombre, message, changes=None, commit_padre=None):
        self.nombre = nombre
        self.rama = deque()
        self.commit_inicial = self.new_commit(message, changes, commit_padre)
        self.estado_final = commit_inicial.changes
        
    def new_commit(self, message, changes, commit_padre):
        #############
        # COMPLETAR:
        # Agregar un nuevo commit del tipo Commit a esta branch.
        # Este commit define el estado final temporalmente.
        #############
        new_commit = Commit(message=message, changes=changes)
        self.rama.append(new_commit)
        self.estado_final = new_commit.changes
        return new_commit

    def pull(self):
        files = []
        #############
        # COMPLETAR:
        # Retornar el estado final de esta branch (una lista de archivos).
        #############
        for commit in self.rama:
            files.append(commit.changes)
        return files


class Repository:

    def __init__(self, name):
        self.name = name
        self.ramas = deque()
        self.create_branch(new_branch_name='master', message='master branch created')
        #############
        # COMPLETAR:
        # Crear branch 'master'.
        # Crear commit inicial y agregarlo a 'master'.
        #############

    def create_branch(self, message, new_branch_name, from_branch_name=None, changes=None, commit_padre=None):
        #############
        # COMPLETAR:
        # Crear branch a partir del último estado de la 'from_branch_name'.
        #############
        if new_branch_name=='master':
            branch_master = Branch(nombre='master', message='master branch created')
            self.ramas.append(branch_master)
        else:
            for branch in self.ramas:
                if branch.nombre == from_branch_name:
                    nueva_branch = Branch(message, changes, nombre=new_branch_name, commit_padre=branch.rama[-1])
                    self.ramas.append(nueva_branch)

    def branch(self, branch_name):
        #############
        # COMPLETAR:
        # Retornar la branch con el nombre 'branch_name'.
        #############
        for branch in ramas:
            if branch.nombre == branch_name:
                return branch
        return None

    def checkout(self, commit_id):
        files = []
        #############
        # COMPLETAR:
        # Buscar el commit con cierta id y retornar el estado del repositorio
        # hasta ese commit. Puede estar en cualquier branch.
        #############
        for rama in self.ramas:
            for commit in rama.rama:
                if commit.id == commit_id:
                    files.append(commit.estado_final)
        return files


if __name__ == '__main__':
    # Ejemplo de uso
    # Puedes modificarlo para probar esto pero al momento de la corrección
    # el ayudante borrará cualquier cambio y restaurará las siguientes lineas
    # a su estado original (como se muestran aquí).

    repo = Repository("syllabus 2.0")

    repo.branch("master").new_commit(Commit(
        message="agregado readme",
        changes=[("CREATE", "README.md")]
    ))

    repo.branch("master").new_commit(Commit(
        message="archivos base",
        changes=[("CREATE", "main.py"), ("CREATE", "clases.py")]
    ))

    # Creamos una rama del estado actual de 'master'
    repo.create_branch("desarrollo-de-vistas", 'master')
    repo.branch("desarrollo-de-vistas").new_commit(Commit(
        message="imagenes",
        changes=[("CREATE", "main.jpg"), ("CREATE", "user.png")]
    ))

    repo.branch("desarrollo-de-vistas").new_commit(Commit(
        message="cambiar instrucciones",
        changes=[("DELETE", "README.md"), ("CREATE", "instrucciones.html")]
    ))

    repo.branch("master").new_commit(Commit(
        message="datos recolectados",
        changes=[("CREATE", "data.csv")]
    ))

    print(repo.branch("master").pull())
    # Esperamos que el repo esté así:
    # ['.jit', 'README.md', 'main.py', 'clases.py', 'data.csv']

    print(repo.branch("desarrollo-de-vistas").pull())
    # Esperamos que el repo esté así:
    # ['.jit', 'main.py', 'clases.py',
    #  'main.jpg', 'user.png', 'instrucciones.html']

    print(repo.checkout(4))
    # Esperamos que el repo esté así:
    # ['.jit', 'README.md', 'main.py', 'clases.py', 'main.jpg', 'user.png']

    print(repo.checkout(1))
    # Esperamos que el repo esté así:
    # ['.jit']