"""
Anonymizer for Django json fixtures using Faker.

First be sure fake factory is installed:
`pip install Faker`

Usage: `python anonymizer.py <fixture>`

Where <fixture> is the path to the JSON fixture you wish to anonymize.

Two files will be created in the same directory:

* replacements.txt is a list of the original values and what they were replaced with. 
  This can be used in subsequent migrations

"""
import json
import random
import sys

from collections import defaultdict
from faker import Faker

fake = Faker()
Faker.seed(0)


def anonymize_json(source, target=None):
    """
    Reads a given source file and anonymized a given list of field names.

    The source argument is a path to a CSV file containing data to anonymize,
    while the optional target arg is a path to write the anonymized CSV data to.
    """
    # We'll populate REPLACEMENTS with the values we replaced and what we replaced it with
    REPLACEMENTS = {}
    # Seed words for more realistic org names. 
    # We have an empty string so some results are randomized with none of the above.
    FS_WORDS = ['', ' Nature Center', ' State University', ' Parks and Recreation Department', ' Parks', ' Training Center', ' County Parks', ' Survey Region']
    # For a given field, how do we want to replace it?
    # We'll eval() these functions later, which is generally not advisable but
    # in this case, with no user input and as a one-time thing, it should be OK.

    REPLACEMENT_FUNCTIONS = {
        'proj_title': 'fake.catch_phrase().upper() + random.choice(FS_WORDS).upper()',
        'created_by': 'fake.first_name()[0] + fake.last_name().upper()', 
        'modified_by': 'fake.first_name()[0] + fake.last_name().upper()',
        'comments': 'fake.paragraph(nb_sentences=1).upper()',
        'applicant_name': 'fake.company().upper() + random.choice(FS_WORDS).upper()',
        'authority_desc': 'fake.paragraph(nb_sentences=1)',
    }

    print('attempting to read source: %s' % str(source))
    f = open(source[0], "r") # because I'm passing args as a list
    data_list = json.loads(f.read())
    new_data_list = []
    for data_dict in data_list:
        for key, original_value in data_dict['fields'].items():
            #check to see if it's a field we want to replace and isn't None
            if key in REPLACEMENT_FUNCTIONS.keys() and original_value: 
                # if the value isn't in replacements already, build it
                if original_value not in REPLACEMENTS.keys():
                    replacement = eval(REPLACEMENT_FUNCTIONS[key])
                    REPLACEMENTS[original_value] = replacement
                print('replacing', original_value)
                data_dict['fields'][key] = REPLACEMENTS[original_value]
                print('with', data_dict['fields'][key])
        new_data_list.append(data_dict)
    # Output our replacements file

    fixture_file = open(str(source[0]) +'_mod.txt', "w")
    fixture_file.write(str(new_data_list))
    fixture_file.close()

if __name__ == "__main__":
   anonymize_json(sys.argv[1:])