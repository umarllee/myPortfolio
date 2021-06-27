from django.db import models

class filedownload(models.Model):
    fileupload=models.FileField(upload_to='media')

    def __str__(self):
        return self.fileupload