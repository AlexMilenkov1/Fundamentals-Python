def add_stop(stops, commands):
    index = int(commands[1])
    string = commands[2]

    if 0 <= index <= len(stops) - 1:
        first_part = stops[:index]
        second_part = stops[index:]
        stops = first_part + string + second_part

    return stops

def remove_stop(stops, commands):
    start_index = int(commands[1])
    end_index = int(commands[2])

    if 0 <= start_index <= len(stops) - 1 and 0 <= end_index <= len(stops) - 1:
        part_to_remove = stops[start_index:end_index + 1]

        stops = stops.replace(part_to_remove, '')

    return stops


def switch_location(stops, commands):
    old_string = commands[1]
    new_string = commands[2]

    if old_string in stops:
        stops = stops.replace(old_string, new_string)

    return stops


def main_control_of_destinations(stops):
    while True:
        commands = input().split(':')

        if commands[0] == 'Travel':
            break

        action = commands[0]

        if action == 'Add Stop':
            stops = add_stop(stops, commands)

            print(stops)

        elif action == 'Remove Stop':
            stops = remove_stop(stops, commands)

            print(stops)

        elif action == 'Switch':
            stops = switch_location(stops, commands)

            print(stops)

    return stops

destinations = input()
result =  main_control_of_destinations(destinations)

print(f"Ready for world tour! Planned stops: {result}")