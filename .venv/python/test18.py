def numIslands(l):
    if not l:
        return 0

    def test_island(i, j):
        if i < 0 or i >= len(l) or j < 0 or j >= len(l[0]) or l[i][j] == "0":
            return

        l[i][j] = "0"
        test_island(i + 1, j)
        test_island(i - 1, j)
        test_island(i, j + 1)
        test_island(i, j - 1)
    c = 0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == "1":
                c += 1
                test_island(i, j)

    return c

def take_grid_input():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))

    print(f"Enter the grid row by row (use '1' for land and '0' for water):")
    grid = []

    for _ in range(m):
        row = input().strip().split()
        if len(row) != n:
            print(f"Invalid row! Please enter exactly {n} values.")
            return None
        grid.append(row)

    return grid

l = take_grid_input()
if l:
    print("Input grid:")
    for row in l:
        print(row)
print(numIslands(l))
