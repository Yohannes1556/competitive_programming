class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        n = len(A)
        sums = [0] * (n+1)
        for i in range (1, n+1):
            sums[i] = A[i-1] +sums[i-1]

        queue = collections.deque()
        result = sys.maxsize

        for right, s in enumerate(sums):
            while queue and s <= sums[queue[-1]]:
                queue.pop()

            while queue and s - sums[queue[0]] >= k:
                result = min(result, right - queue.popleft())
            queue.append(right)
        return result if result != sys.maxsize else - 1
