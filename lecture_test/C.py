class Passenger:
    def __init__(self, distance):
        self.distance = distance


class Driver:
    def __init__(self, speed, oil):
        self.speed = speed
        self.oil = oil
        self.waittime = 0
        self.drivetime = 0

    def wait(self, passengerline):
        if passengerline:
            passenger = passengerline[0]
            passengerline.remove(passenger)
        else:



class 
