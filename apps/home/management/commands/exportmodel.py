from django.core.management.base import BaseCommand, CommandError
from apps.home import resources

class Command(BaseCommand):
    help = "Exports a csv file for db models"

    def add_arguments(self, parser):
        parser.add_argument("modelname")

    def handle(self, *args, **options):
        modelname = options["modelname"]
        print(modelname)
        match modelname:
            case 'Post':
                resource = resources.PostResource
            case 'Category':
                resource = resources.CategoryResource
            case 'User':
                resource = resources.UserResource
            case 'ShortLink':
                resource = resources.ShortLinkResource
            case _:
                raise CommandError('not a valid model')
        dataset = resource().export()
        with open(f'{modelname}sfile.csv','w') as file:
            file.write(dataset.csv)
