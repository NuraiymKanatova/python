# a generator function is a special type of function that returns an iterator object
# instead of using return to send back a single value
# generator use yield to produce a series of results over time
# the function pauses its execution after yield, maintaining its state between iterations

def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)
 # output will be 
 # 1 
 # 2 
 # 3 
 # 4 
 # 5    

 # this generator function fun yields numbers from 1 up to a specified max
 # each call to next() on the generator object resumes execution 
 # right after the yield statement where it last left off

 # why do we need generators?
 # memory efficient, 
 # no list overhead, 
 # lazy evaluation, 
 # support infinite sequences, 
 # pipeline processing