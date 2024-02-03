from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.TextField('Price', max_length=10)
    description = models.TextField('Description')
    date_published = models.DateField('Date of Published')
    img = models.ImageField(null=True, blank=True, upload_to='mainView/static/mainView/img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
