from django.db import models


# Help From Code With Stien


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

