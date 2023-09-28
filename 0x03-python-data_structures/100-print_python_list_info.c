#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function
 * @p:vp1.
 */
void print_python_list_info(PyObject *p)
{
    int list_size, allocated, hat;
    PyObject *list_object;

    list_size = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", allocated);

    for (hat = 0; hat < list_size; hat++)
    {
        printf("Element %d: ", hat);

        list_object = PyList_GetItem(p, hat);
        printf("%s\n", Py_TYPE(list_object)->tp_name);
    }
}
