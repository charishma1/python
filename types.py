""" data types"""
#boolean
b_true = True
v_false = False
x_none = None

#integers
i_1 = 123
i_2 = -456

#Floats
f_1 = 3.14
f_2 = 0.00159

#strings
s_single = 'this is a string'
s_double = "this is also string"
s_triple = """ You guessed it, i am a string"""
s_wrap = """ This strong can
             span multiple 
            lines"""
#lists
l_simple = [1, 2, 3, 4]
l_mixed = [1, "2", b_true, f_1, s_triple, None]
l_nested = [
  [1, 2, 3],
  ["1", "2", "3"],
]
#tuples
t_basic = (1, 2, 3, 4)
t_2 = 5, 6, 7, 8

#dict
d_simple = {
    1: 2,
    "3": 2,
    True: False
}
d_mixed = {
    "a" : 7,
    "x_none" : x_none,
    "s_double" : s_double
}
d_nested = {
    "d_simple": d_simple,
    "d_mixed": d_mixed,
    "nested": {
        "l_simple": l_simple
    }
}