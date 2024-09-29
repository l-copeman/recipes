from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False )
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_uploads"
    )
    serves = models.PositiveIntegerField(blank=False, null=False)
    ingredients = models.TextField(blank=False, null=False)
    method = models.TextField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=False, null=False)
