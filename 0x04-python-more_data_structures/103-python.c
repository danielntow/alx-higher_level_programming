#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
* print_python_bytes - Prints info about Python bytes objects
* @p: PyObject
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t i;

(void)p;
printf("[.] bytes object info\n");
printf("  size: %ld\n", PyBytes_Size(p));
printf("  trying string: %s\n", PyBytes_AsString(p));
printf("  first 10 bytes: ");
for (i = 0; i < PyBytes_Size(p) && i < 10; i++)
{
printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
if (i < PyBytes_Size(p) - 1 && i < 9)
	printf(" ");
}
printf("\n");
}

/**
* print_python_list - Prints info about Python lists
* @p: PyObject
*/
void print_python_list(PyObject *p)
{
PyListObject *pl = (PyListObject *)p;
Py_ssize_t size = PyList_Size(p);
Py_ssize_t i;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", pl->allocated);
for (i = 0; i < size; i++)
{
PyObject *item = pl->ob_item[i];
printf("Element %ld: ", i);
if (PyBytes_Check(item))
{
	printf("bytes\n");
	print_python_bytes(item);
}
else if (PyList_Check(item))
	printf("list\n");
else if (PyFloat_Check(item))
	printf("float\n");
else if (PyTuple_Check(item))
	printf("tuple\n");
else if (PyLong_Check(item))
	printf("int\n");
else if (PyUnicode_Check(item))
	printf("str\n");
}
}

