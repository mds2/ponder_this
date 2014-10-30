#!/bin/ruby

cubes = $stdin.readlines.map{ |l| l.split " "}

puts "There are " + cubes.length.to_s + " cubes"
puts "Cube with minimum sides has " + cubes.map{|c| c.length}.min.to_s + " sides"
puts "Cube with maximum sides has " + cubes.map{|c| c.length}.max.to_s + " sides"

0.upto(cubes.length() - 1).each do |i|
  (i + 1).upto(cubes.length() - 1).each do |j|
    shared_count = cubes[i].map { |s|
      if cubes[j].include? s then 1 else 0 end
    }.reduce { |x, y| x + y}
    if shared_count != 1
      puts "cubes (" + cubes[i].join(",") + ") and (" + cubes[j].join(",") + ")"
      puts "share " + shared_count.to_s + " sides"
    end
  end
end

