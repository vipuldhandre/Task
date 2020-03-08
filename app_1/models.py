from django.db import models
from django.contrib.auth.models import User


# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class UserProfile(models.Model):
    doc_name = models.CharField(max_length=60)
    doc_file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
