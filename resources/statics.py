from datetime import datetime
from typing_extensions import LiteralString


class SysVariables:
    TIMESTAMP: str = datetime.today().time().isoformat(timespec="minutes")
    DATESTAMP: str = datetime.today().date().strftime("%m%d%Y")


class ToolIPVariables:
    URL: LiteralString = "https://ifconfig.co/json"


class ConsoleResponses:
    KBI: str = "Program stopped: 'Ctrl+C' was pressed."
    BADENTRY: str = "Not an option please, choose an option [1-2]"
    CONTINUE: str = "\n\nPress 'Enter' to continue"
