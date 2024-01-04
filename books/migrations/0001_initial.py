# Generated by Django 5.0 on 2024-01-04 14:13

import books.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id_book', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
                ('publishing_company', models.CharField(max_length=100)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=books.models.upload_image_book)),
            ],
        ),
    ]