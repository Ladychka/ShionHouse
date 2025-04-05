# Generated by Django 5.1.4 on 2025-02-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_productassignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MainProductName', models.CharField(max_length=200, null=True)),
                ('MainProductImage', models.ImageField(blank=True, null=True, upload_to='productImages/')),
            ],
        ),
    ]
