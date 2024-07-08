# 示例字典
example_dict = {'a': 3, 'b': 1, 'c': 2}

# 按值排序字典并返回排序后的键值对列表
vals = example_dict.items()
sorted_items = sorted(example_dict.items(), key=lambda item: item[1])

print(sorted_items)
