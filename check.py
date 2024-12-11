<<<<<<< HEAD
import gspread
import json
from gspread import Client, Spreadsheet, Worksheet

from defs import read_tables, logginIssue

google_sheets = None
with open("table_path.txt", 'r', encoding="UTF-8") as google_sheets:
        google_sheets = google_sheets.read()
        print(google_sheets)

SPREADSHEET_URL = google_sheets

def main():
    logIssue = logginIssue.CredentialsManager("./logginIssue.json")
    print(logIssue)
    tables = False
    drive = False
    service_account = None
    with open("service_account.txt", 'r', encoding="UTF-8") as service_account:
        service_account = service_account.read() + "\\service_account.json"
        print(service_account)
    try:
        gc: Client = gspread.service_account(service_account)
        sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
        tables = True
    except FileNotFoundError as e:
        tables = False
        print(e.args)
    except Exception as e:
        tables = False

    print(tables)

    try:
        file_name = read_tables.getFileName(sh)[1]
        print(file_name)
        photopath = None
        with open("photoPath.txt", 'r', encoding="UTF-8") as photofile:
            photopath = photofile.read() + "\\"
            print(photopath)
        file1 = f"{photopath}\\{file_name} (1).jpg"
        open(file1, 'r')
        drive = True
    except Exception as e:
        drive = False
    print(drive)


    if tables == False:
        tables = 0;
    else:
        tables = 1;
    if drive == False:
        drive = 0;
    else:
        drive = 1;

    data = {
        "tabels":tables,
        "drive":drive
    }

    with open('data.json','w') as file:
        json.dump(data,file,indent=4)



if __name__ == '__main__':
    main()


=======
import gspread
import json
from gspread import Client, Spreadsheet, Worksheet

from defs import read_tables, logginIssue

google_sheets = None
with open("table_path.txt", 'r', encoding="UTF-8") as google_sheets:
        google_sheets = google_sheets.read()
        print(google_sheets)

SPREADSHEET_URL = google_sheets

def main():
    logIssue = logginIssue.CredentialsManager("./logginIssue.json")
    print(logIssue)
    tables = False
    drive = False
    service_account = None
    with open("service_account.txt", 'r', encoding="UTF-8") as service_account:
        service_account = service_account.read() + "\\service_account.json"
        print(service_account)
    try:
        gc: Client = gspread.service_account(service_account)
        sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
        tables = True
    except FileNotFoundError as e:
        tables = False
        print(e.args)
    except Exception as e:
        tables = False

    print(tables)

    try:
        file_name = read_tables.getFileName(sh)[1]
        print(file_name)
        photopath = None
        with open("photoPath.txt", 'r', encoding="UTF-8") as photofile:
            photopath = photofile.read() + "\\"
            print(photopath)
        file1 = f"{photopath}\\{file_name} (1).jpg"
        open(file1, 'r')
        drive = True
    except Exception as e:
        drive = False
    print(drive)


    if tables == False:
        tables = 0;
    else:
        tables = 1;
    if drive == False:
        drive = 0;
    else:
        drive = 1;

    data = {
        "tabels":tables,
        "drive":drive
    }

    with open('data.json','w') as file:
        json.dump(data,file,indent=4)



if __name__ == '__main__':
    main()


>>>>>>> 623c4009141dd713f3bb3f4e4ec9dba8c53103b4
