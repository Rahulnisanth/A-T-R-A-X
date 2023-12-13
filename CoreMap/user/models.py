from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        default="images/default.jpg",
        upload_to="profile__picture/",
    )
    username = models.CharField(max_length=200, null=True, blank=True)
    batch = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(null=True, blank=True, max_length=150, unique=True)
    contact = models.PositiveBigIntegerField(default=0, blank=True)
    short_intro = models.CharField(null=True, blank=True, max_length=1000)
    bio = models.TextField(null=True, blank=True, max_length=2000)
    website = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    def __str__(self):
        return str(self.username)
