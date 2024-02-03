from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.TextField('Price', max_length=10)
    description = models.TextField('Description')
    img = models.ImageField(null=True, blank=True, upload_to='meals/static/meals/img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

