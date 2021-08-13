# Generated by Django 3.2 on 2021-06-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Contact', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('Email_Id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=20)),
                ('Unit', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('Email_Id', models.CharField(max_length=50)),
                ('Plan', models.CharField(max_length=50)),
                ('Join_Date', models.CharField(max_length=20)),
                ('Expiry_Date', models.CharField(max_length=20)),
                ('Initial_Amount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Amount', models.CharField(max_length=20)),
                ('Duration', models.CharField(max_length=20)),
            ],
        ),
    ]