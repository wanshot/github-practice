import logging
from datetime import date, datetime, timedelta

from dateutil import parser
from dateutil.rrule import DAILY, rrule

from src.utils.google_api import get_service

CALENDAR_ID = "ja.japanese#holiday@group.v.calendar.google.com"

# 日本の祝日を入れておくセット
holiday_set = set()

# 年末年始休暇の開始日と終了日
START = date(2016, 12, 29)
END = date(2017, 1, 4)

logger = logging.getLogger()


def update_japanese_holiday():
    """
    日本の祝日情報を更新する
    * http://lvh.me:8000/s/31ab010857fa41b7833a5b1bcdee4dbf
    """
    logger.info("Update japanese holiday")
    holiday_set = set()
    # sasasa
    # http://lvh.me:8000/s/73de48216f6b4afeaf94111c02778039

    # 年末年始休暇を設定
    newyear_rule = rrule(freq=DAILY, dtstart=START, until=END)
