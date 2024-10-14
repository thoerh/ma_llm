
circulating_nurse.move([3,2])
patient1.position_for_surgery([1.5,1], [0.5,1])
robot1.move([3,1])
robot1.attach_tool(drill)
robot1.detach_tool()
scalpel.move([3,2])

print(initialize.print_dictionary(initialize.objects))
print(initialize.objects[head_surgeon])
print(initialize.objects[head_surgeon]['position'])
print(initialize.print_dictionary(initialize.objects))
print(head_surgeon.position)
print(head_surgeon.tiredness_level)