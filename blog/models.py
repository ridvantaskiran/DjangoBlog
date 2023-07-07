from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.CharField(max_length=350, null=True, help_text='Enter Bio')
    birthday = models.DateField()

    class Meta:
        ordering = ['user', 'bio']

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
    #Returns the URL to access a particular instance of the model.
        return reverse('author_detail', args=[str(self.id)])


class Post(models.Model):
    #one-->many
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, help_text='Enter the post title')
    content = models.TextField(help_text='Content')
    likes = models.ManyToManyField(User, blank=True, related_name='liked_posts')
    create_date = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'post'
        ordering = ['-create_date']

    def get_absolute_url(self):
    #Returns the URL to access a particular instance of the model.
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    #one-->many
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=300, help_text='Enter your comment here')
    likes = models.ManyToManyField(User, blank=True, related_name='liked_comments')
    create_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_comment=75
        if len(self.content)>len_comment:
            comment=self.content[:len_comment] + '...'
        else:
            comment=self.content
        return comment
    
    def number_of_likes(self):
        return self.likes.count()