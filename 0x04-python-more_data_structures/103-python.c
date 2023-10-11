#include <Python.h>

void print_python_list(PyObject *p)
{
    if (PyList_Check(p))
    {
        Py_ssize_t len = PyList_Size(p);

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", len);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (Py_ssize_t i = 0; i < len; i++)
        {
            PyObject *element = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
            if (PyBytes_Check(element))
            {
                print_python_bytes(element);
            }
        }
    }
}

void print_python_bytes(PyObject *p)
{
    if (PyBytes_Check(p))
    {
        Py_ssize_t size = PyBytes_Size(p);
        char *data = PyBytes_AsString(p);

        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", data);

        if (size >= 10)
        {
            size = 10;
        }
        printf("  first %ld bytes: ", size);
        for (Py_ssize_t i = 0; i < size; i++)
        {
            printf("%02x", data[i] & 0xFF);
            if (i < size - 1)
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    else
    {
        printf("[ERROR] Invalid Bytes Object\n");
    }
}

int main(int argc, char **argv)
{
    Py_Initialize();

    // Create and manipulate Python objects here.
    PyObject *list = PyList_New(0);

    PyObject *str1 = PyUnicode_DecodeUTF8("Holberton", 9, NULL);
    PyList_Append(list, str1);
    PyObject *str2 = PyBytes_FromString("C is fun");
    PyList_Append(list, str2);
    PyObject *str3 = PyUnicode_DecodeUTF8("Python", 6, NULL);
    PyList_Append(list, str3);

    print_python_list(list);

    Py_Finalize();
    return 0;
}
