class Solution:
    def duplicateZeros(self, arr: list) -> None:
        zeros_count = arr.count(0)
        length = len(arr)
        for i in range(length - 1, -1, -1):
            if arr[i] == 0:
                zeros_count -= 1
                if i + zeros_count < length:
                    arr[i + zeros_count] = 0
                if i + zeros_count + 1 < length:
                    arr[i + zeros_count + 1] = 0
            else:
                # Shift the element to the right
                if i + zeros_count < length:
                    arr[i + zeros_count] = arr[i]
