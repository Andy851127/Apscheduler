from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time

class Apscheduler():
    def __init__(self):
        # 創建一個 BackgroundScheduler 實例
        self.scheduler = BackgroundScheduler()

    def schedule_process(self,func_job):
        
        # 添加定時任務，設定每小時執行一次
        self.scheduler.add_job(func_job, trigger=IntervalTrigger(hours=1))

        # 啟動排程器
        self.scheduler.start()

        # 讓程式持續執行，以便排程器能夠運作
        try:
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            # 當程式中斷或退出時，關閉排程器
            self.scheduler.shutdown()
