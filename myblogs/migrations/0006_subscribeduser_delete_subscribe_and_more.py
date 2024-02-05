# Generated by Django 5.0.1 on 2024-01-23 08:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0005_blog_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='subscribe',
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='blog_description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]