from registration import Registration

class RegistrationManager:
    def __init__(self):
        self.__registrations = {}

    def create_registration(self, registration_id, event, participant):
        registration = Registration(registration_id, event, participant)
        self.__registrations[registration_id] = registration
        event.add_registration(registration)

    def get_registration(self, registration_id):
        return self.__registrations.get(registration_id)

    def update_registration(self, registration_id, event=None, participant=None):
        registration = self.get_registration(registration_id)
        if registration:
            if event:
                registration.event.remove_registration(registration)
                registration.event = event
                event.add_registration(registration)
            if participant:
                registration.participant = participant

    def delete_registration(self, registration_id):
        registration = self.get_registration(registration_id)
        if registration:
            registration.event.remove_registration(registration)
            del self.__registrations[registration_id]

    def list_registrations(self):
        return list(self.__registrations.values())
