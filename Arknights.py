from MyHelper import *
import logging

# Detect Coordinate
Coord_DaiLiZhiHui = 1200, 700
Coord_KaiShiXingDong_Blue = 1391, 805
Coord_KaiShiXingDong_Red = 1173, 456
Coord_InTheBattle = 1339, 95

# Click Region (x1, y1, x2, y2)
Region_KaiShiXingDong_Blue = 1176, 748, 1391, 805
Region_KaiShiXingDong_Red = 1173, 456, 1308, 753
Region_Bonus = 1100, 260, 1400, 400

# Color Baseline
Color_DaiLiZhiHui = 'ffffff'
Color_KaiShiXingDong_Blue = '0075a8'
Color_KaiShiXingDong_Red = 'c14600'
Color_InTheBattle = 'ffffff'


class Arknights:
    def __init__(self, arknights_assist, ts_plugin):
        self.arknights_assist = arknights_assist
        self.ts = ts_plugin
        self._running = False
        self.count = 0
        self.auto_feed = 0

    def set_counts(self, count, feed):
        self.count = count
        self.auto_feed = feed

    def terminate(self):
        self._running = False

    def run(self):
        self._running = True
        self.main_loop()

    def is_running(self):
        return self._running

    def thread_sleep(self, sleep_time, variable_time=0):
        if self._running:
            random_sleep(sleep_time, variable_time)
        if not self._running:
            logging.info("Arknights stopped")
            quit()

    def main_loop(self):
        # main loop of battle
        print('--------------------')
        counter = 0
        while self._running:
            counter += 1
            logging.info('<------ Mission Start (%d)------>' % counter)
            self.enter_battlefield()

            # detect if we are in the battle
            while not self.is_in_the_battle():
                self.thread_sleep(500)
            logging.debug('now we are in the battle')

            # detect if we finished
            while self.is_in_the_battle():
                self.thread_sleep(500)
            logging.debug('battle finished')
            self.thread_sleep(2000)

            # bonus page
            while not self.is_proxy_ready():
                logging.debug('bonus time ~~~')
                click_in_region(self.ts, *Region_Bonus)
                self.thread_sleep(500, 1000)
            logging.debug('leave bonus page')
            logging.info('<------ Mission End (%d)------>' % counter)
            if self.count == counter:
                self.arknights_assist.ui.pushButton_stop.click()
                logging.info("Arknights %d mission planning finished" % self.count)
                quit()
            self.thread_sleep(500)

    def enter_battlefield(self):
        while not self.is_proxy_ready():
            logging.info('proxy is not ready')
            self.thread_sleep(500)
        logging.debug('click KaiShiXingDong(Blue)')
        click_in_region(self.ts, *Region_KaiShiXingDong_Blue)
        while self.ts.GetColor(*Coord_KaiShiXingDong_Red) != Color_KaiShiXingDong_Red:
            self.thread_sleep(500)
        logging.debug('click KaiShiXingDong(Red)')
        click_in_region(self.ts, *Region_KaiShiXingDong_Red)
        logging.debug('entered battlefield')

    def is_in_the_battle(self):
        return self.ts.GetColor(*Coord_InTheBattle) == Color_InTheBattle

    def is_proxy_ready(self):
        return self.ts.GetColor(*Coord_DaiLiZhiHui) == Color_DaiLiZhiHui \
               and self.ts.GetColor(*Coord_KaiShiXingDong_Blue) == Color_KaiShiXingDong_Blue



