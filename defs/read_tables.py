import gspread
from gspread import Client, Spreadsheet, Worksheet

with open("table_path.txt", 'r', encoding="UTF-8") as google_sheets:
    google_sheets = google_sheets.read()
    print(google_sheets)

SPREADSHEET_URL = google_sheets

def show_avalible_worksheets(sh: Spreadsheet):
    worksheet = sh.worksheets()
    print()
    for ws in worksheet:
        print(f"{ws}")

def main():
    service_account = None
    with open("service_account.txt", 'r', encoding="UTF-8") as service_account:
        service_account = service_account.read() + "\\service_account.json"
        print(service_account)
    gc: Client = gspread.service_account(service_account)
    sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
    return sh

def getFileName(sh):
    ws = sh.sheet1
    return ws.col_values(2)

def getFileDiscript(sh):
    ws = sh.sheet1
    return ws.col_values(4)

def getFilePrice(sh):
    ws = sh.sheet1
    return ws.col_values(3)
def getFileTags(sh):
    ws = sh.sheet1
    return ws.col_values(5)

def getCategory(sh):
    ws = sh.sheet1
    return ws.col_values(6)
def getSubCategory(sh):
    ws = sh.sheet1
    return ws.col_values(7)

def getGroup(sh):
    ws = sh.sheet1
    return ws.col_values(8)
def getEquipment(sh):
    ws = sh.sheet1
    return ws.col_values(9)

def getMaterial(sh):
    ws = sh.sheet1
    return ws.col_values(10)

def getOriginal(sh):
    ws = sh.sheet1
    return ws.col_values(11)

def getStatus(sh):
    ws = sh.sheet1
    return ws.col_values(12)

if __name__ == '__main__':
    main()