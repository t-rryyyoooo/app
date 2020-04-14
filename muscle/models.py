from django.db import models

class Menu(models.Model):
    PARTS = (("chest", "胸"), ("shoulder", "肩"), ("arm", "腕"), ("leg", "足"), ("back", "背中"), ("abdomen", "腹"))
    name = models.CharField(max_length=20)
    part = models.CharField(max_length=8, choices=PARTS)

    def __str__(self):
        return self.name
