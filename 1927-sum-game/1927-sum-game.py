class Solution:
    def sumGame(self, num: str) -> bool:

        left_marks = 0
        right_marks = 0
        left_sum = 0
        right_sum = 0

        for index, digit in enumerate(num):
            if index < ( len(num) / 2 ):
                if digit == "?":
                    left_marks += 1
                else:
                    left_sum += int(digit)
            elif digit == "?":
                right_marks += 1
            else:
                right_sum += int(digit)

        sum_marks = left_marks + right_marks
        sum_differential = left_sum - right_sum

        if sum_marks % 2 != 0:
            return True
        
        if sum_differential == ( 9/2 * (right_marks - left_marks) ):
            return False
        else:
            return True