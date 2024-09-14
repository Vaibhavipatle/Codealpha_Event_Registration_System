class Participant:
    def __init__(self, participant_id, name, email):
        self.__participant_id = participant_id
        self.__name = name
        self.__email = email

    @property
    def participant_id(self):
        return self.__participant_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f"Participant({self.__participant_id}, {self.__name}, {self.__email})"
