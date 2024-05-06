from django.db import models


# Create your models here. model -> class -> table -> attrs == field
class MoviePosting(models.Model):
    # id - start at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    comention = models.TextField()
    rank = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} | rank: {self.rank} | active: {self.is_active}'
