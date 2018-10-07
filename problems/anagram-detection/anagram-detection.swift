//
//  main.swift
//  Anagram Detection
//
//  Created by Abdul Fattah Ikhsan on 7/10/18.
//  Copyright © 2018 ShareLah. All rights reserved.
//

import Foundation

func hashString(_ str: String) -> Int {
    let charMap: [String: Int] = [
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29,
        "k": 31,
        "l": 37,
        "m": 41,
        "n": 43,
        "o": 47,
        "p": 53,
        "q": 59,
        "r": 61,
        "s": 67,
        "t": 71,
        "u": 73,
        "v": 79,
        "w": 83,
        "x": 89,
        "y": 97,
        "z": 101,
        "A": 103,
        "B": 107,
        "C": 109,
        "D": 113,
        "E": 127,
        "F": 131,
        "G": 137,
        "H": 139,
        "I": 149,
        "J": 151,
        "K": 163,
        "L": 167,
        "M": 173,
        "N": 179,
        "O": 181,
        "P": 191,
        "Q": 193,
        "R": 197,
        "S": 199,
        "T": 211,
        "U": 223,
        "V": 227,
        "W": 229,
        "X": 233,
        "Y": 239,
        "Z": 241
    ]
    let chars = str.map { String($0) }
    return chars.reduce(1, { (memo, char) in
        return memo * charMap[char]!
    })
}

func anagramDetection(parent: String, child: String) -> Int {
    let length = child.count
    let anagram = hashString(child)
    var total = 0
    for i in 0...parent.count - length {
        let startIndex = parent.index(parent.startIndex, offsetBy: i)
        let endIndex = parent.index(parent.startIndex, offsetBy: (i + length))
        let range = startIndex..<endIndex
        let substring = String(parent[range])
        if hashString(substring) == anagram {
            total += 1
        }
    }
    return total
}
