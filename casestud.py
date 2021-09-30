class TimeSheet(Exception):
    def __init__(selfslf,message):
        self.message = message
        print(message)
        print("you cannot submit")