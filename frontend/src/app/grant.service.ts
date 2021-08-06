import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from './../environments/environment';
import { Grant } from './grant';

@Injectable({
  providedIn: 'root',
})
export class GrantService {
  private grantsUrl = `${environment.api_root}/grants`;

  constructor(private http: HttpClient) {}

  getGrants(): Observable<Grant[]> {
    return this.http.get<Grant[]>(this.grantsUrl);
  }
}
