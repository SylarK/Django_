# Generated by Django 3.0.8 on 2020-07-27 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200727_0948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
    ]