# Remove the C binary
rm fibonacci_c

# Cleanup SWIG wrapper stuff
rm -rf build
rm *.egg-info
rm *.so
rm fibonacci.py
rm fibonacci_wrap.c

# Remove *.pyc files
rm -rf __pycache__
