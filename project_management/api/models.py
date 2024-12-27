from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "projects"


class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'), 
        ('Member', 'Member')
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    class Meta:
        db_table = "project_members"


# class Task(models.Model):
#     STATUS_CHOICES = [
#         ('To Do', 'To Do'),
#         ('In Progress', 'In Progress'),
#         ('Done', 'Done')
#     ]
#     PRIORITY_CHOICES = [
#         ('Low', 'Low'), 
#         ('Medium', 'Medium'),
#         ('High', 'High')
#     ]
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
#     assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     due_date = models.DateTimeField()
    
#     class Meta:
#         db_table = "tasks"


# class Comment(models.Model):   
#     content = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         db_table = "comments"
        