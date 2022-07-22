from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_id = models.IntegerField(primary_key=True, default=0)
    topic_title = models.CharField(max_length=50)

    def __str__(self):
        return self.topic_title

class SubTopic(models.Model):
    stopic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sub_topic_title = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_topic_title

