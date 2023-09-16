#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - fdsfsc
 * @p:vp1
 * Return: oo
 */
void print_python_bytes(PyObject *p)
{
	char *sa;
	long int si, ha, ff;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	si = ((PyVarObject *)(p))->ob_size;
	sa = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", si);
	printf("  trying string: %s\n", sa);

	if (si >= 10)
		ff = 10;
	else
		ff = si + 1;

	printf("  first %ld bytes:", ff);

	for (ha = 0; ha < ff; ha++)
		if (sa[ha] >= 0)
			printf(" %02x", sa[ha]);
		else
			printf(" %02x", 256 + sa[ha]);

	printf("\n");
}

/**
 * print_python_list - hafunction 2
 * @p: vp1
 * Return: oo
 */
void print_python_list(PyObject *p)
{
	long int size, ha;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (ha = 0; ha < size; ha++)
	{
		obj = ((PyListObject *)p)->ob_item[ha];
		printf("Element %ld: %s\n", ha, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
}
}
