from django.db import models

class Task(models.Model):
    description = models.CharField(verbose_name='Описание', max_length=300, null=False, blank=False)
    status = models.CharField(verbose_name='Статус', max_length=15, null=False, blank=False, default='new')
    date_deadline = models.CharField(verbose_name='Дата выполнения', max_length=10, null=False, blank=False, default='')

    CHOICES = [('new', 'Новая'), ('process', 'В процессе'), ('done', 'Сделано')]


    def __str__(self):
        return f"{self.description}, {self.status}, {self.date_deadline}"
