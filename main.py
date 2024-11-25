result = 0;

num = input("enter a number : ");
num2 = input("enter a second number : ");
opname = input("enter an operation (addition, subtraction, multiplication, or division) : ");

if opname == 'addition':
	result = int(num) + int(num2);
	print(num + " + " + num2 + " = " + str(result));
elif opname == 'subtraction':
	result = int(num) - int(num2);
	print(num + " - " + num2 + " = " + str(result));
elif opname == 'multiplication':
	result = int(num) * int(num2);
	print(num + " * " + num2 + " = " + str(result));
elif opname == 'division':
	result = int(num) // int(num2);
	print(num + " //" +  num2 + " = " + str(result));
else:
	result = 'invalid operation'
	print(result)
