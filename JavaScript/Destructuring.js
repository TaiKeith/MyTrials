const user = { name: 'Keith', age: 23 };
const { name, age } = user;
console.log(user.name)

const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80
};

const { today, tomorrow } = HIGH_TEMPERATURES;
console.log(HIGH_TEMPERATURES.today)
console.log(HIGH_TEMPERATURES.tomorrow)
