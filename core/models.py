from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombreRol = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreRol

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    clave = models.CharField(max_length=30)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.correo  

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombreR = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombreR

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreC = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreC
    
class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}"

    def direccion_completa(self):
        return f"{self.calle} {self.numero}, {self.comuna}"

class TipoDespacho(models.Model):
    idDespacho = models.IntegerField(primary_key=True)
    nombreDespacho = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.nombreDespacho)
    
class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombreEs = models.CharField(max_length=50)
    
    def clase_boton(self):
        if self.id_estado == 1:
            return 'btn-warning'
        elif self.id_estado == 2:
            return 'btn-secondary'
        elif self.id_estado == 3:
            return 'btn-primary'
        elif self.id_estado == 4:
            return 'btn-success'
        return 'btn-default'  # Fallback class

    def __str__(self) -> str:
        return self.nombreEs

class Venta(models.Model):
    codVenta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estadoP = models.ForeignKey(Estado, on_delete=models.CASCADE)
    tipodespacho = models.ForeignKey(TipoDespacho, on_delete=models.CASCADE)
    total = models.IntegerField()
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.codVenta}"

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCa = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombreCa

class Producto(models.Model):
    codProducto = models.IntegerField(primary_key=True)
    nombreP = models.CharField(max_length=100)
    stock = models.IntegerField()
    descipcion = models.CharField(max_length=500)
    foto = models.ImageField(upload_to="productos")  # Directorio de destino para las imágenes de los productos
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreP
    
    def get_absolute_url(self):
        return reverse('detalleproducto', kwargs={'pk': self.pk})

class DetalleVenta(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

class ProductoCarrito(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class ItemCarrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombreP} - {self.usuario.username}"

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.rating} Stars"
