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

  /**
   * @todo Previously, this was typed as Observable<Grant[]>,
   * and we'd like it to be strongly typed that way again.
   *
   * Possible solutions include chaining promises so that by
   * the time getGrants returns an Observable, we've pulled
   * the data out of the JSON:API 'data' key.
   *
   * Implementing a [JSON:API client library][clients] might obviate the
   * need for this typing work.
   * [clients]: https://jsonapi.org/implementations/#client-libraries-typescript
   */
  getGrants(): Observable<any> {
    return this.http.get(this.grantsUrl);
  }
}
