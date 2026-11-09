from django.db import models


class Responsable(models.Model):
    id = models.AutoField(primary_key=True)  # int, PK
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254, unique=True)
    rut = models.CharField(max_length=12)

    class Meta:
        db_table = 'responsable'

    def __str__(self):
        return f'{self.nombre} ({self.correo})'


class Mascota(models.Model):
    id = models.AutoField(primary_key=True)  # int, PK
    nombre = models.CharField(max_length=100)
    anio_nacimiento = models.IntegerField()
    especie = models.CharField(max_length=50)
    # En la BD queda como la columna responsable_id (FK).
    # CASCADE: al eliminar un responsable se eliminan sus mascotas.
    responsable = models.ForeignKey(
        Responsable,
        on_delete=models.CASCADE,
        related_name='mascotas',
    )

    class Meta:
        db_table = 'mascota'

    def __str__(self):
        return f'{self.nombre} ({self.especie})'
