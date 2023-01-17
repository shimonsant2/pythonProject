# function to check string is
# palindrome or not
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "malayalam1"
ans = isPalindrome(s)

s2 = '1221'
s3 = '12212'

if ans:
    print("Yes")
else:
    print("No")


    def test_answer1():
        assert isPalindrome(s2) == True

    def test_answer2():
        assert isPalindrome(s3) == False