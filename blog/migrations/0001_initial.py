# Generated by Django 4.0.2 on 2022-02-06 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(db_index=True, max_length=90, verbose_name='name category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='name post')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='text post')),
                ('publish', models.BooleanField(default=True)),
                ('datearticle', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='blog/', verbose_name='photo')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.categorypost', verbose_name='category')),
            ],
            options={
                'verbose_name': 'New post',
                'verbose_name_plural': 'All posts',
            },
        ),
    ]
