from django.db import models
from user.models import Profile
import uuid


# Create your models here.
class Job(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    average_salary = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=200, blank=True)
    mode = models.CharField(max_length=150, blank=True)
    experience = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=500, blank=True)
    qualification = models.TextField(max_length=500, blank=True)
    contact = models.PositiveBigIntegerField(default=0, blank=True)
    email = models.CharField(max_length=100, blank=True)
    related_link = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.company_name)


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    media = models.ImageField(
        null=True, blank=True, default="images/default.jpg", upload_to="images/"
    )
    domain = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    project_link = models.CharField(max_length=200, blank=True)
    like = models.ManyToManyField(Profile, related_name="like_count")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.name)


class TechTag(models.Model):
    name = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.name)
