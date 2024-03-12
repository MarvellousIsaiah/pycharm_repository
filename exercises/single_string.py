
# def swap_strings (string1, string2):
#     result = ''
#     result1 = string1 + ' ' + string2
#     result += result1
#     return result
#
#
#
#        ## string1 = input("Enter the first string: ")
#        ## string2 = input("Enter the second string: ")
#
#
#
#
#
#
#        ## print("Result:", result)


class Complex:
    def __int__(self, left, right):
        self.left = left
        self.right = right

    def _add_(self,other):
        return self.left + other. left and self. right + other.right
    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else  "-"} {abs(self.right)}i'

    c1 = complex(2,3)
    c2 = complex(5,-2)
    print (1)

