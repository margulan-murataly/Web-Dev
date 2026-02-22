import { Component } from "@angular/core";
import {Comments} from './comm';

@Component({
    selector: 'app-root',
    standalone: true,
    template: `
        <div>
        <h1>How I feel about Angular</h1>
        <article></article>
        <comments />
        </div>`,
        imports: [Comments],
})

export class App{
    
}