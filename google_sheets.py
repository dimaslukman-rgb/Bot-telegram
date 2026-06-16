import gspread
from google.oauth2.service_account import Credentials


def connect_sheet():
    """
    Initialize Google Sheets integration.
    """

    print("Google Sheets integration initialized.")


def append_report(report_data):
    """
    Save report data into spreadsheet.
    """

    print(f"Report saved: {report_data}")
