# Generated by Django 4.1.7 on 2023-03-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0007_alter_menu_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название меню'),
        ),
    ]
