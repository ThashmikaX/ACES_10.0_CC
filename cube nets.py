def cubenets(cubes):
    # Input grid
    input_grid = cubes

    # Split the input grid into lines
    lines = input_grid.strip().split('\n')

    # Find the boundaries of the square area containing hashes
    min_x, min_y, max_x, max_y = len(lines[0]), len(lines), 0, 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    # Extract the square area
    filtered_grid = []
    for y in range(min_y, max_y + 1):
        row = lines[y][min_x:max_x + 1]
        filtered_grid.append(row)

    # Convert the filtered grid back to a string
    filtered_grid_str = "\n".join(filtered_grid)

    cubesArr = [".##\n.#.\n.#.\n##.", ".#\n.#\n##\n#.\n#.", "##.\n.#.\n.#.\n.##", "#.\n#.\n##\n.#\n.#",".#.\n###\n.#.\n.#.", ".#.\n.#.\n###\n.#.", ".#.\n.##\n##.\n.#.", ".#.\n##.\n.##\n.#.", ".#.\n.#.\n.##\n##.", ".##\n.#.\n##.\n.##", "#..\n##.\n.##\n..#", "..#\n.##\n##.\n#..", "###\n.#.\n.#.\n.#.", ".#.\n.#.\n.#.\n###", "##.\n###\n.#.\n.#.", ".#.\n.#.\n###\n#..", "..#\n###\n.#.\n.#.", ".#.\n.#.\n###\n..#", ".#.\n.#.\n.##\n##.", ".##\n.#.\n##.\n.#.", "##.\n.#.\n.##\n.#.", ".#.\n##.\n.#.\n.##", ".#.\n.##\n.#.\n##.", "##.\n.#.\n.##\n..#", ".##\n.#.\n##.\n#..", "..#\n.##\n.#.\n##.", "#..\n##.\n.#.\n.##", ".#.\n##.\n.##\n..#", ".#.\n.##\n##.\n#..", "..#\n.##\n##.\n.#.", "#..\n.##\n.##\n.#.", ]
    if filtered_grid_str in cubesArr:
        return True
    else:
        return False

cubes = int(input())
for _ in range(cubes):
    arr = list(map(int, input().split()))
    lines = []
    for _ in range(arr[0]):
        line = input()
        lines.append(line)

    multiline_input = '\n'.join(lines)

    results = cubenets(multiline_input)
    if results == True:
        print("1 0")
    else:
        print("0 1")
