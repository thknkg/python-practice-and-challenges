import anytree
from anytree import Node, RenderTree

with open('day_7.txt', 'r', encoding='utf-8') as f:
    text = f.read()

top = Node("/").parent
w = anytree.Walker()
out = ".."
command = "$"
change_dir = "cd"
list_file = "ls"
directory = "dir"
current_dir = top
ln = text.split("\n")
child_dirs = []
new_dir = False
node_list = []
dir_dict = {}


def check_for_new_dir(ln):
    for i in range(len(ln)):
        new_dir = False
        current_line = ln[i]
        cl = current_line
        if command in cl and list_file in cl:
            previous_line = ln[i-1].strip(command + " " + change_dir)
            for j in range(len(ln) - 1):
                next_lines = ln[j + 1]
                if new_dir == False:
                    if command not in next_lines:
                        if directory in next_lines:
                            if next_lines not in dir_dict.values():
                                dir_dict[previous_line] = []
                                dir_dict[previous_line].append(next_lines)


                        elif command in next_lines:
                            new_dir = True

                if new_dir == True:
                    break

def print_dir_files(ln):
    for i in range(len(ln)):
        new_dir = False
        current_line = ln[i]
        cl = current_line
        if command in cl:
            for j in range(len(ln) - 1):
                next_lines = ln[j + 1]
                if new_dir == False:
                    if command not in next_lines:
                        if directory not in next_lines:
                            if next_lines not in child_dirs:
                                child_dirs.append(next_lines)
                                node_list.append(Node(next_lines))


                        elif command in next_lines:
                            new_dir = True

                if new_dir == True:
                    break

for i in range(len(ln)):
    current_line = ln[i]
    cl = current_line
    if command in cl and list_file in cl:
        dr = ln[i-1].strip("$ cd ")
        if dr not in dir_dict.keys():
            dir_dict[dr] = []
        node_list.append(Node(ln[i-1].strip("$ cd ")))

        for i in range(1, len(ln) - 1):
            next_line = ln[i + 1]
            if command not in next_line:
                child_dirs.append(next_line)
                dir_dict[dr].append(next_line)
            elif command in next_line:
                break

            else:
                break


print(node_list)
print(dir_dict)
for key in dir_dict:
    print(key)

print(RenderTree(dir_dict))