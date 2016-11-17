import numpy
from math import log10

def naive_bayes(infile, outfile, tests, labels, *attributes):
    read = open(infile, 'r')
    write = open(outfile, 'w')

    total_labels = [0] * len(labels)

    result = [1] * len(labels)

    tables = []

    for attribute in attributes:
        matrix = numpy.ones((len(attribute), len(labels)))
        tables.append(matrix)

    lines = read.read().splitlines()
    
    for line in lines:
        values = line.split(',')
        for idx, value in enumerate(values[:-1]):
            tables[idx][attributes[idx][value]][labels[values[-1]]] += 1
        total_labels[labels[values[-1]]] += 1
        
    total = sum(total_labels)

    #print(total_labels)
    #print(total)

    for table in tables:
        for idx, value in enumerate(table.T):
            value /= total_labels[idx]
        #table = log10(table)

    for test in tests:
        for idx, label in enumerate(labels):
            result[idx] = total_labels[idx] / total
            for idy, table in enumerate(tables):
                result[idx] *= table[attributes[idy][test[idy]]][idx]
        write.write(','.join(test)+','+list(labels.keys())[list(labels.values()).index(result.index(max(result)))]+'\n')

    #print(tables)

    #print(result)


file = 'car.data'
outfile = 'car.out.data'
file_test = 'car-prueba.data'

test1 = []
read = open(file_test, 'r')
lines = read.read().splitlines()
for line in lines:
    values = line.split(',')
    test1.append(values)
    
read.close()
    
class_values1 = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
buying = {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}
maint = {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}
doors = {'2': 0, '3': 1, '4': 2, '5more': 3}
persons = {'2': 0, '4': 1, 'more': 2}
lug_boot = {'small':0, 'med': 1, 'big': 2}
safety = {'low': 0, 'med': 1, 'high': 2}

naive_bayes(file, outfile, test1, class_values1, buying, maint, doors, persons, lug_boot, safety)


