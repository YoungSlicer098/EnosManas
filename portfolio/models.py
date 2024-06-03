from django.db import models
from django.contrib.auth.models import AnonymousUser

# Create your models here.

class UrlPost(models.Model):
    title = models.CharField(max_length=255)
    webPage = models.URLField((""), max_length=200, null = True)

    def __str__(self):
        return '%s' % (self.title)
    

class Comment(models.Model):
    urlPost = models.ForeignKey(UrlPost, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null = True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.urlPost.title, self.name)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null = True)
    reply = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s > %s' % (self.comment.name, self.name)