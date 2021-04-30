import csv

import click
import os

from echis_web import ROOT_DIR
from echis_web.model.filter_model import FilterModel


@click.command("import-words-from-csv")
@click.argument("file_name")
def import_words_from_csv_command(file_name):
    """
    Import worlds form csv file
    :param file_name:
    :return:
    """
    path = os.path.join(ROOT_DIR / f"import/{file_name}")
    if not os.path.exists(path) and not file_name.lower().endswith('.csv'):
        return click.echo("File not exists")
    try:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for i in row:
                    if not FilterModel.objects(name=i.strip()).count():
                        fil = FilterModel(name=i.strip())
                        fil.save()
                        print(f"Word '{i}' has been added")
        click.echo("Success, words has been imported")
    except Exception as e:
        raise Exception(e)
