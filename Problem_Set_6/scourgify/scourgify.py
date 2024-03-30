import sys, csv

if len(sys.argv) == 3 and sys.argv[1].endswith('.csv'):
    try:
        with open(sys.argv[1],'r') as input_file:
            reader = csv.DictReader(input_file)
            with open(sys.argv[2],'w') as output_file:
                writer = csv.DictWriter(output_file, fieldnames= ['first','last','house'])
                writer.writeheader()
                for row in reader:
                    l_name, f_name = row['name'].split(',')
                    writer.writerow({'first':f_name.lstrip(),'last':l_name,'house':row['house']})
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
else:
    sys.exit('Not a CSV file')