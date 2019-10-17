from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

SUBJECT_OPTIONS =(
       ('', 'Unknown'),
       ('Python', 'Python'),
       ('Django', 'Django'),
       ('Angular', 'Angular'),
    )
class Question(models.Model):
    Subject_name = models.CharField(max_length=255, choices=SUBJECT_OPTIONS)
    question = models.CharField(max_length=100)
    image = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.question
    