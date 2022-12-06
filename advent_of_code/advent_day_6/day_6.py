"""check for certain sequences by iterating through large string of text"""
with open('day_6.txt', 'r', encoding='utf-8') as f:
    text = f.read()

data = []

for n in range(len(text)):
    data.append(text[n])


def find_packets(num):
    print([i + num for i in range(len(data)) if len(set(data[i:i + num])) == num][0])


find_packets(4)
find_packets(14)

# works for some reason with 4 but not 14, using range(len(data)) in list comprehension helped a lot with other version
# char_list = []
# for i in data:
#     char_list.append(i)
#     count += 1
#     if len(char_list) == 4:
#         for i in char_list:
#             test.add(i)
#         if len(test) == 4:
#            print(count)
#         else:
#             test = set()
#             char_list = []
