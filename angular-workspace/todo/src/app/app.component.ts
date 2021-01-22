import { Component } from '@angular/core';
import { Model } from './model';

@Component({
  selector: 'app-todo',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'todo';
  model = new Model();

  getName(): string {
    return this.model.user;
  }

  getTodoItems(): any {
    // @ts-ignore
    return this.model.items.filter(item => !item.done);
  }
}
