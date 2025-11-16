from django.db import models

class StatusChoices(models.TextChoices):
    NEW='new',"🟢 Yangi"
    IN_PROGRESS='in_progress','⏳ Jarayonda'
    DONE='done','✅ Bajarilgan'
    
class Todo(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    status=models.CharField(max_length=50,choices=StatusChoices,default=StatusChoices.NEW)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
