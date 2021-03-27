import { Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-not-found',
  templateUrl: './not-found.component.html',
  styleUrls: ['./not-found.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class NotFoundComponent implements OnInit, OnDestroy {
  constructor() {}

  ngOnInit(): void {
    document.querySelector('html')?.classList.add('not-found');
  }

  ngOnDestroy(): void {
    document.querySelector('html')?.classList.remove('not-found');
  }
}
