def count_islands(map):
    island_coords = []
    for row_num in range(len(map)):
        for col_num in range(len(map[row_num])):
            if map[row_num][col_num] == 1:
                if not last(map, row_num, col_num):
                    island_coords.append([(row_num, col_num)])
                else:
                    island_coords[-1].append((row_num, col_num))
    return len(island_coords)


def last(island_map, row, col):
    adjacent = False
    if row != 0:
        adjacent = bool(island_map[row-1][col])

    if col != 0 and not adjacent:
        adjacent = bool(island_map[row][col-1])

    return adjacent
