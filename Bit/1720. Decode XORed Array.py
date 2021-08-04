class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first] * (len(encoded) + 1)

        for i in range(1, len(encoded) + 1):
            arr[i] = arr[i - 1] ^ encoded[i - 1]

        return arr
