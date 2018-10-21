const split_string = (word, delimeter) => {
  if (typeof word === 'string' && typeof delimeter === 'string') {
    return word.split(delimeter)
  } else {
    return "Must Word and Delimeter must String!";
  }
}