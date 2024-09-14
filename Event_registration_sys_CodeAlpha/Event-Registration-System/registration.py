class Registration:
    def __init__(self, registration_id, event, participant):
        self.__registration_id = registration_id
        self.__event = event
        self.__participant = participant

    @property
    def registration_id(self):
        return self.__registration_id

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event):
        self.__event = event

    @property
    def participant(self):
        return self.__participant

    @participant.setter
    def participant(self, participant):
        self.__participant = participant

    def __str__(self):
        return f"Registration({self.__registration_id}, {self.__event}, {self.__participant})"
