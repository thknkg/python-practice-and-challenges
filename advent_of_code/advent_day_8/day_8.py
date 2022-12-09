"""count how many trees in a grid are visible from the outside"""
import numpy as np

# get data and convert to a 2d array
tree_grid = np.array([[int(column) for column in row] for row in open("day_8.txt").read().strip().split("\n")])

# numpy lets you duplicate arrays but filled with zeroes and make of similar type, respectively
tree_visible_boolean_array = np.zeros_like(tree_grid)
tree_visibility_distance = np.ones_like(tree_grid)

# iterate for each direction
for n in range(4):
    # get dimensions for grid
    for x, y in np.ndindex(tree_grid.shape):
        # go in a straight line and add each to a list if none in that direction are in the way
        path = [d < tree_grid[x, y] for d in tree_grid[x, y + 1:]]

        # update by mapping 1 values to array if visible from outside, join all coordinates with those found in path
        tree_visible_boolean_array[x, y] |= all(path)

        # multiply the values of each direction by each other to get the total visibility score (learned about ~ which is
        # helpful for counting backwards in an index, ex. ~0 = -1)
        tree_visibility_distance[x, y] *= next((i + 1 for i, e in enumerate(path) if ~e), len(path))

    # rotate the arrays to run the loop for each direction
    tree_grid, tree_visible_boolean_array, tree_visibility_distance = map(np.rot90,
                                                                          [tree_grid, tree_visible_boolean_array,
                                                                           tree_visibility_distance])

print(tree_visible_boolean_array.sum())
print(tree_visibility_distance.max())
