# Generated by Django 4.2.2 on 2023-06-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('purchaser', models.TextField(default='Abdullah')),
                ('description', models.TextField(default='Abdullah Shaghnoba')),
            ],
        ),
    ]