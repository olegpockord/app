from django.db import models

class Menu(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    named_url = models.CharField(max_length=150, unique=True, blank=True, null=True, verbose_name='Именованный URL')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child', on_delete=models.CASCADE)

    class Meta:
        db_table = 'menu'
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name
