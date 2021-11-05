from django.db import models

# Create your models here.
class Proveedores(models.Model): #Tabla de Proveedores
    codigo_empresa = models.CharField(max_length=10, primary_key=True, default=0) 
    nombre = models.CharField(max_length=50, default='')
    direccion = models.CharField(max_length=50, default='')
    telefono = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.codigo_empresa, self.nombre, self.direccion, self.telefono, self.email

class Existencias(models.Model):#tabla de existencias
    codigo_producto = models.CharField(max_length=10, primary_key=True, default='')
    descripcion = models.CharField(max_length=250, default='')
    cantidad = models.IntegerField(default=0)
    fecha_ingreso = models.DateField()
    fecha_vencimiento = models.DateField()
    def __str__(self):
        return self.codigo_producto, self.descripcion, self.cantidad, self.fecha_vencimiento


class Portafolio(models.Model): #tabla deProductos
    codigo_empresa = models.ForeignKey(Proveedores, on_delete=models.CASCADE, null=True, blank=True)
    codigo_producto = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.BooleanField(default=True, blank=True, null=True, verbose_name='Disponible', help_text='Disponible',)

    def __str__(self):
        return self.codigo_empresa, self.codigo_producto , self.nombre, self.descripcion, self.precio



class Stock(models.Model): #tabla de stock
   
    id_producto = models.ForeignKey(Existencias, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=250, default='')
    stockmax = models.IntegerField(default=0)
    stockmin = models.IntegerField(default=0)
    stockrecomendado = models.IntegerField(default=0)
    fecha_ingreso = models.DateField(default= '2020-01-01')
    fecha_vencimiento = models.DateField(default= '2020-01-01')
    def __str__(self):
        return self.id_producto, self.descripcion, self.stockmax, self.stockmin, self.stockrecomendado, self.fecha_vencimiento


class Mejorprecio(models.Model): #tabla de mejores precios
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Existencias, on_delete=models.CASCADE)
    precio_minimo = models.FloatField(default=0)
    def __str__(self):
        return self.id_proveedor, self.id_producto, self.precio_minimo


class Cotizaciones(models.Model): #tabla de cotizaciones
    id_producto = models.ForeignKey(Existencias, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250)
    precio = models.FloatField(default=0)
    def __str__(self):
        return self.id_proveedor, self.id_producto, self.precio