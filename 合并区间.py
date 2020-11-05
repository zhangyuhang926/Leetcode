def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merge = []
    for interval in intervals:
        if not merge or merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1][1] = max(merge[-1][1], interval[1])
    return merge

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))