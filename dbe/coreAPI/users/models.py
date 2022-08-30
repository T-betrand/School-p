from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=32)
    photo = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    balance = models.IntegerField(default=0)
    # wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class ServiceProvider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=32)
    photo = models.CharField(max_length=150)
    balance = models.IntegerField(default=0)
    # wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    skills = models.ForeignKey('Skills', on_delete=models.CASCADE, related_name="list_of_skills", blank=True, null=True)


class ServiceProviderHasSkills(models.Model):
    pass 


class Skills(models.Model): 
    skill_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('ServiceProvider', on_delete=models.CASCADE, related_name="skill_owner", blank=True, null=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    photo = models.CharField(max_length=100)

# class Photo(models.Model):
#     photo_id = models.AutoField(primary_key=True)
#     image_url = models.URLField()
#     owners_id = models.ForeignKey()
#     description = models.TextField()
#     alt_text = models.CharField()


# class Wallet(models.Model):
#     wallet_id = models.AutoField()
#     amount = models.IntegerField(default=0)

class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    service_providers_id = models.ForeignKey('ServiceProvider', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    job_cost = models.IntegerField(default=0)
