#include <Python.h>

/**
 * print_python_list - Print information about Python list object
 * @p: PyObject pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, j;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
		{
			printf("  [.] bytes object info\n");
			printf("  size: %ld\n", PyBytes_Size(item));
			printf("  trying string: %s\n", PyBytes_AsString(item));
			printf("  first %ld bytes:", PyBytes_Size(item) + 1 > 10 ? 10 : PyBytes_Size(item) + 1);
			for (j = 0; j < PyBytes_Size(item) + 1 && j < 10; j++)
				printf(" %02x", (unsigned char)PyBytes_AsString(item)[j]);
			printf("\n");
		}
	}
}

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", ((PyVarObject *)p)->ob_size + 1 > 10 ? 10 : ((PyVarObject *)p)->ob_size + 1);
	for (i = 0; i < ((PyVarObject *)p)->ob_size + 1 && i < 10; i++)
		printf(" %02x", (unsigned char)str[i]);
	printf("\n");
}
