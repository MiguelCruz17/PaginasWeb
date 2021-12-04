from peewee import *
from Modelo import  *

db = SqliteDatabase('Data.db')

# ****************************** CREACIÓN DE TABLAS ******************************** #

# Tabla de Factura

class Facturas_A(Model):
    Fecha = TextField()
    Cliente_id = IntegerField()
    Descripcion = TextField()
    Subtotal = IntegerField()
    Itbis = IntegerField()
    Total = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.




# Tabla Detalles de Factura

class Facturas_Detalle(Model):
    f_id = ForeignKeyField(Facturas_A,backref='Detalle')
    Codigo = IntegerField()
    Nombre = TextField()
    Precio = FloatField()
    Cantidad = IntegerField()
    Total = FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.



# Tabla de Clientes

class Cliente(Model):
    Correo = TextField()
    Nombre = TextField()
    Apellido = TextField()
    Rnc = TextField(unique=True)
    Telefono = TextField()
    class Meta:
        database = db # This model uses the "people.db" database.




# Tabla de Articulos

class Articulo(Model):
    Codigo = TextField(unique=True)
    Tipo = TextField()
    Nombre = TextField()
    Precio = FloatField()
    Cantidad = IntegerField()
    Comentario = TextField()

    class Meta:
        database = db # This model uses the "people.db" database.        



db.connect()
db.create_tables([Facturas_A, Facturas_Detalle, Cliente, Articulo])

# ***********- METODO FACTURA -*********** #

def guardar(F:Factura):
    Fac = Facturas_A()
    Fac.Fecha = F.Fecha
    Fac.Cliente_id = F.Cliente_id
    Fac.Descripcion = F.Descripcion
    Fac.Subtotal = F.Subtotal
    Fac.Itbis = F.Itbis
    Fac.Total = F.Total
    Fac.save()

    for D in F.Detalle:
        Detal = Facturas_Detalle()
        Detal.f_id = D.f_id
        Detal.Codigo = D.Codigo 
        Detal.Nombre = D.Nombre
        Detal.Precio = D.Precio
        Detal.Cantidad = D.Cantidad
        Detal.Total = D.Total 
        Detal.save()

def cargar():
    Fac = []
    for P in Facturas_A.select().dicts():
        Fac.append(P)
    return Fac

def actualizar(F:Factura):
    Fac = Facturas_A().get(Facturas_A.id == F.id)
    Fac.Fecha = F.Fecha
    Fac.Cliente_id = F.Cliente_id
    Fac.Descripcion = F.Descripcion
    Fac.Subtotal = F.Subtotal
    Fac.Itbis = F.Itbis
    Fac.Total = F.Total
    Fac.save()

def eliminar(F:Factura):
    
    Fac = Facturas_A().get(Facturas_A.id == F.id)
    Fac.delete_instance(F.id)
    Fac.save()
    
   
# *************- METODOS CLIENTE -*************

def  GuardarCliente(CL: Clientes):
    C = Cliente()
    C.Correo = CL.Correo
    C.Nombre = CL.Nombre
    C.Apellido = CL.Apellido
    C.Rnc = CL.Rnc
    C.Telefono = CL.Telefono
    C.save()


def CargarClientes():
    LCliente = []
    for C in Cliente.select().dicts():
        LCliente.append(C)
    return LCliente


def ActualizarCliente(CL: Clientes):
    C = Cliente().get(Cliente.id == CL.id)
    C.Correo = CL.Correo
    C.Nombre = CL.Nombre
    C.Apellido = CL.Apellido
    C.Rnc = CL.Rnc
    C.Telefono = CL.Telefono
    C.save()


def EliminarCliente(CL: Clientes):
    
    C = Cliente.get(Cliente.id == CL.id)
    C.delete_instance(CL.id)
    C.save()


# *************- METODOS ARTICULO -*************

def  GuardarArticulo(Art: Articulos):
    A = Articulo()
    A.Codigo = Art.Codigo
    A.Tipo = Art.Tipo
    A.Nombre = Art.Nombre
    A.Precio = Art.Precio
    A.Cantidad = Art.Cantidad
    A.Comentario = Art.Comentario 
    A.save()


def CargarArticulo():
    LArt = []
    for A in Articulo.select().dicts():
        LArt.append(A)
    return LArt


def ActualizarArticulo(Art: Articulos):
    A = Articulo().get(Articulo.id == Art.id)
    A.Codigo = Art.Codigo
    A.Tipo = Art.Tipo
    A.Nombre = Art.Nombre
    A.Precio = Art.Precio
    A.Cantidad = Art.Cantidad
    A.Comentario = Art.Comentario 
    A.save()    

def EliminarArticulo(Art: Articulos):
    
    A = Articulo().get(Articulo.id == Art.id)
    A.delete_instance(Art.id)
    A.save()