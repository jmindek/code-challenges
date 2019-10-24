def count_islands(map):
    last = 0
    island_coords = []
    # TODO master the dang multiple for for loop
    for row_num in range(len(map)-1):
        for col_num in range(len(map[row_num])-1):
            if map[row_num][col_num]:
                if not last:
                    island_coords.append([(row_num, col_num)])
                    last = 1
                else:
                    island_coords[-1].append((row_num, col_num))
            else:
                last = 0

    return len(island_coords)
