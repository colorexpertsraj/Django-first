from django.db import models
# Create your models here.

# SuperUserInformation
# User: Rajjak
# Email: colorexpertsraj@gmail.com
# Password: Rajjak

# CREATE SOME TEST DATA WITH SOME SHELL COMMANDS:

# python manage.py shell

# from first_app.models import Topic
# print(Topic.objects.all())
# t = Topic(top_name="Social Network")
# t.save()
# print(Topic.objects.all())
# quit()


class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     age = models.IntegerField()


# class Author(models.Model):
#     name = models.CharField(max_length=50)
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)


# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     tags = models.ManyToManyField('Tag')
#
#     def __str__(self):
#         return self.title
#
# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
