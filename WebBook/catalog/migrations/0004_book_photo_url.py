# Generated by Django 4.2.6 on 2023-11-06 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_author_surname_alter_book_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo_url',
            field=models.CharField(blank=True, help_text='URL-photo', max_length=200, null=True, verbose_name='URL-photo'),
        ),
    ]
