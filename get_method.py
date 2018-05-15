# The get() method on dicts
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
print(greeting(4545454)) # Any random numbers will be accepted in this case
