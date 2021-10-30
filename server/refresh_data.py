import schedule
import time
import get_data


def refresh():
    get_data.get_rates()


schedule.every().hour.do(refresh)

while True:
    schedule.run_pending()
    time.sleep(1)
