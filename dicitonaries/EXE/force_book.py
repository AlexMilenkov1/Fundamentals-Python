# sides = {}
# #
# # while True:
# #     command = input()
# #
# #     if command == 'Lumpawaroo':
# #         break
# #
# #     if '|' in command:
# #         new_command = command.split(' | ')
# #
# #         side, user = new_command
# #
# #         if side not in sides.keys() and user not in sides.values():
# #             sides[side] = []
# #             sides[side].append(user)
# #
# #         if any(user in value for value in sides.values()):
# #             continue
# #         else:
# #             sides[side].append(user)
# #
# #     else:
# #         new_command = command.split(' -> ')
# #
# #         user, side = new_command
# #
# #         if side not in sides.keys() and user not in sides.values():
# #             sides[side] = []
# #             sides[side].append(user)
# #
# #         if any(user in value for value in sides.values()):
# #             for side_ in sides.keys():
# #                 if user in sides[side_]:
# #                     sides[side_].remove(user)
# #                     sides[side].append(user)
# #                     print(f"{user} joins the {side} side!")
# #                     break
# #
# #         else:
# #             sides[side].append(user)
# #
# #
# # print(sides)


force_command = input()

force_book = {}


def force_side(side_, user_):
    for key in force_book:
        if user_ in force_book[key]:
            return
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(user_, side_)


def force_change(user_, side_):
    for key in force_book:
        if user_ in force_book[key]:
            del force_book[key][user_]
            break
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(user_, side_)
    print(f"{user_} joins the {side_} side!")


while force_command != "Lumpawaroo":

    if " | " in force_command:
        force_command = force_command.split(" | ")
        force_side(str(force_command[0]), str(force_command[-1]))
    elif " -> " in force_command:
        force_command = force_command.split(" -> ")
        force_change(str(force_command[0]), str(force_command[-1]))
    force_command = input()

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for name in force_book[side]:
            print(f"! {name}")
