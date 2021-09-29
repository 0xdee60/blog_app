from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug':self.slug
        })

    def get_absolute_url_delete(self):
        return reverse("delete", kwargs={
            'slug':self.slug
        })

    def get_absolute_url_update(self):
        return reverse("update", kwargs={
            'slug':self.slug
        })

    def get_like_url(self):
        return reverse("like", kwargs={
            'slug':self.slug
        })

    @property
    def get_like_count(self):
        return self.like_set.all().count()
        
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def comments(self):
        return self.comment_set.all()
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self) :
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

