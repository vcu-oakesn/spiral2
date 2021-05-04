def spiralize(size, n=1):
    """ Your code goes somewhere in here"""

    # first step is to get a list of all numbers between 1 and 501
    a = 502
    all_numbers = list(range(1,a))

    # next step is to establish a complete ring around the previous spiral layer
    b = 1
    select_list1 = []
        for x in select_list1:
            if x = (b+2)^2
                select_list1.append(x)

    # what I'm trying to do here is say that one ring continues until the x is
    # the square of b + 2 (so the first ring would go until x = (b+2)^2, or 3*3 = 9)

    # except I need the sum, starting at 1 (and skipping 1) of all those numbers to b
    # so the select_list list needs to be in a for (or while) loop and adding 2 after each layer
    c = 1
    select_list2 = []
        for y in range(1,a)
            if y = (c+2)^2 
                select_list2.append(y) and 
                # here's where I get stuck--I need add two to c to create the next layer
                # Googling brings me to GLobal and Local variables, but I don't know how
                # to incorporate Print and Return statements 
                def specific_list:
                    d = c + 2
                        if y = (c+2)^2
                    print(d)

    # so what I'm trying to do is identify the values in the list by: 1) skipping over
    # 1 (starting at c) in the all_numbers list, starting at 1, until we get to the square of 
    # c, (1+2) = 3^2 = 9. Then we add 2 to c to get the new base of d (so now we're skipping)
    # not 1 but 3 digits in the over all_numbers list until we get to the new value of 
    # (d + 2)^2 = (3+2)^2 = 25, which would give us the next ring in the spiral,
    # and then we add 2 to the new value of d, which then returns the new
    # value of c...until we get through the whole range of the all_numbers list. 

    return_value = sum(select_list2)
    return return_value

    # I know none of this actually works, but after last class I could see you're looking
    # for our train of thought. I don't know how to actually code most of this, so do with
    # it what you will. It's been swell.