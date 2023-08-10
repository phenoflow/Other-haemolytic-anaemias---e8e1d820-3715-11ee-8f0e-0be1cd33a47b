# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"D1...00","system":"readv2"},{"code":"Dyu1.00","system":"readv2"},{"code":"100022.0","system":"med"},{"code":"100388.0","system":"med"},{"code":"104454.0","system":"med"},{"code":"107820.0","system":"med"},{"code":"110176.0","system":"med"},{"code":"15314.0","system":"med"},{"code":"21369.0","system":"med"},{"code":"22531.0","system":"med"},{"code":"26437.0","system":"med"},{"code":"27771.0","system":"med"},{"code":"28238.0","system":"med"},{"code":"29323.0","system":"med"},{"code":"29933.0","system":"med"},{"code":"31107.0","system":"med"},{"code":"31662.0","system":"med"},{"code":"31734.0","system":"med"},{"code":"31800.0","system":"med"},{"code":"32373.0","system":"med"},{"code":"35612.0","system":"med"},{"code":"3818.0","system":"med"},{"code":"38327.0","system":"med"},{"code":"39164.0","system":"med"},{"code":"39682.0","system":"med"},{"code":"39876.0","system":"med"},{"code":"39944.0","system":"med"},{"code":"40545.0","system":"med"},{"code":"43367.0","system":"med"},{"code":"44381.0","system":"med"},{"code":"45944.0","system":"med"},{"code":"46322.0","system":"med"},{"code":"47598.0","system":"med"},{"code":"48096.0","system":"med"},{"code":"49182.0","system":"med"},{"code":"49451.0","system":"med"},{"code":"49822.0","system":"med"},{"code":"50495.0","system":"med"},{"code":"52522.0","system":"med"},{"code":"5434.0","system":"med"},{"code":"55561.0","system":"med"},{"code":"57298.0","system":"med"},{"code":"57575.0","system":"med"},{"code":"61665.0","system":"med"},{"code":"63936.0","system":"med"},{"code":"64468.0","system":"med"},{"code":"64619.0","system":"med"},{"code":"67088.0","system":"med"},{"code":"71808.0","system":"med"},{"code":"7237.0","system":"med"},{"code":"7526.0","system":"med"},{"code":"7624.0","system":"med"},{"code":"91034.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-haemolytic-anaemias-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anaemias---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anaemias---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anaemias---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
