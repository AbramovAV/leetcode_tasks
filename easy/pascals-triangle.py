class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = [[1]]
        last_row_len = 1
        for row in range(1, numRows):
            new_row = []
            last_row = pascal_triangle[-1]
            last_row_len = len(last_row)
            for i in range(last_row_len-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row = [1] + new_row + [1]
            pascal_triangle.append(new_row)
        return pascal_triangle