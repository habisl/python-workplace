# Pythonic tricks for get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

# Calling the function with the ids
print(greeting(382))
# "Hi Alice!"

print(greeting(4545454)) # If it does not exist then the value of the default argument is returned instead.
# "Hi there!"

