class Party:
    def __init__(self):
        self.people = []

    def add_people(self, name):
        self.people.append(name)


party = Party()

while True:
    person = input()

    if person == 'End':
        break

    party.add_people(person)

print(f"Going: {', '.join(party.people)}")
print(f'Total: {len(party.people)}')
