#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - Print information about a Python list.
 * @p: A pointer to a Python object (assumed to be a list).
 */
void print_python_list(PyObject *p)
{
    setbuf(stdout, NULL);

    if (PyList_Check(p))
    {
        PyObject *item;
        Py_ssize_t size = ((PyVarObject *)p)->ob_size;
        Py_ssize_t i;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++)
        {
            item = ((PyListObject *)p)->ob_item[i];
            printf("Element %ld: %s\n", i, ((PyObject *)item)->ob_type->tp_name);
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
    setbuf(stdout, NULL);

    if (PyBytes_Check(p))
    {
        Py_ssize_t size = ((PyVarObject *)p)->ob_size;
        Py_ssize_t i;
        char *data = ((PyBytesObject *)p)->ob_sval;

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
    setbuf(stdout, NULL);

    if (PyFloat_Check(p))
    {
        printf("[.] float object info\n");
        printf("  value: %.17g\n", ((PyFloatObject *)p)->ob_fval);
    }
    else
    {
        fprintf(stderr, "Invalid Float Object\n");
    }
}
