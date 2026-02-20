import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def create_users():
    # Create Student
    if not User.objects.filter(username='abel').exists():
        user = User.objects.create_user(username='abel', password='abel', role='STUDENT')
        print("Usuario Alumno creado: abel / abel")
    else:
        print("El usuario 'abel' ya existe.")

    # Create Referee
    if not User.objects.filter(username='albitro').exists():
        user = User.objects.create_user(username='albitro', password='albitro', role='REFEREE')
        print("Usuario Árbitro creado: albitro / albitro")
    else:
        print("El usuario 'albitro' ya existe.")

if __name__ == '__main__':
    create_users()
