from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ['-level', 'name']

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    tags = models.CharField(max_length=200, blank=True, help_text='Comma separated')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]
    

class Resume(models.Model):
    title = models.CharField(max_length=200, default='My Resume')
    resume = models.FileField(upload_to='resume_file/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Images(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profile_pic/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

