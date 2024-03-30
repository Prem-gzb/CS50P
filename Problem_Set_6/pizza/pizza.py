import tabulate, sys, csv

if len(sys.argv) == 2 and sys.argv[1].endswith('.csv'):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate.tabulate(reader, headers = "keys", tablefmt='grid'))
    except FileNotFoundError:
        sys.exit('File does not exist')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif sys.argv[1].endswith != '.csv':
    sys.exit('Not a CSV file')