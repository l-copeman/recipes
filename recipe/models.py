from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]


class Recipe(models.Model):
    """Recipe model"""
    title = models.CharField(
        max_length=300, unique=True, blank=False, null=False
    )
    slug = models.SlugField(max_length=300, unique=True)
    image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_uploads"
    )
    serves = models.PositiveIntegerField(blank=False, null=False)
    ingredients = models.TextField(max_length=900, blank=False, null=False)
    method = models.TextField(max_length=3000, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(max_length=900, blank=False, null=False)


class Comment(models.Model):
    """Comment model"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField(
        "Max characters 900", max_length=900, blank=False, null=False
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
