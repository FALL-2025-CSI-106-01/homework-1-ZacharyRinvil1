var1 = "hello"

def my_function(var1):
  global var1
  var1 = 'goodbye'
  
var1 = my_function(var1)
print(var1)