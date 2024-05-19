from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class ReachOut(models.Model):
    ABOUT_CHOICES = [
        ('general', 'General Question'),
        ('order', 'About an order'),
        ('other', 'Something else'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_number = models.CharField(max_length=32, null=True, blank=True)
    about = models.CharField(max_length=10, choices=ABOUT_CHOICES)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
