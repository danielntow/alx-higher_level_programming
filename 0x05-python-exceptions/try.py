
import sys
# Printing to the standard output
print("This is regular output")

# Printing an error message to the standard error stream
print("This is an error", file=sys.stderr)
