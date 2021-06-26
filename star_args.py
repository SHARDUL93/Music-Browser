#from __future__ import print_function
#print("Hello","planet","earth")

#*args
print("*args")
def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:",*args)
    mean = 0
    for arg in args:
        mean += arg
    return mean/len(args)


print("Average : {}".format(average(1,2,3,4)))


def build_tuple(*args):
    return args


num_tuple = build_tuple(1,2,3,4,5)
print(type(num_tuple))
print("num_tuple: ",num_tuple,end='\n')

string_tuple = build_tuple("abc","def","ghi","jkl")
print(type(string_tuple))
print("string_tuple: ",string_tuple,end='\n')


#**kwargs
print("**kwargs")
# def print_backwards(*args, end=' ', **kwargs):
# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     kwargs.pop('end',None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)

def print_backwards(*args, **kwargs):
    end_char = kwargs.pop('end','\n')
    sep_char = kwargs.pop('sep',' ')
    for word in args[:0:-1]: #change the range
        print(word[::-1], end=sep_char, **kwargs)
    print(args[0][::-1], end=end_char, **kwargs)  #print the 1st word separately
    # print(end=end_char)


def backwards_print(*args, **kwargs):
    sep_char = kwargs.pop('sep',' ')
    print(sep_char.join(word[::-1] for word in args[::-1]), **kwargs)



with open("backwards.txt",'w') as backwards:
    # print_backwards("hello","planet","earth","take","me","to","your","leader", file=backwards)
    print_backwards("hello","planet","earth","take","me","to","your","leader", end='\n')
    print("another string")

print()
print("hello","planet","earth","take","me","to","your","leader", end='', sep='\n**\n')
print_backwards("hello","planet","earth","take","me","to","your","leader", end='', sep='\n**\n')
print("="*10)
