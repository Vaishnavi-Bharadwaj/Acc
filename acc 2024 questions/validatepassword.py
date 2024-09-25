# Given a string, it should have:
# atleast 4 characters
# atleast 1 numeric
# atleast 1 capital letter
# no space or slash 
# should not begin with a number 
import re
def main():
    string=input()
    print(validate(string))

def validate(string):
    if len(string)<4 or string[0].isdigit():
        return False
    if re.search('\d',string) and re.search('[A-Z]',string) and not re.search('[ /]',string):
        return True
    
if __name__=='__main__':
    main()