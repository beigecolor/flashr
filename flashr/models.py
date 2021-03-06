from django.utils import timezone
from django.db import models
from accounts.models import Profile

# Create your models here.
class Tag(models.Model):
  content = models.TextField()
  color_code = models.CharField(max_length=100)

  def __str__(self):
    return self.content
  
class Question(models.Model):
  author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='question')
  title = models.CharField(max_length=100)
  content = models.TextField(null=True, blank=True)
  tags = models.ManyToManyField(Tag, blank=True)

  def __str__(self):
    return self.title

class Deck(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='deck')
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='deck')
  order_idx = models.IntegerField()

  # def __str__(self):
  #   return self.order_idx
    
class Pain(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='pain')
  question = models.ForeignKey(Question, on_delete=models. CASCADE, related_name='pain')
  level = models.IntegerField()
  time_stamp = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(f'{self.time_stamp}: pain {self.level} - q {self.question.id}')

class Answer(models.Model):
  author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='answer')
  question = models.ForeignKey(Question, on_delete=models. CASCADE, related_name='answer')
  public = models.BooleanField(default=False)
  content = models.TextField()
  time_stamp = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.content

class Vote(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='vote')
  answer = models.ForeignKey(Answer, on_delete=models. CASCADE, related_name='vote')
  vote = models.IntegerField() # test with default=0
  time_stamp = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(self.vote)