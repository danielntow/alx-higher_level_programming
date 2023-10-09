#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: PyObject representing the Python list
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc;
    Py_ssize_t i;
    PyObject *item;

    if (PyList_Check(p))
    {
        size = PyList_Size(p);
        alloc = ((PyListObject *)p)->allocated;
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", alloc);

        for (i = 0; i < size; i++)
        {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    }
}
