from cli.conman import conpad


@conpad
def mainmenu(title: str):
    menuoptions: dict = {
        "1": "Get full IP info",
        "2": "Exit"
    }
    print(f"{'-'*5} {title} {'-'*5}")
    for num, options in menuoptions.items():
        print(f"{num} - {options}")
