from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(user_id='u1', name='Test User', email='test@example.com')
        self.assertEqual(user.name, 'Test User')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(team_id='t1', name='Test Team', members=[])
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(activity_id='a1', user='u1', type='run', duration=30, timestamp='2025-11-19T00:00:00Z')
        self.assertEqual(activity.type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(leaderboard_id='l1', team='t1', score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(workout_id='w1', user='u1', description='Pushups', date='2025-11-19')
        self.assertEqual(workout.description, 'Pushups')
