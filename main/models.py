from django.db import models

# Create your models here.
class Proveedor(models.Model):
    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.razon_social

class Categoria(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.codigo}: {self.nombre}'

class Localizacion(models.Model):
    distrito = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.distrito}, {self.provincia}, {self.departamento}'

class Producto(models.Model):
    # Relaciones
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    # Atributos
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.FloatField()
    estado = models.CharField(max_length=3)
    descuento = models.FloatField(default=0)

    def __str__(self):
        return self.nombre

    def precio_final(self):
        return self.precio * (1 - self.descuento)

    def sku(self):
        codigo_categoria = self.categoria.codigo.zfill(4)
        codigo_producto = str(self.id).zfill(6)

        return f'{codigo_categoria}-{codigo_producto}'

class Usuarios(models.Model):
    email = models.TextField()
    password = models.CharField(max_length=15)
    dni = models.CharField(max_length=8)
    nombre = models.TextField()
    apellidoPaterno = models.TextField()
    apellidoMaterno = models.TextField()
    genero = models.CharField(max_length=1)
    fechaNacimiento = models.DateField()
    fechaCreacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellidoPaterno} {self.apellidoMaterno}'


class Cliente(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete = models.SET_NULL, null = True)
    preferencias = list()

    def _str_(self):
        return f'{self.preferencias}'

class Colaborador(models.Model):
    #Relaciones
    usuario = models.ForeignKey('Usuarios',on_delete = models.SET_NULL, null=True)
cliente = models.ForeignKey('Cliente',on_delete = models.SET_NULL, null=True)
  #Atributos
preferencias = list()

def str(self):
        return f'{self.preferencias}'

class Pedido(models.Model):
    #Relaciones
    cliente = models.ForeignKey('Cliente',on_delete = models.SET_NULL, null=True)
    colaborador = models.ForeignKey('Colaborador',on_delete = models.SET_NULL, null=True)

    #Atributos
    fechaCreacion = models.DateField()
    estado = models.TextField()
    fechaEntrega = models.DateField()
    direccionEntrega = models.TextField()
    tarifa = models.FloatField()

    def _str_(self):
        return f'{self.direccionEntrega},{self.estado}'


class DetallePedido(models.Model):
    #Relaciones
     pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True)
    #Atributos
     cantidad = models.IntegerField()
     subtotal = models.FloatField()
     def _str_(self):
         return f'"Cantidad Total": {self.cantidad}, "Subtotal": {self.subtotal}'