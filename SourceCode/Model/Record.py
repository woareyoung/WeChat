class Record:

    def __init__(self):
        self.Time = ""
        self.Sender = ""
        self.MsgId = ""

    @staticmethod
    def get_record_object(type):
        if type == "text":
            return TextRecord()
        return Record()


class TextRecord(Record):

    def __init__(self):
        super().__init__()
        self.Content = ""

