from participant import Participant

class ParticipantManager:
    def __init__(self):
        self.__participants = {}

    def create_participant(self, participant_id, name, email):
        participant = Participant(participant_id, name, email)
        self.__participants[participant_id] = participant

    def get_participant(self, participant_id):
        return self.__participants.get(participant_id)

    def update_participant(self, participant_id, name=None, email=None):
        participant = self.get_participant(participant_id)
        if participant:
            if name:
                participant.name = name
            if email:
                participant.email = email

    def delete_participant(self, participant_id):
        if participant_id in self.__participants:
            del self.__participants[participant_id]

    def list_participants(self):
        return list(self.__participants.values())
