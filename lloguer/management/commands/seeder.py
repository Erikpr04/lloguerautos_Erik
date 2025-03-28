import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva

class Command(BaseCommand):
    help = "Seed the database with random Automobiles, Users, and Reservations"

    def add_arguments(self, parser):
        # Añadir argumentos opcionales para definir el número de automóviles y usuarios a crear
        parser.add_argument('num_automobiles', type=int, help="Número de automóviles a crear", default=5)
        parser.add_argument('num_users', type=int, help="Número de usuarios a crear", default=5)

    def handle(self, *args, **options):
        num_automobiles = options['num_automobiles']
        num_users = options['num_users']

        # Crear Automóviles
        automobiles = []
        for i in range(num_automobiles):
            auto = Automobil.objects.create(
                marca=random.choice(["Toyota", "Ford", "BMW", "Audi", "Honda"]),
                model=f"Modelo-{i}",
                matricula=f"{random.randint(1000, 9999)}ABC"
            )
            automobiles.append(auto)

        # Crear Usuarios
        users = []
        for i in range(num_users):
            username = f"user{i}"

            # Verifica si el nombre de usuario ya existe
            while User.objects.filter(username=username).exists():
                username = f"user{random.randint(1000, 9999)}"

            user = User.objects.create_user(
                username=username,
                email=f"{username}@example.com",
                password="password"
            )
            users.append(user)

        # Crear Reservas (1 o 2 por usuario)
        for user in users:
            num_reservas = random.randint(1, 2)
            for _ in range(num_reservas):
                auto = random.choice(automobiles)
                data_inici = date.today() + timedelta(days=random.randint(1, 30))
                data_fi = data_inici + timedelta(days=random.randint(1, 5)) if random.choice([True, False]) else None

                if not Reserva.objects.filter(data_inici=data_inici, cotxe=auto).exists():
                    Reserva.objects.create(
                        data_inici=data_inici,
                        data_fi=data_fi,
                        cotxe=auto,
                        usuari=user
                    )

        self.stdout.write(self.style.SUCCESS(f"Se han creado {num_automobiles} automóviles, {num_users} usuarios y varias reservas."))
