public_toilet="pb"

def home():
    private_toilet="PT"
    print(private_toilet)
    print(public_toilet)
home()

def stranger():
#    print(private_toilet) // local variable not allowed
    print(public_toilet)
#print(private_toilet) // local variable not allowed

print(public_toilet)
stranger()