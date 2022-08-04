from actualDLL import DLL

Dll = DLL()
Dll.append(5)

Dll.push(9)

Dll.push(3)

Dll.append(7)

Dll.insertAfter(Dll.head.next, 8)

print(f"The created Dll is: ")
Dll.printList(Dll.head)
