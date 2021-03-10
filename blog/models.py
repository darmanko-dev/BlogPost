from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Timespametedmodels(models.Model):
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    
    class Meta:
        abstract = True


class Post(Timespametedmodels):
    title = models.name = models.CharField(max_length=255)
    body = models.TextField()
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    
    def get_absolute_url(self):
        return reverse('show', kwargs={
            'pk': self.pk
        })
    
    def __str__(self):
        return self.title
    
class Comment(Timespametedmodels):
    post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='comments') 
    user = models.ForeignKey(User , on_delete=models.CASCADE) 
    content = models.TextField(max_length=160 ) 
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    

    def __str__(self):
        return '{} {}'.format(self.post.title ,str(self.user.username))