
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.TextField(max_length=10, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('img', models.ImageField(blank=True, null=True, upload_to='meals/static/meals/img')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
            },
        ),
    ]
