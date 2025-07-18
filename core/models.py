from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return self.name

class Link(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class TradeLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)