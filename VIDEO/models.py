from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Topic(models.Model):
    topic_id = models.AutoField
    topic_title = models.CharField(max_length=50)
    topic_duration = models.FloatField(default=None)
    topic_instructors_name = models.CharField(max_length=400, default=None)

    def __str__(self):
        return self.topic_title

class Parts_Of_Speech(models.Model):
    Parts_Of_Speech_id = models.AutoField
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    duration = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='VIDEO/PARTS-OF-SPEECH/VIDEO-IMAGE', default="")
    video = models.FileField(upload_to='VIDEO/PARTS-OF-SPEECH/VIDEOS',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    def __str__(self):
        return self.title
class Article(models.Model):
    Article_id = models.AutoField
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    duration = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='VIDEO/ARTICLE/VIDEO-IMAGE', default="")
    video = models.FileField(upload_to='VIDEO/ARTICLE/VIDEOS',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    def __str__(self):
        return self.title
class Jumbled_Sentence(models.Model):
    Jumbled_Sentence_id = models.AutoField
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    duration = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='VIDEO/JUMBLED-SENTENCES/VIDEO-IMAGE', default="")
    video = models.FileField(upload_to='VIDEO/JUMBLED-SENTENCES/VIDEOS',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    def __str__(self):
        return self.title
class Errors_and_Omission(models.Model):
    Error_and_Omission_id = models.AutoField
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    duration = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='VIDEO/ERROR-AND-OMMISION/VIDEO-IMAGE', default="")
    video = models.FileField(upload_to='VIDEO/ERROR-AND-OMMISION/VIDEOS',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    def __str__(self):
        return self.title