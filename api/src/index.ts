import express, { Request, Response, NextFunction } from 'express';

const app  = express();
const port = 3000;

app.listen(port, () => {
  console.log(`Timezones by location app is running on port ${port}.`)
});

interface LocationWithTimezone {
  location: string;
  timezoneName: string;
  timezoneAbbr: string;
  utcOffset: number;
}

const getLocationsWithTimezones = (
  request: Request,
  response: Response,
  next: NextFunction
) => {
  let locations: LocationWithTimezone[] = [
    {
      location: 'France',
      timezoneName: 'Central European Time',
      timezoneAbbr: 'CET',
      utcOffset: 1
    },
    {
      location: 'New England',
      timezoneName: 'China Standard Time',
      timezoneAbbr: 'CST',
      utcOffset: 8
    },
    {
      location: 'Old England',
      timezoneName: 'Argentina Time',
      timezoneAbbr: 'ART',
      utcOffset: -3
    },
    {
      location: 'Japan',
      timezoneName: 'Japan Standard Time',
      timezoneAbbr: 'JST',
      utcOffset: 9
    }
  ];

  response.status(200).json(locations);
}

app.get('/timezones', getLocationsWithTimezones);

module.exports = app;
