from MyHelper import *
import threading


class QuitThread(Exception):
    pass


class ArknightsThread(threading.Thread):
    def __init__(self, arknights_assist, ts_plugin):
        super(ArknightsThread, self).__init__()
        self._stop_event = threading.Event()
        self._arknights_assist = arknights_assist
        self._ts = ts_plugin
        self._count = 0
        self._auto_feed = 0

    def set_counts(self, count, feed):
        self._count = count
        self._auto_feed = feed

    def stop(self):
        self._stop_event.set()

    def is_stopped(self):
        return self._stop_event.is_set()

    def run(self):
        logger.info("线程(%s) 开始运行" % self.getName())
        try:
            self.__main_loop()
        except QuitThread as e:
            logger.info("线程(%s) 已退出" % self.getName())

    def __emit_stop_signal(self):
        self.stop()
        self._arknights_assist.stop_signal.emit(int(self.getName()))

    def __sleep_or_quit(self, sleep_time, variable_time=0):
        if not self.is_stopped():
            random_sleep(sleep_time, variable_time)
        if self.is_stopped():
            logger.debug("线程(%s) 即将停止" % self.getName())
            raise QuitThread('quit')

    def __main_loop(self):
        # main loop of battle
        counter = 0
        while not self.is_stopped():
            counter += 1
            logger.info('<------ Mission Start (%d)------>' % counter)
            self.enter_battlefield()

            # detect if we are in the battle
            while not self.is_in_the_battle():
                self.__sleep_or_quit(500)
            logger.debug('已经进入战场')

            # detect if we finished
            while self.is_in_the_battle():
                self.__sleep_or_quit(500)
            logger.debug('战斗结束')
            self.__sleep_or_quit(2000)

            # bonus page
            while not self.is_proxy_ready():
                click_in_region(self._ts, *Region_Bonus)
                self.__sleep_or_quit(500, 1000)
            self.__check_counter(counter)
            self.__sleep_or_quit(500)

    def enter_battlefield(self):
        start_time = time.clock()
        while not self.is_proxy_ready():
            logger.debug('proxy is not ready')
            current_time = time.clock()
            if current_time - start_time > 10:
                logger.info("未能检测到准备界面，正在退出")
                self.__emit_stop_signal()
            self.__sleep_or_quit(1000)
        logger.debug('点击【开始行动（蓝）】')
        click_in_region(self._ts, *Region_KaiShiXingDong_Blue)
        while self._ts.GetColor(*Coord_KaiShiXingDong_Red) != Color_KaiShiXingDong_Red:
            self.__sleep_or_quit(500)
        logger.debug('点击【开始行动（红）】')
        click_in_region(self._ts, *Region_KaiShiXingDong_Red)
        logger.debug('正在进入战场')

    def is_in_the_battle(self):
        return self._ts.GetColor(*Coord_InTheBattle) == Color_InTheBattle

    def is_proxy_ready(self):
        return self._ts.GetColor(*Coord_DaiLiZhiHui) == Color_DaiLiZhiHui \
               and self._ts.GetColor(*Coord_KaiShiXingDong_Blue) == Color_KaiShiXingDong_Blue

    def __check_counter(self, counter):
        logger.info("<--- 第 %d 次战斗结束 --->" % counter)
        if self._count == counter:
            logger.info("<--- 计划任务 %d/%d 完成 --->" % (counter, self._count))
            self.__emit_stop_signal()

    def unbind_window(self):
        if self._ts is not None:
            logger.info('Thread(%s) unBindWindow return: %d' % (self.getName(), self._ts.UnBindWindow()))
            self._ts = None

