import { Component, OnInit } from '@angular/core';
import { Grant } from '../grant';
import { GrantService } from '../grant.service';

@Component({
  selector: 'app-grants',
  templateUrl: './grants.component.html',
  styleUrls: ['./grants.component.css'],
})
export class GrantsComponent implements OnInit {
  grants: Grant[] = [];

  constructor(private grantService: GrantService) {}

  ngOnInit(): void {
    this.getGrants();
  }

  getGrants(): void {
    this.grantService
      .getGrants()
      .subscribe((response) => (this.grants = response.data));
  }
}
