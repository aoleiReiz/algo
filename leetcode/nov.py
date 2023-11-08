from typing import List


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        cur_0_count = 0
        cur_1_count = 0
        max_count = 0
        for c in s:
            if c == '1':
                cur_1_count += 1
            elif c == '0':
                if cur_1_count > 0:
                    cur_count = min(cur_0_count, cur_1_count)
                    max_count = max(cur_count, max_count)
                    cur_0_count = 0
                    cur_1_count = 0
                cur_0_count += 1
        return max(max_count, min(cur_0_count, cur_1_count))

    def shortestToChar(self, s: str, c: str) -> List[int]:
        queue = []
        ans = []
        visited = [False] * len(s)
        for idx,char in enumerate(s):
            if char == c:
                ans.append(0)
                queue.append(idx)
                visited[idx] = True
            else:
                ans.append(-1)

        step = 0
        while queue:
            new_queue = set()
            step += 1
            for i in queue:
                forward_idx = i + 1
                backward_idx = i - 1
                if backward_idx >= 0:
                    if ans[backward_idx] == -1:
                        ans[backward_idx] = step
                    if not visited[backward_idx]:
                        new_queue.add(backward_idx)
                        visited[backward_idx] = True
                if forward_idx < len(ans):
                    if ans[forward_idx] == -1:
                        ans[forward_idx] = step
                    if not visited[forward_idx]:
                        new_queue.add(forward_idx)
                        visited[forward_idx] = True
            queue = list(new_queue)

        return ans

print(Solution().shortestToChar("loveleetcode", c = "e"))