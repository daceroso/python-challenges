text = "this is a very special challenge_string"
print(text.capitalize())
print(text.title())

product = "Apple Mac"
price = 3500

# variants of the formatted output

print("the", product, "costs", price)
print("the {} cost {}".format(product, price))
print(f"the %s costs %d" % (product, price))
print(f"the {product} costs {price}")
