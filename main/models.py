from django.db import models
from account.models import MyUser


class Theme(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.author}:{self.text}'


class Likes(models.Model):
    likes = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return str(self.likes)


class Rating(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='rating'
    )
    author = models.ForeignKey(
        'account.MyUser', on_delete=models.CASCADE,
        related_name='rating', null=True
    )
    rating = models.PositiveIntegerField()


class Favorite(models.Model):
    user = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='favorites')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=True)

