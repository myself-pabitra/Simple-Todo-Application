# Generated by Django 4.0 on 2022-03-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_alter_notes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
