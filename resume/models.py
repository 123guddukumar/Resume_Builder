from typing import Any
from django.db import models

class Resume(models.Model):
    # gender_choices = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    #     ('Transgender', 'Transgender'),
    #     ('Other', 'Other')
    # ]
    
    # Language = [
    #     ('Hindi','Hindi'),
    #     ('English','English'),
    #     ('Bhojpuri','Bhojpuri'),
    #     ('Urdu','Urdu'),
    #     ('Punjabi','Punjabi'),
    #     ('Mathali','Mathali'),
    #     ('Marathi','Marathi'),
    # ]
    
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=150, null=True)
    about = models.TextField(null=False, max_length=1500)
    image = models.ImageField(upload_to='images')
    email = models.EmailField(max_length=100)
    number = models.IntegerField(default=0)  # Set a default value
    github_link = models.URLField(blank=False, null=True)
    linkedin_link = models.URLField(blank=False, null=True)
    address = models.TextField(null=False )
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    developer = models.TextField(null=False )
    skills = models.TextField(null=True)  # Corrected typo in field name 'skils' to 'skills'
    language = models.CharField(max_length=20)
    summary = models.TextField(null=False )
    
    experience = models.TextField(null=False )  # Corrected typo in field name 'exprience' to 'experience'
    ex_job = models.TextField(null=False, default='developer')  # Corrected typo in field name 'exprience' to 'experience'
    start_job = models.DateField(default='2024-01-01')  # Set a default value
    end_job = models.DateField(default='2024-01-01')
    
    graduation = models.TextField(null=False, default='BBSBEC')       # Set a default value
    start_grad = models.DateField(default='2024-01-01')  # Set a default value
    end_grad = models.DateField(default='2024-01-01')
    grad_marks = models.TextField(null=False, default='88.5')
    
    inter = models.TextField(null=False, default="MJK college bettiah") # Set a default value
    start_inter = models.DateField(default='2024-01-01')  # Set a default value
    end_inter = models.DateField(default='2024-01-01')
    inter_marks = models.TextField(null=False, default='88.5')
    
    tenth = models.TextField(null=False, default='RDS')          # Set a default value
    start_ten = models.DateField(default='2024-01-01')  # Set a default value
    end_ten = models.DateField(default='2024-01-01')
    ten_marks = models.TextField(null=False, default='88.5')
    
    project = models.TextField(null=False)
    project_link = models.URLField(blank=True, null=True)
    project1 = models.TextField(null=True )
    project_link1 = models.URLField(blank=True, null=True)
    project2 = models.TextField(null=True )
    project_link2 = models.URLField(blank=True, null=True)
    
    hobbies = models.TextField(null=False )
    
    achievement = models.TextField(null=False )
    position = models.CharField(max_length=20,default="Gold", null=False)
    
    achievement1 = models.TextField(null=True)
    position1 = models.CharField(max_length=20,default="Gold",null=True)
    
    achievement2 = models.TextField(null=True )
    position2 = models.CharField(max_length=20,default="Gold", null=True)
    
    def __str__(self):
        return self.f_name
