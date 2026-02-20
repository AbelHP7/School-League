import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tournament.models import Match

# Wipe all matches so we don't have duplicates from previous testing.
Match.objects.all().delete()
print("All previous duplicate matches have been deleted!")
