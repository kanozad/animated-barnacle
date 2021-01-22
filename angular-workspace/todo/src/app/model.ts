export class Model {
  user;
  items: any;

  constructor() {
    this.user = 'Melvin';
    this.items = [new TodoItem('Buy Flowers', false),
      new TodoItem('Eat wax', true),
      new TodoItem('Trim nose hair', false),
      new TodoItem('Call Dentist', false)];
  }
}

export class TodoItem {
  action;
  done;

  constructor(action: any, done: any) {
    this.action = action;
    this.done = done;
  }
}
