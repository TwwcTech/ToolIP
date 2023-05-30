import requests
import pandas as pd
from typing_extensions import LiteralString

__author__ = "twwch.tech"
__version__ = "1.0"


class ProcessIP:
    def __init__(self, url: LiteralString) -> None:
        self.url = url

    def getinfo_andfomat(self) -> pd.DataFrame:
        info: dict = requests.get(url=self.url).json()
        format_frame: dict = {
            "IP": f"{info['ip']}",
            "Country": f"{info['country']} ({info['country_iso']})",
            "Region": f"{info['region_name']} ({info['region_code']})",
            "ZipCode": f"{info['zip_code']} ({info['city']})",
            "Coordinates": f"{info['latitude']}, {info['longitude']}",
            "TimeZone": f"{info['time_zone']}",
            "ISP": f"{info['asn_org']}"
        }
        pd.set_option("display.max_columns", None)
        return (pd.Series(
            data=format_frame,
            index=[
                "IP", "Country", "Region", "ZipCode",
                "Coordinates", "TimeZone", "ISP"
            ]
        ))
