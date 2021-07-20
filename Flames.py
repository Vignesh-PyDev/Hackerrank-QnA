from itertools import cycle
import itertools


Name_1 = list(''.join(I1 for I1 in input("Enter Your Name :").lower()))

Name_2 = list(''.join(e for e in input("Enter Your Partner Name :").lower()))

Flames_List = ["Friendship","Love","Affection","Marriage","Enemy","Siblings"]

Flames_Dict = {Output_List_1[x]:Flames_List[x] for x in range(len(Flames_List))}

Output_List_1 = ['F','L','A','M','E','S']


for x in Name_1:

	for y in Name_2:

		if x in y:

			Name_1.remove(x),Name_2.remove(y)

			break


def cycle_Flames(*List):

	List = list(List[0])

	# print(List)

	if len(List) == 1:

		return List[0]

	elif len(List) >= 1:

		list_cycle = itertools.cycle(List)		

		for i in range(len(Name_1+Name_2)):

			next_element = next(list_cycle)

			Index = List.index(next_element)

		List.remove(next_element)

		Temp_List = []

		for i in range(len(List)):

			Temp_List.append(List[Index % len(List)])

			Index += 1

		return cycle_Flames(Temp_List)

		

print(cycle_Flames(Output_List_1),'-->',Flames_Dict[cycle_Flames(Output_List_1)])