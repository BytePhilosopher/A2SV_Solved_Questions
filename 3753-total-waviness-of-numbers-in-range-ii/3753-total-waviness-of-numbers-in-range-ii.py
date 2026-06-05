class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import cache

        def solve(n):
            s = str(n)

            @cache
            def dfs(pos, tight, started, prev2, prev1, length):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            False,
                            10,
                            10,
                            0
                        )
                        total_cnt += cnt
                        total_wav += wav

                    elif not started:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            10,
                            d,
                            1
                        )
                        total_cnt += cnt
                        total_wav += wav

                    elif length == 1:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            prev1,
                            d,
                            2
                        )
                        total_cnt += cnt
                        total_wav += wav

                    else:
                        add = int(
                            (prev2 < prev1 > d) or
                            (prev2 > prev1 < d)
                        )

                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            prev1,
                            d,
                            length + 1
                        )

                        total_cnt += cnt
                        total_wav += wav + add * cnt

                return total_cnt, total_wav

            return dfs(0, True, False, 10, 10, 0)[1]


       
        return solve(num2) - solve(num1 - 1)