from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class login(models.Model):
    Name = models.CharField(max_length=50, primary_key=True, unique=True)
    id = models.IntegerField(auto_created=True, unique=True)
    uName = models.CharField(max_length=15, unique=True)
    uPassword = models.CharField(max_length=15)
    

    def __str__(self):
        return self.Name

class taluka(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class village(models.Model):
    villageName = models.CharField(primary_key=True, max_length=100, unique=True)
    taluka = models.ForeignKey(taluka, default=1, on_delete=models.SET_DEFAULT)  
    def __str__(self):
        return self.villageName
    class Meta: 
        db_table = 'village'
        # Add verbose name 
        verbose_name = 'Village List'

class visitHistory(models.Model):    
    entry_by = models.ForeignKey('login', on_delete=models.DO_NOTHING)
    villageName = models.ForeignKey('village', on_delete=models.DO_NOTHING)
    visit_name = models.CharField(max_length=70)
    visit_date = models.CharField(max_length=70)
    visit_reason = models.CharField(max_length=200)
    visit_to_be = models.CharField(max_length=200)
    visit_contact = models.CharField(max_length=100)
    visit_help = models.CharField(max_length=200)
    visit_remark = models.CharField(max_length=200)

    def __str__(self):
        return self.visit_date
