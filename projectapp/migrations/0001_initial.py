# Generated by Django 3.1.4 on 2021-01-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='project/')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]