# Generated by Django 3.0.7 on 2020-10-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitme', '0003_auto_20201009_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_for_ML',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ml_pics')),
            ],
        ),
    ]
