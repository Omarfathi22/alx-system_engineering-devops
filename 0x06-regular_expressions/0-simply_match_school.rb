#!/usr/bin/env ruby

# Get the argument passed to the script
# Define the regular expression pattern
# Match the pattern in the input
# Print the matched string or empty if not found
puts ARGV[0].scan(/School/).join
