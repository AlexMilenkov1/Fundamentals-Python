def add_piece(current_piece, current_composer, current_key, composer_dict):
    if current_piece in composer_dict.keys():
        return f"{current_piece} is already in the collection!"

    else:
        composer_dict[current_piece] = [current_composer, current_key]

        return f"{current_piece} by {current_composer} in {current_key} added to the collection!"
def remove_piece(current_piece, composer_dict):
    if current_piece in composer_dict.keys():
        del composer_dict[current_piece]

        return f"Successfully removed {current_piece}!"

    else:
        return f"Invalid operation! {current_piece} does not exist in the collection."

def change_key(current_piece, new_key, composer_dict):
    if current_piece in composer_dict.keys():
        composer_dict[current_piece][1] = new_key

        return f"Changed the key of {current_piece} to {new_key}!"

    else:
        return f"Invalid operation! {current_piece} does not exist in the collection."


def main_functionality(pieces):
    all_the_info = {}

    for _ in range(pieces):
        piece, composer, key = input().split('|')

        all_the_info[piece] = [composer, key]

    while True:
        command = input().split('|')

        if command[0] == 'Stop':
            break

        action, *params = command

        if action == 'Add':
            current_piece, current_composer, current_key = params

            print(add_piece(current_piece, current_composer, current_key, all_the_info))

        elif action == 'Remove':
            current_piece = params[0]

            print(remove_piece(current_piece, all_the_info))

        elif action == 'ChangeKey':
            current_piece, new_key = params

            print(change_key(current_piece, new_key, all_the_info))

    return all_the_info

number_of_pieces = int(input())

ready_collection = main_functionality(number_of_pieces)

for piece, data in ready_collection.items():
    composer, key = data

    print(f'{piece} -> Composer: {composer}, Key: {key}')

