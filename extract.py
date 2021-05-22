"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
   
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            info = {}
            info['designation'] = row['pdes']
            if row['name']:
                info['name'] = row['name']
            else:
                info['name'] = None
            if row['diameter']:
                info['diameter'] = float(row['diameter'])
            else:
                info['diameter'] = float('nan')
            if row['pha'] == 'Y': 
                info['hazardous'] = True
            else:
                info['hazardous'] = False
                
            neo = NearEarthObject(**info)
            data.append(neo)
        
    return data


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
   
    with open(cad_json_path) as f:
        json_data = json.load(f)
        data = []
        for item in json_data['data']:
            info = {}
            info['designation'] = item[0]
            info['time'] = item[3]
            info['distance'] = float(item[4])
            info['velocity'] = float(item[7])
            
            co = CloseApproach(**info)
            data.append(co)
        
    return data

