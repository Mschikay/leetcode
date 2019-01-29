class Solution:
    def minSwapsCouples1(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        if not row:
            return None

        length = len(row)
        swap = 0
        seat = {location: idCouple for (idCouple, location) in enumerate(row)}

        for i in range(0, length, 2):
            partnerLocation = -1
            if row[i] % 2:
                partnerLocation = row[i] - 1
                if row[i + 1] == row[i] - 1:
                    continue

            if not row[i] % 2:
                partnerLocation = row[i] + 1
                if row[i + 1] == row[i] + 1:
                    continue

            originalLocation = row[i + 1]
            row[i + 1] = partnerLocation

            seat[originalLocation] = seat[partnerLocation]
            row[seat[partnerLocation]] = originalLocation

            seat[partnerLocation] = i + 1
            swap += 1
            print(row)

        return swap

    def minSwapsCouples(self, row):
        if not row:
            return None

        rowGroup = [r // 2 for r in row]
        groups = {i: i + 1 for i in range(0, len(rowGroup) // 2)}
        swap = 0
        for j in range(0, len(rowGroup), 2):
            if rowGroup[j] != rowGroup[j + 1]:
                if groups.get(rowGroup[j], rowGroup[j]) != groups.get(rowGroup[j + 1], rowGroup[j + 1]):
                    print(groups)
                    swap += 1
                    value = groups.setdefault(rowGroup[j], None) or groups.setdefault(rowGroup[j+1], None)
                    if value:
                        groups[rowGroup[j]] = value
                        groups[rowGroup[j+1]] = value
                    groups[rowGroup[j]] = groups[rowGroup[j]]
                    groups[rowGroup[j + 1]] = value[rowGroup[j]]

        return swap

# 提取一对数
# 如果属于不同组群，swap++ 在groups里面寻找是否有存在，如果有，等于它 如果没有 新建


