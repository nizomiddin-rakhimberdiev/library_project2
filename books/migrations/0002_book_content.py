# Generated by Django 4.2.5 on 2023-09-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(),
            preserve_default=False,
        ),
    ]
