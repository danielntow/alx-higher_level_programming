#include <Python.h>

/**
* print_python_list - Print information about a Python list.
* @p: A pointer to a Python object (assumed to be a list).
*/
void print_python_list(PyObject *p)
{
if (PyList_Check(p))
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
else
{
	fprintf(stderr, "Invalid List Object\n");
}
}

/**
* print_python_bytes - Print information about a Python bytes object.
* @p: A pointer to a Python object (assumed to be bytes).
*/
void print_python_bytes(PyObject *p)
{
if (PyBytes_Check(p))
{
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  Size: %ld\n", size);
	printf("  trying string: %s\n", data);
	printf("  first %ld bytes: ", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", data[i]);
		if (i < 9 && i < size - 1)
		{
			printf(" ");
		}
	}
	printf("\n");
}
else
{
	fprintf(stderr, "Invalid Bytes Object\n");
}
}

/**
* print_python_float - Print information about a Python float object.
* @p: A pointer to a Python object (assumed to be a float).
*/
void print_python_float(PyObject *p)
{
if (PyFloat_Check(p))
{
	printf("[.] float object info\n");
	printf("  value: %.17g\n", PyFloat_AsDouble(p));
}
else
{
	fprintf(stderr, "Invalid Float Object\n");
}
}

