from django.db import models
from utils.models import BaseModel

class Network(BaseModel):
    name = models.CharField(max_length=20, help_text="name of the network")
    description = models.CharField(max_length=255, help_text="description of the network")
    type = models.CharField(max_length=10, help_text="type of the network")

    def __str__(self):
        return f"{self.name} - {self.description} - {self.type}"

    class Meta:
        db_table = "apps_networks"