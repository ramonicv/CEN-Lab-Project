from django.db import models

class GameSession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    player_data = models.TextField(help_text="Stores the player names as a JSON string") # for debug purposes, can be changed to a more structured format later

    def __str__(self):
        return f"Session at {self.created_at}"

# Create your models here.
