import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Create test users
def create_users():
    User.objects.create(user_id='u1', name='Alice', email='alice@example.com')
    User.objects.create(user_id='u2', name='Bob', email='bob@example.com')
    User.objects.create(user_id='u3', name='Charlie', email='charlie@example.com')

# Create test teams
def create_teams():
    Team.objects.create(team_id='t1', name='Team Alpha', members=['u1', 'u2'])
    Team.objects.create(team_id='t2', name='Team Beta', members=['u3'])

# Create test activities
def create_activities():
    Activity.objects.create(activity_id='a1', user='u1', type='run', duration=30, timestamp='2025-11-19T08:00:00Z')
    Activity.objects.create(activity_id='a2', user='u2', type='cycle', duration=45, timestamp='2025-11-19T09:00:00Z')

# Create test leaderboard
def create_leaderboard():
    Leaderboard.objects.create(leaderboard_id='l1', team='t1', score=150)
    Leaderboard.objects.create(leaderboard_id='l2', team='t2', score=80)

# Create test workouts
def create_workouts():
    Workout.objects.create(workout_id='w1', user='u1', description='Pushups', date='2025-11-19')
    Workout.objects.create(workout_id='w2', user='u2', description='Squats', date='2025-11-19')

if __name__ == '__main__':
    create_users()
    create_teams()
    create_activities()
    create_leaderboard()
    create_workouts()
    print('Test data populated.')
