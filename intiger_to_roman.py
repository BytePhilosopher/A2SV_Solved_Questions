class Solution:
    def intToRoman(self, num: int) -> str:
        hash = {
            1: "I", 2: "II", 3: "III", 4: "IV",
            5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
            10: "X", 40: "XL", 50: "L", 90: "XC",
            100: "C", 400: "CD", 500: "D",
            900: "CM", 1000: "M"
        }

        _num = str(num)
        ans = ""

        while True:
            if num == 0:        # ✅ FIX: stop when fully converted
                break

            if len(_num) == 1:
                ans += hash[int(_num)]
                break

            base = pow(10, len(_num) - 1)
            digit = int(_num[0])
            power = base * digit
            num -= power

            if power in hash:
                ans += hash[power]
            else:
                if base == 100:
                    if digit >= 5:
                        ans += "D"
                        digit -= 5
                    ans += "C" * digit
                elif base == 10:
                    if digit >= 5:
                        ans += "L"
                        digit -= 5
                    ans += "X" * digit
                else:  # thousands
                    ans += "M" * digit

            _num = str(num)

        return ans
