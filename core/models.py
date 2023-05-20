from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class Url(models.Model):
    original_url = models.URLField(validators=[URLValidator()])
    short_url_slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.short_url_slug}"
    
    def save(self, *args, **kwargs):
        if not self.short_url_slug:
            self.short_url_slug = slugify(get_random_string(length=15))
            while Url.objects.filter(short_url_slug=self.short_url_slug).exists():
                self.short_url_slug = slugify(get_random_string(length=15))
        super(Url, self).save(*args, **kwargs)



class CustomURLValidator(URLValidator):
    def __call__(self, value):
        if value and not value.startswith(('http://', 'https://')):
            value = f'http://{value}'

        super().__call__(value)

        parts = value.split('.')
        if len(parts) < 3 or not parts[-1]:
            raise ValidationError("Invalid URL")

