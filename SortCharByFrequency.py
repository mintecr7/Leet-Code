class Solution:
    def frequencySort(self, s: str) -> str:

        count = dict()
        output = ''

        for char in s:
            if char in count.keys():
                count[char] += 1
            else:
                count[char] = 1

        sorted_tuples = sorted(count.items(), key=lambda item: item[1], reverse=True)

        for items in sorted_tuples:
            output += items[0] * items[1]

        return output
