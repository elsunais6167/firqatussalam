from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Mosque)
admin.site.register(Applicant)
admin.site.register(MosqueAdmin)
admin.site.register(StateAdmin)
admin.site.register(Approval)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Comment)