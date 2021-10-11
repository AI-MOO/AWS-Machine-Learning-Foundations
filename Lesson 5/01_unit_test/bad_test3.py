from nearest import nearest_square

nearest_5 = nearest_square(5)
print("Nearest square <=5: returned {}, correct answer is 4.".format(nearest_square(5)))
assert(nearest_5 == 4)

nearest_n12 = nearest_square(-12)
print("Nearest square <=-12: returned {}, correct answer is 0.".format(nearest_square(-12)))
assert(nearest_n12 == 0)

nearest_9 = nearest_square(9)
print("Nearest square <=9: returned {}, correct answer is 9.".format(nearest_square(9)))
assert(nearest_9 == 9)