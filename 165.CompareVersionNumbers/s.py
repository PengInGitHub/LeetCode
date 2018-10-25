class Solution:
    def compareVersion(self, version1, version2):
        v1 = map(int, version1.split("."))
        v2 = map(int, version2.split("."))

        v1.extend([0]*(len(v2)-len(v1)))
        v2.extend([0]*(len(v1)-len(v2)))

        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
        return 0