# Data Structures and Algorithms
Implementations of  Data Structures and Algorithms in JavaScript

<ul>
<li>
<h3><a href="https://github.com/psitronic/Data-Structures-and-Algorithms-in-JS/tree/master/Linked%20Lists">Nodes</a></h3>
<p>
A basic building block for the linked list implementation. Each node contains the list <i>element</i> and <i>pointer</i> - a reference to the next node. It is implemented as a class with the setters and getters to access and modify the element and the pointer:
<ul>
<li><b>get_value()</b> is a getter which return the element value.</li> 
<li><b>get_pointer()</b> is a getter which return the pointer to the next node (next element) in the list.</li>
<li><b>set_pointer(pointer)</b> is a setter which sets the pointer for the current node to the next node.</li>
</ul>
</p>
</li>
<li>
<h3><a href="https://github.com/psitronic/Data-Structures-and-Algorithms-in-JS/tree/master/Linked%20Lists">Singly Linked Lists (unordered)</a></h3>
<p>A singly linked list is a collection of nodes where each node points to the next node. The implemented list operations:
<ul>
<li><b>LinkedList()</b> creates a new empty list.</li>
<li><b>add(element)</b> adds a new element to the list.</li>
<li><b>append(element)</b> adds a new element to the end of the list making it the last element in the list</li>
<li><b>delete(element)</b> removes an element from the list.</li>
<li><b>index(element)</b> returns the position of element in the list.</li>
<li><b>insert(index, element)</b> adds a new element to the list at position index.</li>
<li><b>is_empty</b> checks whether the list is empty.</li>
<li><b>pop()</b> removes and returns the rear (last) element in the list.</li>
<li><b>pop(index)</b> removes and returns the element at the index postion in the list.</li>
<li><b>search(element)</b> searches for the element in the linked list.</li>
<li><b>size()</b> returns the number of elements in the list</li>
<li><b>__str__()</b> returns a string representation of the list.</li>
</ul>
</li>
</ul>