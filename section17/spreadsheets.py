import csv

# Open the file
data = open('example.csv', encoding='utf-8') # this specific encoding is neccessary because in file there are mails with @ and python doesn't know by default how to read

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object: list of lists
data_lines = list(csv_data)

print(len(data_lines)) # 1001 = 1 column names + 1000 entries

for line in data_lines[:5]:
    print(line)

all_emails = []

for line in data_lines[1:15]:
    all_emails.append(line[3]) # email column

print(all_emails)

full_names = []

for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])

print(full_names)

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
file_to_output.close()

f = open('to_save_file.csv', mode='a', newline='') # mode='a' for append(not overwrite)
csv_writer = csv.writer(f)
csv_writer.writerow(['11', '12', '13'])
f.close()