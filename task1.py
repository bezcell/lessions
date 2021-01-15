import datetime, time


class Дата:
    date_str = ''

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def reformat_date(cls, obj):
        date_list = obj.date_str.split('-')
        date_obj = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0])).timetuple()
        result_int = int(time.mktime(date_obj))
        return result_int

    @staticmethod
    def validate_date(obj):
        valid = True
        date_list = obj.date_str.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        if day < 0 or day > 31:
            valid = False
        if month < 0 or month > 12:
            valid = False
        if year < 1:
            valid = False
        return valid


date_o = Дата('01-10-2021')
date_int = date_o.reformat_date(date_o)
print(date_int)
date_valid = date_o.validate_date(date_o)
print(date_valid)
