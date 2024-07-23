//template literals; Backtick-quoted strings i.e `....`
//-> They can span lines and also Embed other values
//When you write sth inside ${} in a template literal, its result will be
//"computed, converted to a string, and included at that position"
const text = `half of 100 is ${100 / 2}`

console.log(text)
