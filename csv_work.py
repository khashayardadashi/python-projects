import csv
# For the average
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    averages = OrderedDict()
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            thesegrades = []
            for i in range(1, len(row)):
                thesegrades.append (float(row[i]))
            avg = mean(thesegrades)
            averages [row[0]] = avg
            
    with open (output_file_name, 'w') as out:
        count = 0
        for person in averages:
            count += 1
            if count == 1:
                out.write(person+ ","+ str(averages[person]))
            else:
                out.write("\n"+ person+ ","+ str(averages[person]))
            
        


def calculate_sorted_averages(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            thesegrades = []
            for i in range(1, len(row)):
                thesegrades.append (float(row[i]))
            avg = mean(thesegrades)
            averages [row[0]] = avg

    averagesordered = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))

    with open (output_file_name, 'w') as out:
        count = 0
        for person in averagesordered:
            count += 1
            if count == 1:
                out.write(person+ ","+ str(averagesordered[person]))
            else:
                out.write("\n"+ person+ ","+ str(averagesordered[person]))
    
        


def calculate_three_best(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            thesegrades = []
            for i in range(1, len(row)):
                thesegrades.append (float(row[i]))
            avg = mean(thesegrades)
            averages [row[0]] = avg

    averagesordered = OrderedDict (sorted (averages.items(), key=lambda x:(-x[1], x[0])))

    with open (output_file_name, 'w') as out:
        best = []
        for i in range (3):
            best_avg = averagesordered.popitem (last=False)
            best.append (best_avg)

        out.write (best[0][0]+","+str(best[0][1])+"\n")
        out.write (best[1][0]+","+str(best[1][1])+"\n")
        out.write (best[2][0]+","+str(best[2][1]))


def calculate_three_worst(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            thesegrades = []
            for i in range(1, len(row)):
                thesegrades.append (float(row[i]))
            avg = mean(thesegrades)
            averages [row[0]] = avg

    averagesordered = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))
    
    with open (output_file_name, 'w') as out:
        worst = []
        for i in range (3):
            worst_avg = averagesordered.popitem (last=False)
            worst.append (worst_avg)
            
        out.write (str(worst[0][1])+"\n")
        out.write (str(worst[1][1])+"\n")
        out.write (str(worst[2][1]))


def calculate_average_of_averages(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            thesegrades = []
            for i in range(1, len(row)):
                thesegrades.append (float(row[i]))
            avg = mean(thesegrades)
            averages [row[0]] = avg

    averagesordered = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))

    SUM = 0
    count = 0
    for average in averagesordered:
        count += 1
        SUM += float(averagesordered[average])

    avg_avg = SUM/count
    with open (output_file_name, 'w') as out:
        out.write(str(avg_avg))
