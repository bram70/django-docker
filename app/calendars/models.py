from django.db import models

class Appointment(models.Model):
    title = models.CharField(max_length=200, default='')
    start = models.DateTimeField('date started')
    end = models.DateTimeField('date finished')
    description = models.TextField('description')
    status = models.IntegerField(default=0)
#    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('calendars:detail', args=[self.id])
