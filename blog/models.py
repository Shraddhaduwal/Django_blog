from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        # In python manage.py shell, we want the Posts to be printed by their title
        # Not like [<Post: Post object (1)>, <Post: Post object (2)>]
        # We want the post to be printed as
        # >>> Post.objects.all()
        # <QuerySet [<Post: Blog post 1>, <Post: Blog post 2>]>
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        # The redirect and reverse are different from each other
        # Redirect -> redirects to a route
        # Reverse -> gives the url to that route in a string form
