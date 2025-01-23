from django.db import models


class EntryPassword(models.Model):
    website_name = models.CharField(max_length=100)
    website_url = models.URLField(max_length=255)

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.website_url}"
