from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'This is more complex command !'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='pass user name')



    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hi {name}, Welcome this testing environment !!'
        self.stdout.write(greeting + ' normal printing')  
        self.stderr.write(greeting + ' error printing') 
        
        self.stdout.write(self.style.SUCCESS(greeting + " success!!"))
        self.stdout.write(self.style.WARNING(greeting + " warning printing!"))
