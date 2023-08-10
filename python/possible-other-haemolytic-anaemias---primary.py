# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"103151.0","system":"med"},{"code":"103252.0","system":"med"},{"code":"14698.0","system":"med"},{"code":"1529.0","system":"med"},{"code":"18631.0","system":"med"},{"code":"21335.0","system":"med"},{"code":"31462.0","system":"med"},{"code":"3326.0","system":"med"},{"code":"39456.0","system":"med"},{"code":"39967.0","system":"med"},{"code":"45935.0","system":"med"},{"code":"57897.0","system":"med"},{"code":"70762.0","system":"med"},{"code":"72721.0","system":"med"},{"code":"87112.0","system":"med"},{"code":"94214.0","system":"med"},{"code":"99308.0","system":"med"},{"code":"99917.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-haemolytic-anaemias-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["possible-other-haemolytic-anaemias---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["possible-other-haemolytic-anaemias---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["possible-other-haemolytic-anaemias---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
