# Generated by Django 4.1.3 on 2023-07-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='MovieImg',
            field=models.ImageField(default='asdd', upload_to='Pics'),
            preserve_default=False,
        ),
    ]