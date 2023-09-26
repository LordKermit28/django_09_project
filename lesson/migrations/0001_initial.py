# Generated by Django 4.2.5 on 2023-09-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('preview', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
