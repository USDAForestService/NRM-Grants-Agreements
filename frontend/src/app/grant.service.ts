import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from './../environments/environment';
import { Grant } from './grant';

@Injectable({
  providedIn: 'root',
})

/**
 * @todo Get the JSON from they key "data"
 */
export class GrantService {
  private grantsUrl = `${environment.api_root}/grants`;

  constructor(private http: HttpClient) {}

  getGrants(): Observable<any> {
    return this.http.get(this.grantsUrl);
  }
}
