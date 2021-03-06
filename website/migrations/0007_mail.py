# Generated by Django 2.2.5 on 2021-05-18 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
    ]
