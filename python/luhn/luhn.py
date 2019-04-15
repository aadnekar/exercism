class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def is_valid(self):
        if len(self.card_num) < 2 or not self.card_num.isdigit():
            return False

        digits = list(self.card_num)

        for _ in range(len(digits)-2, -1, -2):
            digits[_] = int(digits[_]) * 2
            digits[_] = digits[_] if digits[_] < 10 else digits[_] - 9
        
        return sum(int(_) for _ in digits) % 10 == 0