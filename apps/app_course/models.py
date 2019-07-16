from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s the place" % self.name

class Description(models.Model):
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    desc = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.desc}"

 