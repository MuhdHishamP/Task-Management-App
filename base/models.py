from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['complete']

class UserInvitation(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
    def send_invitation(self):
        invitation_link = "https://task-management-app-kappa-bay.vercel.app/"
        
        send_mail(
            subject='Invitation to use task app',
            message=f'This is an invitaion for to you use my new task app. Start using the app right away by clicking this link: {invitation_link}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email],
            fail_silently=False,
        )