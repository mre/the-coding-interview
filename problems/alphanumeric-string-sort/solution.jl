#!/usr/bin/env julia

input = join(sort(split(ARGS[1], "")))

upper = IOBuffer()
lower = IOBuffer()
even = IOBuffer()
odd = IOBuffer()

for c in input
    if 'a' <= c && c <= 'z'
        print(lower, c)
    elseif 'A' <= c && c <= 'Z'
        print(upper, c)
    elseif occursin(c, "02468")
        print(even, c)
    else
        print(odd, c)
    end
end

print(String(take!(lower)))
print(String(take!(upper)))
print(String(take!(even)))
print(String(take!(odd)))
println()
