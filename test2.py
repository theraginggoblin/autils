acceptable_uncertainty = 0.05
actual_uncertainty = 0.07732900490760242
diff = 0.027329004907602414 # actual_uncertainty - acceptable_uncertainty
print(diff)
divided = actual_uncertainty / diff
print(divided)
square_divided = divided ** 2
print(square_divided)