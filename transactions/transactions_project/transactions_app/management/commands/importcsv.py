import os.path
import csv
import datetime

from django.core.management.base import BaseCommand, CommandError
from transactions_app.models import Transaction


class Command(BaseCommand):
    help = 'Import transactions from a CSV file, optionally delete all previous records from DB'

    def add_arguments(self, parser):
        # required args
        parser.add_argument('csvfile', type=str)

        # optional args (starts with --)
        parser.add_argument('--empty_db', action='store_true')

    def handle(self, *args, **options):
        if 'empty_db' in options and options['empty_db'] is True:
            print("WARNING: Deleting all rows in database before import!!!")
            # Transaction.objects.all().delete()

        csv_file_path = options['csvfile']

        # check if the path is correct, is it a file???
        if not os.path.isfile(csv_file_path):
            print(f"ERROR: File {csv_file_path} does not exist")

        # open the file using CSV reader (python docs)
        with open(csv_file_path, newline='') as file:
            reader = csv.DictReader(file)
            # iterate for each row
            for row in reader:
                # read row, create new model object instance and save
                transcation = Transaction()
                transcation.transaction_date = datetime.datetime.strptime(row['Transaction Date'], "%m/%d/%Y").strftime("%Y-%m-%d")
                transcation.post_date = datetime.datetime.strptime(row['Post Date'], "%m/%d/%Y").strftime("%Y-%m-%d")
                transcation.description = row['Description']
                transcation.category = row['Category']
                transcation.transaction_type = row['Type']
                transcation.amount = row['Amount']

                print(f"Importing: {transcation}")
                transcation.save()
        # done
