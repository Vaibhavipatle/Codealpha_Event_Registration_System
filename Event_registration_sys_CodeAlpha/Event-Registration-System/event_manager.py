from event import Event

class EventManager:
    def __init__(self):
        self.__events = {}

    def create_event(self, event_id, name, date, location, max_participants):
        if self.is_event_available(date):
            if self.is_location_available(date, location):
                event = Event(event_id, name, date, location, max_participants)
                self.__events[event_id] = event
                return "Event created successfully."
            else:
                return "Event cannot be created. Another event is already booked at this location on that date."
        else:
            return "Event cannot be created. Another event is already booked on that date."

    def is_event_available(self, date):
        for event in self.__events.values():
            if event.date == date:
                return False
        return True

    def is_location_available(self, date, location):
        for event in self.__events.values():
            if event.date == date and event.location == location:
                return False
        return True

    def get_event(self, event_id):
        return self.__events.get(event_id)

    def update_event(self, event_id, name=None, date=None, location=None, max_participants=None):
        event = self.get_event(event_id)
        if event:
            if date and not self.is_event_available(date):
                return "Event cannot be updated. Another event is already booked on that date."
            if location and not self.is_location_available(date, location):
                return "Event cannot be updated. Another event is already booked at this location on that date."

            if name:
                event.name = name
            if date:
                event.date = date
            if location:
                event.location = location
            if max_participants:
                event.max_participants = max_participants
            return "Event updated successfully."
        else:
            return "Event not found."

    def delete_event(self, event_id):
        if event_id in self.__events:
            del self.__events[event_id]
            return "Event deleted successfully."
        else:
            return "Event not found."

    def list_events(self):
        return list(self.__events.values())
