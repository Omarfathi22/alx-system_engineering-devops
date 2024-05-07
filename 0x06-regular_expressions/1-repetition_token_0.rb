#!/usr/bin/env ruby

# Get the argument passed to the script
# Define the regular expression pattern
# Match the pattern in the input
# Print the matched string or empty if not found
input = ARGV[0]
pattern = /School+/
match = input.match(pattern)
puts match ? match[0] : ""

