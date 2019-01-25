from django.db import models

class languagecont(models.Model):
    language = models.CharField(max_length=200)
    information = models.TextField()
    figure = models.CharField(max_length=200)
    figureinfo = models.TextField()
    figuredob = models.CharField(max_length=200)


class example(models.Model):
    examName = models.CharField(max_length=200)
    examOne = models.TextField()
    examTwo = models.TextField()
    examThree = models.TextField()
    popeditors = models.CharField(max_length=200, default='Popular Editors')
    popeditor1 = models.CharField(max_length=200, default=' ')
    popeditor1link = models.CharField(max_length=200, default=' ')
    popeditor2 = models.CharField(max_length=200, default=' ')
    popeditor2link = models.CharField(max_length=200, default=' ')
    popeditor3 = models.CharField(max_length=200, default=' ')
    popeditor3link = models.CharField(max_length=200, default=' ')
    popeditor4 = models.CharField(max_length=200, default=' ')
    popeditor4link = models.CharField(max_length=200, default=' ')

class usage(models.Model):
    usagehead = models.CharField(max_length=200, default='Usage')
    usagebody = models.TextField(default=' ')

class about(models.Model):
    about1 = models.TextField(default=' ')
    about2 = models.TextField(default=' ')

class contact(models.Model):
    CEO = models.CharField(max_length=200, default=' ')
    email = models.CharField(max_length=200, default=' ')
    telephone = models.CharField(max_length=200, default=' ')



