from django.db import models
from accounts.models import User

# Create your models here.

BLOG_CHOICES = (
    ('Fashion', 'Fashion'),
    ('Food', 'Food'),
    ('Travel', 'Travel'),
)
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    blog_type = models.CharField(max_length=20, choices=BLOG_CHOICES)
    date = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    picture = models.ImageField(upload_to = 'blogs')

    def __str__(self):
        return self.title