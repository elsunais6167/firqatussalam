from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lga(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Mosque(models.Model):
    name = models.CharField(max_length=250)
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=300)
    accepting_applications = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.lga}'

class MosqueAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Applicant(models.Model):
    mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_phone = models.CharField(max_length=20)
    medical_condition = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    id_card_no = models.CharField(max_length=20)
    id_image = models.ImageField()
    photo = models.ImageField()
    added_by = models.ForeignKey(MosqueAdmin, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} - {self.mosque}'

class Processing(models.Model):
    participant = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    check_in = models.DateField(blank=True)
    check_out = models.DateField(blank=True)
    additional_info = models.TextField(blank=True)
    approved_by = models.ForeignKey(MosqueAdmin, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.participant