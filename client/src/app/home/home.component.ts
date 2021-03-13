import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import ResponseUserData from './home.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent implements OnInit {
  userData: ResponseUserData;

  constructor(private route: ActivatedRoute, private cd: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.userData = this.route.snapshot.data as ResponseUserData;
    this.cd.detectChanges();
  }
}
