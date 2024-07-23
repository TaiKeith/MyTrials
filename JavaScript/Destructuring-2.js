const user = { name: 'Keith', age: 23 };
const { name: userName, age: userAge } = user;
console.log(userName)

const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80
};

const { today: highToday, tomorrow: highTomorrow } = HIGH_TEMPERATURES;
console.log(highToday)
console.log(highTomorrow)
