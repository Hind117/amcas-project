from PIL.Image import Image
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    messages = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    likes = models.ManyToManyField(User)
    published = models.BooleanField(default=True)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class nasaNew(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    published = models.BooleanField(default=True)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title



class FilesAdmin(models.Model):
    adminupload=models.FileField(upload_to='images/')
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()

    def __str__(self):
        return self.title



class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)
    img = Image.open(self.image.path)
    if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


#Topic model
class Topic(models.Model):
    title=models.CharField(max_length=200)
    pdfupload=models.FileField(upload_to='images/')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#Book model
class Book(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField(upload_to='images/')
    link1 = models.CharField(max_length=200)
    link2 = models.CharField(max_length=200, blank=True)
    link3=models.CharField(max_length=200, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class MemberPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField()
    like = models.BooleanField(default=False)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
