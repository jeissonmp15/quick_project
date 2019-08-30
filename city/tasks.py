import openpyxl
from background_task import background


# @background(schedule=1)
from city.models import City


def proccess_file(filename):
    document = openpyxl.load_workbook(filename, data_only=True)
    sheet = document.get_sheet_by_name('Hoja 1')

    cities = []
    for cont, row in enumerate(sheet.iter_rows(min_row=2)):
        cities.append(City(
            name=row[0].value.strip().capitalize(),
            code=row[0].value.strip()
        ))

    City.objects.bulk_create(cities)
