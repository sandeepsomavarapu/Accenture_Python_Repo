def f(a, L=5):
	res=a+L
	print(res)
f(40)
def arbitaryArgumentsFunction(*args):
	print(args[0]+" "+args[1])

def my_function(**kid):#keyword and arbitary arguments
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
    
def f1(b=10, L=10):#keyword arguments
	res=b+L
	print(res)

f1(L=50,b=30)
arbitaryArgumentsFunction("sandeep","naresh","suresh")