# Database documentation

## `incident_reports` table

This table presents all the incidents that have involved an intervention of the Boston police over the sample period.

One row corresponds to one incident, identified by its alpha-numeric `INCIDENT_NUMBER`.

The following fields are available:

- `OFFENSE_CODE_GROUP`: a text column that describes the nature of the incident (with a limited number of unique incident categories);


- `DISTRICT`: the alpha-numeric code of the police district involved in the incident;


- `SHOOTING`: indicator variable that takes value 1 if and only if the incident involved gunfires;


- `OCCURED_ON_DATE`: the date and time (timestamp stored as text) when the incident was reported;


- `LAT`: latitude of the point where the incident took place;


- `LON`: longitude of the point where the incident took place.


## `districts` table

This table gathers key information about the police districts of Boston.

One row corresponds to one district, identified by its alpha-numeric `CODE`.

The following fields are availabl:

- `NAME`: the full-text name of the district;


- `LAT_POLICE_STATION`: the latitude of the police station of the district;


- `LONG_POLICE_STATION`: the longitude of the police station of the district.


## `indicators` table

This table gathers key socio-economic characteristics of Boston's various police districts.

One row corresponds to one district, identified by its alpha-numeric `CODE`.

The following fields are available:

- `MEDIAN_AGE`: the average median age (computed at each year end) of the population of the district over the 2015-2019 period;


- `TOTAL_POP`: the average total population of the district (measured at each year end) over the 2015-2019 period;


- `PERC_OF_30_34`: the average percentage of people between 30 and 34 years old over the 2015-2019 period in the district considered;


- `PERC_MARRIED_COUPLE_FAMILY`: the percentage, among all households in the districts, of married-couple families averaged over the 2015-2019 period;


- `PER_CAPITA_INCOME`: the average per-capita income (average income per person) in the district over the 2015-2019;


- `PERC_OTHER_STATE_OR_ABROAD`: the percentage of the district's residents having moved in from abroad or from another US state less than one year ago, averaged over the 2015-2019 period;


- `PERC_LESS_THAN_HIGH_SCHOOL`: the percentage of the district's residents having not obtained a high school degree averaged over the 2015-2019 period;


- `PERC_COLLEGE_GRADUATES`: the percentage of the district's residents having completed a college degree averaged over the 2015-2019.
