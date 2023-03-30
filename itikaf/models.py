from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mosque(models.Model):
    name = models.CharField(max_length=250)
    lga = models.CharField(max_length=50)
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
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    id_type = models.CharField(max_length=50)
    id_card_no = models.CharField(max_length=20)
    id_image = models.ImageField(null=True, blank=True, upload_to="id_images/")
    photo = models.ImageField(null=True, blank=True, upload_to="profile_images/")
    added_by = models.ForeignKey(MosqueAdmin, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} - {self.mosque}'

class Approval(models.Model):
    participant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    approved = models.CharField(max_length=30, default='Disapproved')
    approved_by = models.ForeignKey(MosqueAdmin, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.approved

class CheckIn(models.Model):
    participant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    check_in = models.CharField(max_length=30, null=True)
    approved_by = models.ForeignKey(MosqueAdmin, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.check_in

class CheckOut(models.Model):
    participant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    check_out = models.CharField(max_length=30, null=True)
    approved_by = models.ForeignKey(MosqueAdmin, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.check_out

class Comment(models.Model):
    participant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    additional_info = models.CharField(max_length=30, null=True)
    approved_by = models.ForeignKey(MosqueAdmin, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.additional_info