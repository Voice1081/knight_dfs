
def coordinates_are_correct(field_coord):
    return 1 <= field_coord[0] <= 8 and 1 <= field_coord[1] <= 8


def pawn_does_not_attack_field(field_coord, pawn_coord):
    return field_coord != (pawn_coord[0] - 1, pawn_coord[1] + 1) and \
           field_coord != (pawn_coord[0] + 1, pawn_coord[1] + 1)


def get_next_fields(current_field, pawn_coord):
    fields = [(current_field[0] - 2, current_field[1] + 1),
              (current_field[0] - 2, current_field[1] - 1),
              (current_field[0] - 1, current_field[1] - 2),
              (current_field[0] + 1, current_field[1] - 2),
              (current_field[0] + 2, current_field[1] - 1),
              (current_field[0] + 2, current_field[1] + 1),
              (current_field[0] + 1, current_field[1] + 2),
              (current_field[0] - 1, current_field[1] + 2)]
    correct_fields = []
    for field in fields:
        if coordinates_are_correct(field) and \
                pawn_does_not_attack_field(field, pawn_coord):
            correct_fields.append(field)
    return correct_fields


def dfs(knight_coord, pawn_coord):
    stack = [knight_coord]
    track = dict()
    track[knight_coord] = None
    path_founded = False
    while len(stack) != 0:
        current_field = stack.pop()
        next_fields = get_next_fields(current_field, pawn_coord)
        for field in next_fields:
            if field in track:
                continue
            track[field] = current_field
            if field == pawn_coord:
                path_founded = True
                break
            stack.append(field)
        if path_founded:
            break
    return get_path(track, pawn_coord)


def get_path(track, end):
    path_item = end
    result = []
    while path_item is not None:
        result.append(path_item)
        path_item = track[path_item]
    result.reverse()
    return result


def main():
    print(dfs((2, 2), (5, 6)))


if __name__ == '__main__':
    main()


