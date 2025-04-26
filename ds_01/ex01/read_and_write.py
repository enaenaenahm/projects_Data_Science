def read_and_write():
    with open('ds.csv', 'r') as csv:
        lines = csv.readlines()
    with open('ds.tsv', 'w') as tsv:
        for line in lines:
            tsv.write(line.replace(',', '\t'))

if __name__ == '__main__':
    read_and_write()