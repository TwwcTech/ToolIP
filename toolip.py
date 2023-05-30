from time import sleep
from cli.menu import mainmenu
from cli.conman import clearcon
from backend.processipinfo import ProcessIP
from resources.statics import SysVariables as sv
from resources.statics import ToolIPVariables as tipv
from resources.statics import ConsoleResponses as conr

__author__ = "twwc.tech"
__version__ = "1.0"

if __name__ == "__main__":
    try:
        while True:
            clearcon()
            mainmenu(title="Main Menu")
            option_input: str = input("Select an option: ")
            match option_input:
                case "1":
                    clearcon()
                    print(f"\nStart Time: {sv.DATESTAMP}, {sv.TIMESTAMP}\n")
                    print(
                        f"\n\n{ProcessIP(url=tipv.URL).getinfo_andfomat()}\n\n"
                    )
                    coninput: str = input(conr.CONTINUE)
                case "2": clearcon(), exit(0)
                case _: print(conr.BADENTRY), sleep(1.5)
    except KeyboardInterrupt:
        print(conr.KBI)
