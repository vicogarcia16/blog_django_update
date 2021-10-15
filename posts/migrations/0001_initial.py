# Generated by Django 3.2.7 on 2021-10-15 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('miniature', models.ImageField(upload_to='posts/images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category')),
            ],
        ),
    ]
