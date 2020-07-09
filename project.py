def get_event_date(event):
	return event.date

def current_users(events):
	events.sort(key=get_event_date)
	machines = {}
	for event in events:
		if event.machine not in machines:
			machines[event.machine] = set()
		if event.type == "login":
			machines[event.machine].add(event.user)
		elif event.type == "logout":
			machines[event.machine].remove(event.user)

	return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.name = machine_name
        self.user = user

events=[
    Event('2020-06-21 12:45:56', 'login', 'myworkstation.local', 'leo'),
    Event('2020-06-22 15:53:42', 'logout', 'webserver.local', 'leo'),
    Event('2020-06-21 13:40:24', 'login', 'webserver.local', 'mike'),
    Event('2020-06-22 10:25:34', 'logout', 'myworkstation.local', 'leo'),
    Event('2020-06-21 08:20:05', 'login', 'webserver.local', 'leo'),
    Event('2020-06-23 11:45:44', 'login', 'mailserver.local', 'don'),
]

users = current_users(events)
print(users)