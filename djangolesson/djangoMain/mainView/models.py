from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.TextField('Price', max_length=10)
    description = models.TextField('Description')
    img = models.ImageField(null=True, blank=True, upload_to='mainView/static/mainView/img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Main'
        verbose_name_plural = 'Mains'

class Articles1(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.TextField('Price', max_length=10)
    description = models.TextField('Description')
    img = models.ImageField(null=True, blank=True, upload_to='mainView/static/mainView/img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Buy'
        verbose_name_plural = 'Buys'
