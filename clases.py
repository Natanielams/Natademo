
class Producto:
    nombre=''
    descripcion=''
    precio=0
    stock=0

class Direccion:
    calle=''
    numero=0

class Persona:
    nombre=''
    apellido=''
    edad=0
    productos=[]
    direccion= Direccion()

    def agregar(self,pro):#self es la instancia del objeto
        self.productos.append(pro)

class Persona2:
    nombre=''
    apellido=''
    edad=0
    productos=[Producto()]

