from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Drop collections directly for Djongo compatibility
        from django.db import connection
        db = connection.cursor().db_conn
        for collection in ['octofit_tracker_user', 'octofit_tracker_team', 'octofit_tracker_activity', 'octofit_tracker_leaderboard', 'octofit_tracker_workout']:
            try:
                db.drop_collection(collection)
            except Exception:
                pass

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
        Workout.objects.create(name='Speed Run', description='Speed workout for heroes')

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with test data'))
