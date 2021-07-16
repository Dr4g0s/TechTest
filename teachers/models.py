from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from teachers.utils import read_csv_bulk



def restrict_amount(value):
    subjects_taught = value.split(',')
    if subjects_taught and len(subjects_taught) > 5:
        raise ValidationError("Teacher can't exceed maximal amount of subjects (5)")


class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='teachers/', default='default_image.jpg')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    subjects_taught = models.CharField(max_length=255, null=True, blank=True,
                        validators=(restrict_amount,), help_text="Enter subjects separated by comma (,)")

    def __str__(self):
        return self.email


class TeacherData(models.Model):
    csv_file = models.FileField(upload_to='files/', 
                validators=[FileExtensionValidator(allowed_extensions=['csv'])])

