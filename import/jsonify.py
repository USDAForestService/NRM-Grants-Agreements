import csv
import json
import sys


def make_json(args):
    """
    Pretty simple and somewhat naive script that =takes a `.xsv` file as an argument,
    converts it to JSON, and outputs it as a json file of the same name as the original csv.

    It can handle .csv or .tsv files.

    It does, however, make a lot of assumptions about the nature of the file and PKs,
    so... we'll see how well it works.
    """
    jsondata = [] 
    # convert from args list
    cvspath = args[0]
    with open(cvspath, encoding='utf-8', errors='replace') as csvf:
        if  cvspath.endswith('.tsv'):
            read_file = csv.DictReader(csvf, delimiter="\t")
        else:
            read_file = csv.DictReader(csvf)
        for row in read_file:
            jsondata.append(row)
 
        jsonpath = cvspath.rsplit('.')[0] + '.json'
        with open(jsonpath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(jsondata, indent=4))

if __name__ == "__main__":
   make_json(sys.argv[1:])