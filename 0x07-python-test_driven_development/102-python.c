#include <Python.h>

/**
 * print_python_string - Prints a Python string
 * @p: PyObject pointer
 */
void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        PyErr_SetString(PyExc_TypeError, "print_python_string() requires a string");
        return;
    }

    PyObject *ascii_repr = PyObject_Repr(p);
    if (ascii_repr != NULL)
    {
        const char *ascii_str = PyUnicode_AsUTF8(ascii_repr);
        if (ascii_str != NULL)
        {
            printf("String: %s\n", ascii_str);
        }
        Py_DECREF(ascii_repr);
    }
}
