from django.db import models

class file_Upload(models.Model):
    three_choices = (
        ('Form', 'Form'),
        ('Table', 'Table(key-value)'),
        ('Text', 'Text(line-by-line)'),
    )
    profile_image = models.ImageField(null=True, blank=True, upload_to='', default='profiles/user-default.png')
    choice = models.CharField(max_length=10,null=True, blank=True, choices=three_choices)
    

    def __str__(self):
        return self.choice

