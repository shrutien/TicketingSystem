from django.db import models

# Create your models here.


ISSUE_TYPES = (
    ("STORY", "story"),
    ("TASK", "task"),
    ("BUG", "bug"),
)
class Project(models.Model):
    project_name = models.CharField(max_length=300)
    issue_type = models.CharField(max_length=300, choices=ISSUE_TYPES, default='STORY')
    description = models.TextField()
    label = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "ticket_site"

    def __str__(self):
        return u'{0}'.format(self.project_name)


class Ticket(models.Model):
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE)







