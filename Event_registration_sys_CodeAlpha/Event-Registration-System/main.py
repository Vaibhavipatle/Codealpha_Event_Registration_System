from event_manager import EventManager
from participant_manager import ParticipantManager
from registration_manager import RegistrationManager
from event import Event
from participant import Participant
from registration import Registration
import uuid

def generate_unique_id():
    return str(uuid.uuid4())

def main():
    event_manager = EventManager()
    participant_manager = ParticipantManager()
    registration_manager = RegistrationManager()

    while True:
        print("\nEvent Registration System")
        print("1. Create Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Create Participant")
        print("6. View Participants")
        print("7. Update Participant")
        print("8. Delete Participant")
        print("9. Register Participant for Event")
        print("10. View Registrations")
        print("11. Update Registration")
        print("12. Cancel Registration")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            event_id = generate_unique_id()
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            location = input("Enter event location: ")
            max_participants = int(input("Enter max participants: "))
            
            result = event_manager.create_event(event_id, name, date, location, max_participants)
            print(result)
        
        elif choice == "2":
            events = event_manager.list_events()
            if not events:
                print("No events available.")
            else:
                for event in events:
                    print(event)
        
        elif choice == "3":
            event_id = input("Enter event ID to update: ")
            name = input("Enter new event name (leave blank to skip): ")
            date = input("Enter new event date (leave blank to skip): ")
            location = input("Enter new event location (leave blank to skip): ")
            max_participants = input("Enter new max participants (leave blank to skip): ")
            max_participants = int(max_participants) if max_participants else None
            
            result = event_manager.update_event(event_id, name, date, location, max_participants)
            print(result)
        
        elif choice == "4":
            event_id = input("Enter event ID to delete: ")
            result = event_manager.delete_event(event_id)
            print(result)
        
        elif choice == "5":
            participant_id = generate_unique_id()
            name = input("Enter participant name: ")
            email = input("Enter participant email: ")
            participant_manager.create_participant(participant_id, name, email)
            print("Participant created successfully.")
        
        elif choice == "6":
            participants = participant_manager.list_participants()
            if not participants:
                print("No participants available.")
            else:
                for participant in participants:
                    print(participant)
        
        elif choice == "7":
            participant_id = input("Enter participant ID to update: ")
            name = input("Enter new participant name (leave blank to skip): ")
            email = input("Enter new participant email (leave blank to skip): ")
            participant_manager.update_participant(participant_id, name, email)
            print("Participant updated successfully.")
        
        elif choice == "8":
            participant_id = input("Enter participant ID to delete: ")
            participant_manager.delete_participant(participant_id)
            print("Participant deleted successfully.")
        
        elif choice == "9":
            registration_id = generate_unique_id()
            event_id = input("Enter event ID: ")
            participant_id = input("Enter participant ID: ")
            event = event_manager.get_event(event_id)
            participant = participant_manager.get_participant(participant_id)
            if event and participant:
                registration_manager.create_registration(registration_id, event, participant)
                print("Participant registered for event successfully.")
            else:
                print("Invalid event ID or participant ID.")
        
        elif choice == "10":
            registrations = registration_manager.list_registrations()
            if not registrations:
                print("No registrations available.")
            else:
                for registration in registrations:
                    print(registration)
        
        elif choice == "11":
            registration_id = input("Enter registration ID to update: ")
            event_id = input("Enter new event ID (leave blank to skip): ")
            participant_id = input("Enter new participant ID (leave blank to skip): ")
            event = event_manager.get_event(event_id) if event_id else None
            participant = participant_manager.get_participant(participant_id) if participant_id else None
            registration_manager.update_registration(registration_id, event, participant)
            print("Registration updated successfully.")
        
        elif choice == "12":
            registration_id = input("Enter registration ID to cancel: ")
            registration_manager.delete_registration(registration_id)
            print("Registration cancelled successfully.")
        
        elif choice == "13":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
