# Generated by Django 4.0 on 2022-03-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0006_alter_notes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
