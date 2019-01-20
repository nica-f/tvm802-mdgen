#!/usr/bin/python3

# tvm802-mdgen - TVM802 pick and place machine data generator from KiCad POS files

# Copyright (C) 2019 Nicole Faerber
# License: GNU General Public License v3.0 or later
# License: GPL-3.0+
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

import sys
import getopt
import csv

verbose = False

def gen_components_list (filename):
    ""
    # array to hold individual components use in the project
    components = []
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        firstline = True
        for row in readCSV:
            # first line contains column headers, skip it
            if firstline:
                firstline = False
                continue
            package = row[2]
            val = row[1]
            components.append(package + ' ' + val)
        components = sorted(set(components))
        return components

def read_feeder_component_mappings (filename):
    ""
    cfeeders = {}
    firstline = True
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # first line contains column headers, skip it
            if firstline:
                firstline = False
                continue
            cfeeders[row[0]] = [ row[1], row[2], row[3], row[4] ]
    csvfile.close()
    return cfeeders

def map_components_feeders (pos_filename, cfeeders):
    ""
    with open(pos_filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        firstline = True
        for row in readCSV:
            # first line contains column headers, skip it
            if firstline:
                firstline = False
                continue
            component = row[2] + ' ' + row[1]
            try:
                print (cfeeders[component])
            except KeyError:
                print ('')
    csvfile.close()
    return

def gen_machine_data (pos_filename, cfeeders, output_file):
    ""
    with open(pos_filename) as csvfile:
        with open(output_file, 'w') as outfile:
            outfile.write('"Designator","NozzleNum","StackNum","Mid X","Mid Y","Rotation","Height","Speed","Vision","Pressure","Explanation"\n')
            readCSV = csv.reader(csvfile, delimiter=',')
            firstline = True
            for row in readCSV:
                # first line contains column headers, skip it
                if firstline:
                    firstline = False
                    continue
                component = row[2] + ' ' + row[1]
                # designator
                outfile.write('"' + row[0] + '",')
                # nozzle number (NozzleNum)
                try:
                    outfile.write('"' + cfeeders[component][1] + '",')
                except KeyError:
                    outfile.write('"",')
                # feeder (aka StackNum)
                try:
                    outfile.write('"' + cfeeders[component][0] + '",')
                except KeyError:
                    outfile.write('"",')
                # PosX (Mid X)
                outfile.write('"' + row[3] + '",')
                # PosY (Mid Y)
                outfile.write('"' + row[4] + '",')
                # Rot (Rotation)
                outfile.write('"' + row[5] + '",')
                # Height
                try:
                    outfile.write('"' + cfeeders[component][3] + '",')
                except KeyError:
                    outfile.write('"",')
                # Speed
                try:
                    outfile.write('"' + cfeeders[component][2] + '",')
                except KeyError:
                    outfile.write('"",')
                # Speed
                outfile.write('"' + row[4] + '",')
                # Vision
                outfile.write('"' + "None" + '",')
                # Pressure
                outfile.write('"' + "True" + '",')
                # Explanation
                outfile.write('"' + component + '"')
                outfile.write('\n')
            outfile.close()
        csvfile.close()
    return


def usage():
    ""
    print ('Usage:')
    print ('  -h, --help                   print this help')
    print ('  -v, --verbose                be verbose')
    print ('  -i <file>, --input=<file>    KiCad POS CSV iput file')
    print ('  -f <file>, --feeders=<file>  feeders CSV config file')
    print ('  -g, --gen_feeders            generate template feeders file,')
    print ('                               requires -i and -f, will overwrite feeders file')
    print ('  -o <file>, --output=<file>   TVM802 machine data output file')
    return

def main(argv):
    ""
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'i:o:f:ghv', ['input=',
            'output=', 'feeders=', 'gen_feeders', 'help', 'verbose', ])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    global verbose
    input_filename = ''
    output_filename = ''
    feeders_filename = ''
    gen_feeders = False

    for opt, arg in options:
        if opt in ('-o', '--output'):
            output_filename = arg
        elif opt in ('-i', '--input'):
            input_filename = arg
        elif opt in ('-f', '--feeder'):
            feeders_filename = arg
        elif opt in ('-g', '--gen_feeders'):
            gen_feeders = True
        elif opt in ('-h', '--help'):
            usage()
            sys.exit(0)
        elif opt in ('-v', '--verbose'):
            verbose = True
        else:
            assert False, "unhandled option"

    if (verbose):
        print ('input        :', input_filename)
        print ('output       :', output_filename)
        print ('feeders      :', feeders_filename)
        print ('gen feeders? :', gen_feeders)
        # print ('opts remain  :', remainder)

    if (gen_feeders):
        if (feeders_filename == ''):
            print("Feeders file missing.")
            usage()
            sys.exit(2);
        components = gen_components_list(input_filename)
        with open(feeders_filename,'w') as resultFile:
            resultFile.write('"Component","Feeder","Nozzle","Speed","Height"\n')
            for i in range(0, len(components)):
                resultFile.write('"' + components[i] + '"' + ',"","1/2","100","0.5"\n')
        resultFile.close()
        sys.exit(0)

    if (input_filename != '' and output_filename != '' and feeders_filename != ''):
        cfeeders = read_feeder_component_mappings(feeders_filename)
        gen_machine_data (input_filename, cfeeders, output_filename)
        sys.exit(0)

    usage()
    sys.exit(2)


if __name__ == '__main__':
    main(sys.argv)
