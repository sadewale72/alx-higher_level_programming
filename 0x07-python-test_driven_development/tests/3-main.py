#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Adewale", "Aderoju")
say_my_name("Adewale", "Aderoju")
say_my_name("wale")
try:
    say_my_name(12, "Aderoju")
except Exception as e:
    print(e)
