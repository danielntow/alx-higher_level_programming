#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (Py_ssize_t i = 0; i < size; i++)
		{
			PyObject *item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		printf("[ERROR] Invalid Python List\n");
	}
}

/**
 * print_python_list - Print information about Python list object
 * @p: PyObject pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		printf("[.] bytes object info\n");
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first 10 bytes: ");
		if (size < 10)
		{
			for (Py_ssize_t i = 0; i < size; i++)
			{
				printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
				if (i < size - 1)
				{
					printf(" ");
				}
			}
			printf("\n");
		}
		else
		{
			for (Py_ssize_t i = 0; i < 10; i++)
			{
				printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
				if (i < 9)
				{
					printf(" ");
				}
			}
			printf("\n");
		}
	}
	else
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
}