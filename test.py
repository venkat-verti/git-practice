import csv
import json


class TestClass(object):

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz

    def fizz_buzz(self, digit_1, digit_2):
        for i in range(1, 100):
            if i % digit_1 == 0:
                if i % digit_2 == 0:
                    print 'fizzbuzz!'
                else:
                    print 'fizz!'
            elif i % digit_2 == 0:
                print 'buzz!'
            else:
                print i

    ''' introducing new methods - read_csv() and csv2json() '''
    csv_file= 'inputfile.csv'
    json_file = 'outputfile.json'

    #read csv file
    def read_csv(cfile):
        rows = []
        with open(cfile) as cf:
            field = csv.DictReader(cf).fieldnames
            for row in csv.DictReader(cf):
                rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
            csv2json(rows, json_file)

    def json_to_csv(self, json_file_path, outfile_path):
        """Convert a file containing a list of flat JSON objects to a csv.

        What's a DictWriter, you say? Never heard of it!

        """
        with open(json_file_path) as f:
            data = json.load(f)
        with open(outfile_path, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
