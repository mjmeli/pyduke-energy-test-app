import aiohttp
from datetime import datetime, timedelta
import jsonpickle
import pytz

from pyduke_energy.client import DukeEnergyClient

def append(org: str, to_append: str):
    """ Append to string with two line breaks between """
    return (org + "\n\n" + to_append).strip()

def append_json(org: str, prefix: str, obj):
    """ Append json with two line breaks between """
    return append(org, (prefix + "\n" + jsonpickle.encode(obj, indent=4, unpicklable=False)).strip())

async def get_data(email: str, password: str, timezone: str):
    """ Get data from the API and concat into a string for display """
    async with aiohttp.ClientSession() as client:
        response = ""

        duke_energy = DukeEnergyClient(email, password, client)

        # Get account list
        account_list = await duke_energy.get_account_list()
        account = account_list[0] # just use first for now
        response = append_json(response, "ACCOUNT:", account)

        # Get account details
        account_details = await duke_energy.get_account_details(account)
        response = append_json(response, "ACCOUNT DETAILS:", account_details)

        # Get meter
        meter, gateway = await duke_energy.select_default_meter()
        response = append_json(response, "METER:", meter)
        response = append_json(response, "GATEWAY:", gateway)

        # Last today usage
        tz_info = pytz.timezone(timezone)
        today = datetime.now(tz_info)
        today_start = datetime(today.year, today.month, today.day, 0, 0, 0, 0, tz_info)
        today_end = today_start + timedelta(days=1)
        gw_usage = await duke_energy.get_gateway_usage(today_start, today_end)
        today_usage = sum(x.usage for x in gw_usage)
        response = append(response, "TODAY USAGE:\n" + f"From {gw_usage[0].datetime_utc.astimezone(tz_info)} to {gw_usage[-1].datetime_utc.astimezone(tz_info)}: {today_usage} W ({len(gw_usage)} measurements)")

        return response
