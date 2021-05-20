from django.db import models

# Create your models here.
class Notifications(models.Model):
    Comp_Id = models.ForeignKey('complaints.Complaints',db_column='Comp_Id', on_delete=models.CASCADE)
    Message = models.CharField(max_length=400)
    Message_By = models.ForeignKey('users.Users',db_column='Message_By' ,on_delete=models.CASCADE)
    class Meta:
        db_table = 'Notifications'