import os
import csv
import random
from shapely.wkt import loads

list = []


class Area:

    def __init__(self, id, name, points):
        self.id = id
        self.name = name
        self.polygon = polygon_from_string(points)
        self.costToAreas = {}

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'polygon': self.polygon.to_wkt(),
            'costToAreas': self.costToAreas
        }


def load():
    path = os.path.dirname(os.path.abspath(__file__)) + '/data.csv'
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            a = Area(row[0], row[1], row[2])
            list.append(a)
    init_costs()


def init_costs():
    total = len(list)
    for fromIdx, fromArea in enumerate(list):
        for toIdx in range(0, total):
            if toIdx != fromIdx:
                fromArea.costToAreas[list[toIdx].id] = random.randint(10, 100)


def polygon_from_string(points_string):
    points_string = points_string.replace('(', '').replace(')', '').replace(',', ' ')
    points = points_string.split(';')
    points.append(points[0])
    return loads('POLYGON ((' + ', '.join(points) + '))')