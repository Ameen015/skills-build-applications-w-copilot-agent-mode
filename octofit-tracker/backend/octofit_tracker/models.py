from django.db import models

# User, Team, Activity, Leaderboard, Workout models for MongoDB
class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add more fields as needed

class Team(models.Model):
    team_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)
    # Add more fields as needed

class Activity(models.Model):
    activity_id = models.CharField(max_length=100, unique=True)
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    timestamp = models.DateTimeField()
    # Add more fields as needed

class Leaderboard(models.Model):
    leaderboard_id = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    # Add more fields as needed

class Workout(models.Model):
    workout_id = models.CharField(max_length=100, unique=True)
    user = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    # Add more fields as needed
