# tvm802-mdgen
TVM802 pick and place machine data generator from KiCad POS files

This is my first Python hackery, so bare with me :-)

The intention of this project is to create a program to help with generating CSV machine dat afiles for the TVM802 pick and place machines, quite cheaply available from China, like this one (which is what I got myself recently):
http://www.qhsmt.com/tvm802bx/tvm802bx.html

The machine reads pretty simple text files which are almost self explanatory. The parts data is contained in CSV format first followed by configuration for the PCB setup (location and panelization) are well as config parameters for IC tray setup etc.

My idea was to create a script that takes input from KiCad and turns it into a machine data file with as little as possible manual intervention. Since a PCB project will most certainly contain the same component in many different places I wanted the program to assign the feeder slots automatically.

ATM the program will not output a fll machine data file, I am still working on the CSV in-and output. The idea is as follows:

From KiCad you generate the POS file for your project. Then you run the program once with it and the "-h" option to generate a parts list with feeder assignments. This list will contin only unique parts accoring to the component value and component package ("Val" and "Package" in the KiCad POS file). After this first step you can edit the generated file and assign a feeder slot, nozzle number to use for placing, speed and a component height to each uniqe component.

In the second step you can use the previously generated feeders file to process the KiCad POS file and generate a matching machine output, that will now automatcally assign the same feeder to the same components, along with the other parameters.

I hope this will save some time when setting up a project. I will add the machine setup footer to the generated file as soon as I have time :) The examples directory contains some example CSV files, generated for the FST-01 USB stick by Niibe Yutaka.


Usage:
  -h, --help                   print this help
  -v, --verbose                be verbose
  -i <file>, --input=<file>    KiCad POS CSV iput file
  -f <file>, --feeders=<file>  feeders CSV config file
  -g, --gen_feeders            generate template feeders file,
                               requires -i and -f, will overwrite feeders file
  -o <file>, --output=<file>   TVM802 machine data output file
