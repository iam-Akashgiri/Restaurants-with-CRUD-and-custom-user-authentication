# Generated by Django 4.2.2 on 2024-01-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='BgImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
