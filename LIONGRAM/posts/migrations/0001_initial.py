# Generated by Django 4.2.6 on 2023-10-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('content', models.TextField(verbose_name='Content')),
                ('created_at', models.DateTimeField(verbose_name='Created At')),
                ('view_count', models.IntegerField(verbose_name='View Count')),
            ],
        ),
    ]
