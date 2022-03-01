# Generated by Django 4.0.2 on 2022-03-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_marketing_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='studio/icon')),
                ('image', models.FileField(upload_to='studio/image')),
                ('title', models.CharField(max_length=225)),
                ('discribe', models.CharField(max_length=225)),
            ],
        ),
    ]
