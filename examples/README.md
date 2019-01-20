step #1 - generate an unconfigged feeder config:

../tvm802-mdgen.py -i fst-01-top-pos.csv -g -f feeders-unconfigged.csv

step #2 - edit the config

for each uniqe componente add the actual feeder, nozzle to use, speed and
height

step #3 - generate machine data

../tvm802-mdgen.py -i fst-01-top-pos.csv -f feeders-configged.csv -o tvm802-md.csv

step #4 - upload data file to machine

... and watch it perform :-)
