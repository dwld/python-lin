from abc import ABCMeta, abstractmethod


class BusABC(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        raise NotImplementedError("__init__ function function not implemented")

    @abstractmethod
    def send(self, message):
        raise NotImplementedError("send function function not implemented")

    @abstractmethod
    def recv(self, timout_s):
        raise NotImplementedError("recv function function not implamented")

    @abstractmethod
    def addSchedule(self, schedule, index):
        raise NotImplementedError("addSchedule function not implemented")

    @abstractmethod
    def startSchedule(self, index):
        raise NotImplementedError("startSchedule function not implemented")

    @abstractmethod
    def pauseSchedule(self, index):
        raise NotImplementedError("pauseSchedule function not implemented")

    @abstractmethod
    def stopSchedule(self, index):
        raise NotImplementedError("stopSchedule function not implemented")

    @abstractmethod
    def wakeBus(self):
        raise NotImplementedError("wakeBus function not implemented")

    @abstractmethod
    def closeConnection(self):
        raise NotImplementedError("closeConnection function not implemented")

		
