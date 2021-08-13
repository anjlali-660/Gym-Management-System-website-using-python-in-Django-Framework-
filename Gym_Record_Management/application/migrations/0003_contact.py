# Generated by Django 3.2 on 2021-06-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_rename_equipents_equipments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Contact', models.CharField(max_length=20)),
                ('Email_Id', models.EmailField(max_length=50)),
                ('Age', models.CharField(max_length=20)),
                ('Describe', models.TextField(max_length=300)),
            ],
        ),
    ]
