from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=20)
    option_two = models.CharField(max_length=20)
    option_three = models.CharField(max_length=20)
    option_count_one =models.IntegerField(default=0)
    option_count_two =models.IntegerField(default=0)
    option_count_three =models.IntegerField(default=0)

    def total(self):
        return self.option_count_one + self.option_count_two  +  self.option_count_three

