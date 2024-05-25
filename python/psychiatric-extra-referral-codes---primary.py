# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Jonathan Green, Carolyn A Chew-Graham, Nav Kapur, Darren M Aschcroft, 2024.

import sys, csv, re

codes = [{"code":"8H23000","system":"readv2"},{"code":"8H4f.00","system":"readv2"},{"code":"ZL5B400","system":"readv2"},{"code":"8HlB.00","system":"readv2"},{"code":"ZL5B500","system":"readv2"},{"code":"8HJ3.00","system":"readv2"},{"code":"8H49.00","system":"readv2"},{"code":"ZL5B.00","system":"readv2"},{"code":"ZL5B300","system":"readv2"},{"code":"8H23.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('extra-referral-codes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["psychiatric-extra-referral-codes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["psychiatric-extra-referral-codes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["psychiatric-extra-referral-codes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
