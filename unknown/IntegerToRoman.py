class Solution:
    def numbers_in_different_magnitude(self, num):
        num_in_string = str(num)
        num_len = len(num_in_string)
        num_list = []
        for i in range(num_len):
            magnitude = 10 ** (num_len - i - 1)
            digit = int(num_in_string[i])
            num_list.append(digit * magnitude)
        return num_list

    def intToRoman(self, num: int) -> str:
        roman = ""
        look_up = {
            0: "",
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        num_list = self.numbers_in_different_magnitude(num)

        for number in num_list:
            if number >= 1000:
                roman += look_up[1000] * number / 1000
            elif number >= 500:
                number -= 500
                roman += "D"
                roman += look_up[100] * number / 100
            elif number >= 100:
                roman += look_up[100] * number / 100
            elif number >= 50:
                number -= 50
                roman += "L"
                roman += look_up[10] * number / 10
            elif number >= 10:
                roman += look_up[10] * number / 10
            elif number >= 5:
                number -= 5
                roman += "V"
