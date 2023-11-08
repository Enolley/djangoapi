# Generated by Django 3.2.23 on 2023-11-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(default='Default')),
                ('image', models.ImageField(default='products/product.png', upload_to='products')),
            ],
        ),
    ]
