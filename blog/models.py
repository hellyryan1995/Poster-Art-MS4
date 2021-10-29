from django.db import models
from django.contrib.auth.models import User


# Help From Code With Stien


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    intro = models.TextField(null=False, blank=False, default='')
    body = models.TextField(null=False, blank=False, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
    
    def __str__(self):
        return f"Comment on {self.post.title} by {self.user}"

