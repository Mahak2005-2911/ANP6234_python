def gen_value_receiver():
    while True:
        r = yield
        print("you passed following value", r)
        
gen = gen_value_receiver()
next(gen)
gen.send("i am python developer")
gen.send("i am coder")