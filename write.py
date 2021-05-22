"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation',
                  'name', 'diameter_km', 'potentially_hazardous')
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(fieldnames)
        for row in results:
            row = [row.time, row.distance, row.velocity, row.neo.designation, 
                   row.neo.name, row.neo.diameter, row.neo.hazardous]
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is 
    a list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
   
    with open(filename, 'w') as f:
        out_result = []
        for approach in results:
            result = approach.serialize()
            result['neo'] = approach.neo.serialize_neo()
            out_result.append(result)
        json.dump(out_result, f, indent=4)