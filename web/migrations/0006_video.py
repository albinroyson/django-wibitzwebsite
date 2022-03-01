# Generated by Django 4.0.2 on 2022-03-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_feature_auther_desigination_feature_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='video/image')),
                ('icon', models.FileField(upload_to='video/icon')),
                ('title', models.CharField(max_length=225)),
            ],
        ),
    ]
