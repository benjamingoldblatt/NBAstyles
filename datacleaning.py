import csv
import string

input_file = open('playtype.csv', 'r')
output_file = open('playtype2.csv', 'w')
data = csv.reader(input_file)
writer = csv.writer(output_file,quoting=csv.QUOTE_ALL)# dialect='excel')
specials = '%'

for line in data:
    line = str(line)
    new_line = str.replace(line,specials,'')
    writer.writerow(new_line.split(','))

input_file.close()
output_file.close()