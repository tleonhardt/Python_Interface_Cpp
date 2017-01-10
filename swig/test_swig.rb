#!/usr/bin/env ruby

# The feature name begins with a lowercase letter...
require 'fibonacci'

# ... but the module name begins with an uppercase letter
puts "fib(20): #{Fibonacci.compute_fibonacci(20)}"
