pass_gen is a library for dealing with generating secure randomised passwords that are customisable and strong simultaneously.

Usage examples:

var = simple(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
print(var.generate(3))

print(var.result(1))

stored_password = hash(var.result(1))
print(stored_password)

p = input('Password: ')
if verify_hash(stored_password, p) == True:
    print('The password is correct')


Output:

['5oruq5qvih4eh79zowqv', '8cyx7ytx62wm5i2dgkzp', 'gt9ttdboh3efmnulpnto']
8cyx7ytx62wm5i2dgkzp
4d9a0dcb403512b316d166fe65b43cd273b61786957b20591f8bd2e9df465283db1022d036e53e7d1525d22ac9f3539e6a8e4c66abe124edb935020295a47955198d4d3201af0d60a42330713423e174001fd0abb8b5f603ecb1040a220f0469
Password: 8cyx7ytx62wm5i2dgkzp
The password is correct
