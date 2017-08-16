example_list = ["left", "right", "up", "down"]
# for i in range(len(example_list)):
#     print(i, example_list[i])
# for i, j in enumerate(example_list):
#     print(i, j)
#
example_dict = {"left": "a", "right": "d", "up": "w", "down": "s",}
# [print(i, j) for i, j in enumerate(example_dict)]
#
# en = enumerate(example_list)
# new_dict = dict(en)
# print(en)
# print(new_dict)

[print(i) for i in sorted(enumerate(example_list), key=lambda x: x[1])]
