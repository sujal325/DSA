def missing(list):
    length = len(list)
    total = length * (length + 1) / 2
    total_ = sum(list)
    missing = int(total - total_)
    print(missing)


list = [0, 1, 2, 3, 5, 6]
missing(list)
