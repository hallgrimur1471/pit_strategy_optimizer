#!/usr/bin/env python3.7

# Standard library
import re
import pickle
from datetime import timedelta
from typing import Dict, Tuple, List, Any
import os.path
from os.path import dirname, abspath, join

# PyPi
from googleapiclient.discovery import build as google_service_build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def read_data(
    spreadsheet_url: str
) -> Tuple[Dict[str, List[timedelta]], Dict[str, Any]]:
    credentials = _authenticate_user()
    spreadsheet_id = _extract_spreadsheet_id(spreadsheet_url)
    return _read_data(spreadsheet_id, credentials)


def _authenticate_user():
    project_dir = dirname(dirname(abspath(__file__)))
    token_file = join(project_dir, ".token.pickle")
    credentials_file = join(project_dir, ".credentials.json")

    # print("Authenticating user ...")
    credentials = None
    # The file .token.pickle stores the user's access and refresh tokens, and
    # is created automatically when the authorization flow completes for the
    # first time.
    if os.path.exists(token_file):
        with open(token_file, "rb") as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, scopes
            )
            credentials = flow.run_local_server()
        # Save the credentials for the next run
        with open(token_file, "wb") as token:
            pickle.dump(credentials, token)
    return credentials


def _extract_spreadsheet_id(url: str) -> str:
    pattern = re.compile("^.+\/spreadsheets\/d\/([^\/]+)(\/.*)?$")
    match = re.match(pattern, url)
    if not match:
        raise RuntimeError(f"Could not read spreadsheet_id from url:{url}")
    return match.group(1)


def _read_data(
    spreadsheet_id: str, credentials: Credentials
) -> Tuple[Dict[str, List[timedelta]], Dict[str, Any]]:

    # print(f"Reading data from spreadsheet ...")

    service = google_service_build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets()
    data_range = "A1:G"
    result = (
        sheet.values()
        .get(spreadsheetId=spreadsheet_id, range=data_range)
        .execute()
    )
    data = result.get("values", [])

    lap_times = {
        "RH": [],
        "RM": [],
        "RS": [],
    }  # type: Dict[str, List[timedelta]]
    i = 0
    while data[i] != ["Lap", "RH", "", "RM", "", "RS"]:
        i += 1
    i += 1
    assert data[i] == ["", "min", "sec", "min", "sec", "min", "sec"]
    i += 1
    while len(data[i]) == 7:
        (m, s) = (int(data[i][1]), float(data[i][2]))
        lap_times["RH"].append(timedelta(minutes=m, seconds=s))
        (m, s) = (int(data[i][3]), float(data[i][4]))
        lap_times["RM"].append(timedelta(minutes=m, seconds=s))
        (m, s) = (int(data[i][5]), float(data[i][6]))
        lap_times["RS"].append(timedelta(minutes=m, seconds=s))
        i += 1

    extra_info = dict()  # type: Dict[str, Any]
    while (not data[i]) or data[i][0] != "average pit time [seconds]":
        i += 1
    extra_info["average_pit_time"] = int(data[i][1])
    while (not data[i]) or data[i][0] != "max laps per tank":
        i += 1
    extra_info["max_laps_per_tank"] = int(data[i][1])
    while (not data[i]) or data[i][0] != "laps in race":
        i += 1
    extra_info["laps_in_race"] = int(data[i][1])

    return (lap_times, extra_info)
