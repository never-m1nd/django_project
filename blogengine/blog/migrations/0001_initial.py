# Generated by Django 3.1 on 2020-08-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(db_index=True)),
                ('title', models.CharField(db_index=True, max_length=40)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('tags', models.ManyToManyField(related_name='posts', to='blog.Tag')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]