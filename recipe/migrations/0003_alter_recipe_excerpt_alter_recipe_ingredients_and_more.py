# Generated by Django 4.2.16 on 2024-09-29 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0002_recipe_image_alter_recipe_excerpt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='excerpt',
            field=models.TextField(max_length=900),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=900),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=900)),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipe.recipe')),
            ],
        ),
    ]
