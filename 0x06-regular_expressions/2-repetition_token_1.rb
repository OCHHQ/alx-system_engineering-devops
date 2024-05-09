#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: ./1-repetition_token_1.rb <string>"
  exit 1
end

input_string = ARGV[0]

regex = /h(bt+)?n/

if input_string.match?(regex)
  puts input_string
else
  puts "No match found."
end
