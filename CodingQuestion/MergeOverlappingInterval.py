# Problem Description: https://www.geeksforgeeks.org/merging-intervals/
# https://leetcode.com/problems/merge-intervals/

def mergeoverlapping(intervals):
    intervals.sort(key = lambda x:x[0])
    final_range = []
    final_range.append(intervals[0])
    for i in range(1, len(intervals)):
        if (final_range[-1][0] <= intervals[i][0] <= final_range[-1][1]):
            if intervals[i][1] > final_range[-1][1]:
                final_range[-1][1] = intervals[i][1]
        else:
            final_range.append(intervals[i])
    return final_range

# Driver code
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeoverlapping(intervals))
