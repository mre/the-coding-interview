const reverse_string = (word) => {
  if (typeof word === 'string') {
    return word.split("").reverse().join("")
  } else {
    return "Must String!"
  }
}

reverse_string("Hello World")