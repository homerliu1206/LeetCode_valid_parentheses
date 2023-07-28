class Solution:
    def isValid(self, s):

        # Arrange the elements
        a = "()"
        b = "[]"
        c = "{}"
        list_s = "".join(list(s))
        # list_s = "".join(sorted(list(s))) # if the seperated two elements can be regared valid
        print(list_s)

        # Remove valid parentheses from the strings
        while bool(list_s) == True:
            if a in list_s:
                list_s = list_s.replace(a, "")
            elif b in list_s:
                list_s = list_s.replace(b, "")
            elif c in list_s:
                list_s = list_s.replace(c, "")
            elif a or b or c not in list_s:
                break

        # Finally checking the remains of the string
        if bool(list_s) == True:
            print(False)
        elif bool(list_s) == False:
            print(True)

solution = Solution()
solution.isValid("(]")

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false