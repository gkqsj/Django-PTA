from django.db import models

# Create your models here.
class  People(models.Model):
    name = models.CharField(verbose_name = 'Nome_completo', max_length = 100)
    cpf = models.IntegerField('CPF', primary_key = True, unique = True)
    email = models.EmailField('E-mail', null = True)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

        def __str__(self):
            return self.name
