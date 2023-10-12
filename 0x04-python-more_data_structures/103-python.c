#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", Py_SIZE(p));
	printf("  trying string: %s\n", PyUnicode_AsUTF8(p));

	if (Py_SIZE(p) > 10)
	{
		printf("  first 10 bytes: ");
		for (int i = 0; i < 10; i++)
		{
			printf("%02x", bytes->ob_sval[i] & 0xff);
			if (i < 9)
				printf(" ");
		}
		printf("\n");
	}
	else
	{
		printf("  first %ld bytes: ", Py_SIZE(p));
		for (int i = 0; i < Py_SIZE(p); i++)
		{
			printf("%02x", bytes->ob_sval[i] & 0xff);
			if (i < Py_SIZE(p) - 1)
				printf(" ");
		}
		printf("\n");
	}
}


/**
 * print_python_list - Print information about Python list object
 * @p: PyObject pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));

	for (Py_ssize_t i = 0; i < Py_SIZE(p); i++)
	{
		PyObject *element = list->ob_item[i];

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
