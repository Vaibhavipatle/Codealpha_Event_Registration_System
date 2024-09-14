class Event:
    def __init__(self, event_id, name, date, location, max_participants):
        self.__event_id = event_id
        self.__name = name
        self.__date = date
        self.__location = location
        self.__max_participants = max_participants
        self.__registrations = []

    @property
    def event_id(self):
        return self.__event_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def max_participants(self):
        return self.__max_participants

    @max_participants.setter
    def max_participants(self, max_participants):
        self.__max_participants = max_participants

    def add_registration(self, registration):
        if len(self.__registrations) < self.__max_participants:
            self.__registrations.append(registration)
        else:
            raise ValueError("Event is full")

    def remove_registration(self, registration):
        self.__registrations.remove(registration)

    def get_registrations(self):
        return self.__registrations

    def __str__(self):
        return f"Event({self.__event_id}, {self.__name}, {self.__date}, {self.__location}, {self.__max_participants})"
