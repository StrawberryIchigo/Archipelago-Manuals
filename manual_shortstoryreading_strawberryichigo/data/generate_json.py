# Generates the relevant json files for manual to work
import csv
import json

# Converts the sources csv to an items json
def sources_to_items(csv_file):
    output = []
    for row in csv_file:
        item = {'count': row['Count'], 'name': row['Name'], 'category':[row['Category']], row['Classification']: True}
        output.append(item)

    with open('items.json','w') as json_items:
        json_items.write(json.dumps(output))

def generate_locations():
    output = []
    for difficulty in ['Easy', 'Medium', 'Hard']:
        for i in range(1, 101):
            plural = 'ies'
            if i == 1:
                plural = 'y'
            item = {'name': f'{i} {difficulty} Stor{plural}', 'region': 'Main', 'category':[difficulty]}
            output.append(item)

    with open('locations.json', 'w') as json_locs:
        json_locs.write(json.dumps(output))

# def generate_regions():


if __name__ == "__main__":
    with open('sources.csv', newline='') as csv_sources:
        sources_reader = csv.DictReader(csv_sources)
        sources_to_items(sources_reader)

    generate_locations()