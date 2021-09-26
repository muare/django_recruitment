import csv
from django.core.management import BaseCommand
from interview.models import Candidate


class Command(BaseCommand):
    help = 'import candidates from csv files'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel', delimiter=',',)    
            next(reader)        
            for row in reader:
                print(row)
                candidate = Candidate.objects.create(
                    username=row[0],
                    city=row[1],
                    phone=row[2],
                    email=row[3],
                    major=row[4],
                    degree=row[5],
                    first_result=row[6],
                    first_interviewer=row[7],
                    second_result=row[8],
                    second_interviewer=row[9],
                    hr_result=row[10],
                    hr_interviewer=row[11]
                )
