import numpy as np
import pandas as pd

import os


def load_crime_data():
    path = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(path, 'data', 'incident_reports.csv')

    df = pd.read_csv(path)

    return df.copy()


def load_district_table():
    path = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(path, 'data', 'districts.csv')

    df = pd.read_csv(path)

    return df.copy()


def load_regression_features():

    path = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(path, 'data', 'indicators.csv')

    df = pd.read_csv(path)

    return df.copy()


def load_regression_data():

    regression_features_df = load_regression_features()
    crime_reports_df = load_crime_data()
    districts_df = load_district_table()

    per_district_crimes = crime_reports_df.groupby('DISTRICT').count().reset_index()[['DISTRICT', 'INCIDENT_NUMBER']]

    regression_data = regression_features_df.merge(
        per_district_crimes,
        how='inner',
        left_on='CODE', right_on='DISTRICT'
    )

    regression_data.drop(columns='DISTRICT', inplace=True)

    regression_data = regression_data.merge(
        districts_df[['CODE', 'NAME']],
        how='left',
        on='CODE'
    )

    regression_data.rename(
        columns={'INCIDENT_NUMBER': 'NB_INCIDENTS'},
        inplace=True
    )

    # regression_data['LOG_NB_INCIDENTS'] = np.log(regression_data['NB_INCIDENTS'])

    return regression_data.copy()


def load_logistic_regression_data():

    crime_reports_df = load_crime_data()
    district_table = load_district_table()

    shootings_df = crime_reports_df.merge(
        district_table,
        how='inner',
        left_on='DISTRICT', right_on='CODE')

    shootings_df = shootings_df[['SHOOTING', 'NAME']].copy()

    return shootings_df.copy()


def load_data_viz_data():

    crime_reports_df = load_crime_data()
    district_table = load_district_table()

    crime_reports_df = crime_reports_df.merge(
        district_table[['CODE', 'NAME', 'LAT_POLICE_STATION', 'LONG_POLICE_STATION']],
        how='inner',
        left_on='DISTRICT', right_on='CODE'
    )

    crime_reports_df.drop(columns=['DISTRICT', 'CODE'], inplace=True)

    return crime_reports_df.copy()
