import random


class pvSimulator:

    def __init__(self,
                 peak_primary=3.2,
                 peak_time_primary=14,
                 scale_primary=-0.09,
                 peak_secondary=0.5,
                 peak_time_secondary=13,
                 scale_secondary=-0.007,
                 noise_scale=0.05):

        # primary parabola values
        self.__peak_primary = peak_primary
        self.__peak_time_primary = peak_time_primary
        self.__scale_primary = scale_primary

        # secondary parabola values
        self.__peak_secondary = peak_secondary
        self.__peak_time_secondary = peak_time_secondary
        self.__scale_secondary = scale_secondary

        # noise scale
        self.__noise_scale = noise_scale

    def __getParabolaValue(self, a, x, h, k):
        return a * (x - h) * (x - h) + k

    def __getPrimary(self, time, add_noise=True):
        power = self.__getParabolaValue(
            a=self.__scale_primary,
            x=time,
            h=self.__peak_time_primary,
            k=self.__peak_primary
        )

        if add_noise:
            power *= random.uniform(1 - self.__noise_scale, 1 + self.__noise_scale)

        return power

    def __getSecondary(self, time, add_noise=True):
        power = self.__getParabolaValue(
            a=self.__scale_secondary,
            x=time,
            h=self.__peak_time_secondary,
            k=self.__peak_secondary
        )

        if add_noise:
            power *= random.uniform(1 - self.__noise_scale, 1 + self.__noise_scale)

        return power

    def getPowerValue(self, time):
        from datetime import datetime
        assert isinstance(time, datetime)
        # convert to float
        time = time.hour+time.minute/60+time.second/60/60

        return max(0, max(self.__getPrimary(time), self.__getSecondary(time)))
