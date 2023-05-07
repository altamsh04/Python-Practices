class MyClass:
    def print_int_char(self, n, c):
        print("Integer:", n)
        print("Character:", c)
    
    def print_char_int(self, c, n):
        print("Character:", c)
        print("Integer:", n)

my_obj = MyClass()

my_obj.print_int_char(10, 'a')

my_obj.print_char_int('b', 20)
