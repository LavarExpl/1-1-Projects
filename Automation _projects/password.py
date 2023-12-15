class PWD:
    correct_pwd = 'varvar'
    correct_usn = 'scavyvar'

    def __init__(self,username, attempt):
        self.username = username
        self.attempt = attempt

   # username = input('Enter username:')
    #attempt = input('Enter Password')
    #if self.username == PWD.correct_usn and PWD.attempt == correct_pwd:

                   # print(f' Hi {username}, Hope you are having a great day.')
                  #  print("\U0001f600")

username = input('Enter username:')
attempt = input('Enter Password')
p1= PWD('scavyvar','varvar')


if username == PWD.correct_usn and PWD.correct_pwd== attempt :
        print(f' Hi {p1.username}, Hope you are having a great day.')
        print("\U0001f600")
