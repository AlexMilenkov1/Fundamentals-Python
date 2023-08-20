class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):

        message = f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

        return message

all_messages = []

while True:
    info = input().split()

    if info[0] == 'Stop':
        break

    current_sender, current_receiver, current_content = info

    email = Email(current_sender,current_receiver, current_content)

    all_messages.append(email)

indices = [int(s) for s in input().split(', ')]


for x in indices:
    all_messages[x].send()

for email in all_messages:
    print(email.get_info())
