from datetime import date
from datetime import timedelta
class sayTime:
  def sayToday(self):
    return date.today()
  def sayWeek(self):
    today = date.today()
    yesterday = today - timedelta(days = 7)
    return yesterday