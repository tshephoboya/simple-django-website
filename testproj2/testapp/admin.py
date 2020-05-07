from django.contrib import admin
from testapp.models import *

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

# Register your models here.
