import csv
import json
import xmltodict


class WorkedData:
    @staticmethod
    def clean_csv(path: str):
        with open(path) as data:
            changed = csv.DictReader(data)
            listed_changed = list(changed)
        return listed_changed

    @staticmethod
    def clean_json(path: str):
        with open(path) as data:
            changed = data.read()
            listed_changed = list(json.loads(changed))
        return listed_changed

    @staticmethod
    def clean_xml(path: str):
        with open(path) as file:
            changed = xmltodict.parse(file.read())["dataset"]["record"]
        return changed
