import requests
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
from datetime import datetime
import os

ASSET_PATH = os.path.join('..', 'assets', 'figures', 'Hosps_and_cases_vs_vacc_rate.html')

def normalize_rate(vacc_status, value, vacc_rate, pop_total = 8604495, normal_denominator = 100000):
    vacc_rate = vacc_rate/100.
    if vacc_status == 'Fully Vaccinated (2 doses)':
        normalized_value = value * normal_denominator / (pop_total*vacc_rate)
    else:
        normalized_value = value * normal_denominator / (pop_total*(1-vacc_rate))
    return normalized_value

url_new_cases = 'https://msss.gouv.qc.ca/professionnels/statistiques/documents/covid19/COVID19_Qc_RapportINSPQ_CasSelonStatutVaccinalEtAge.csv'
url_new_hosp = 'https://msss.gouv.qc.ca/professionnels/statistiques/documents/covid19/COVID19_Qc_RapportINSPQ_HospitalisationsSelonStatutVaccinalEtAge.csv'

r = requests.get(url_new_cases)
open('COVID19_Qc_RapportINSPQ_CasSelonStatutVaccinalEtAge.csv', 'wb').write(r.content)
r = requests.get(url_new_hosp)
open('COVID19_Qc_RapportINSPQ_HospitalisationsSelonStatutVaccinalEtAge.csv', 'wb').write(r.content)

# Manually download the CSV file of plot 2.1 @ https://www.inspq.qc.ca/covid-19/donnees/vaccination.
# To download the CSV, clikc the three dots and "Télécharger les données en format CSV".
# Finally, rename that file to "vaccination.csv".

df_hosp = pd.read_csv('COVID19_Qc_RapportINSPQ_HospitalisationsSelonStatutVaccinalEtAge.csv')
df_cases = pd.read_csv('COVID19_Qc_RapportINSPQ_CasSelonStatutVaccinalEtAge.csv')
df_vaccination = pd.read_csv('vaccination.csv')

df_hosp = pd.DataFrame(df_hosp.groupby(['Date','Statut_Vaccinal'])['Nb_Nvelles_Hosp'].sum()).reset_index()
df_cases = pd.DataFrame(df_cases.groupby(['Date','Statut_Vaccinal'])['Nb_Nvx_Cas'].sum()).reset_index()
df_vaccination = df_vaccination.rename(columns={"Date de vaccination": "Date",
                                                "Ensemble du Québec": 'taux_vacc_tous',
                                                '12 ans et plus' : 'taux_vacc_12plus'})
df_vaccination = df_vaccination[['Date', 'taux_vacc_tous', 'taux_vacc_12plus']]

# Convert Date to datetime object to normalize the format
df_hosp['Date'] = pd.to_datetime(df_hosp['Date'])
df_cases['Date'] = pd.to_datetime(df_cases['Date'])
df_vaccination['Date']  = pd.to_datetime(df_vaccination['Date'] )

# Merge on Date
df_hosp = pd.merge(df_hosp,df_vaccination,on='Date')
df_cases = pd.merge(df_cases,df_vaccination,on='Date')

# Drop statut vaccinal 1 dose
df_hosp = df_hosp[df_hosp['Statut_Vaccinal']!= 'Vacciné 1 dose'].reset_index().drop(columns=['index'])
df_cases = df_cases[df_cases['Statut_Vaccinal']!= 'Vacciné 1 dose'].reset_index().drop(columns=['index'])

vaccinal_status_to_english = {'Non-vacciné':'Unvaccinated', 'Vacciné 2 doses': 'Fully Vaccinated (2 doses)'}
df_hosp['Statut_Vaccinal'] = df_hosp['Statut_Vaccinal'].replace(vaccinal_status_to_english)
df_cases['Statut_Vaccinal'] = df_cases['Statut_Vaccinal'].replace(vaccinal_status_to_english)
df_hosp = df_hosp.rename(columns={"Statut_Vaccinal": "Vaccine_Status"})
df_cases = df_cases.rename(columns={"Statut_Vaccinal": "Vaccine_Status"})

df_hosp['Normalized_Hosps'] = df_hosp.apply(lambda row: normalize_rate(row['Vaccine_Status'],
                                                                       row['Nb_Nvelles_Hosp'],
                                                                       row['taux_vacc_tous']), axis=1)
df_cases['Normalized_Cases'] = df_cases.apply(lambda row: normalize_rate(row['Vaccine_Status'],
                                                                       row['Nb_Nvx_Cas'],
                                                                       row['taux_vacc_tous']), axis=1)
# Rolling X day average new hosps
df_hosp['Normalized_Hosps'] = pd.to_numeric(df_hosp['Normalized_Hosps'])
df_cases['Normalized_Cases']= pd.to_numeric(df_cases['Normalized_Cases'])
for i in range(14):
    window = i+1
    df_hosp[f'Moving Average {window}d'] = df_hosp.groupby('Vaccine_Status')['Normalized_Hosps'].transform(lambda x: x.rolling(window).mean())
    df_cases[f'Moving Average {window}d'] = df_cases.groupby('Vaccine_Status')['Normalized_Cases'].transform(lambda x: x.rolling(window).mean())

# Figure 1
fig1 = px.line(df_hosp, x='Date', y='Moving Average 7d', color='Vaccine_Status')
fig1.update_traces(showlegend=False) # to avoid having 2 legends for each of fig 1 and fig 2. Fig2's legend is used implicitly

# Figure 2
fig2 = px.line(df_cases, x='Date', y='Moving Average 7d', color='Vaccine_Status')
fig2.update_layout(showlegend=False)
# Get data and traces
figure1_traces = []
figure2_traces = []
for trace in range(len(fig1["data"])):
    figure1_traces.append(fig1["data"][trace])
for trace in range(len(fig2["data"])):
    figure2_traces.append(fig2["data"][trace])

#Create a 1x2 subplot
final_fig = sp.make_subplots(rows=1, cols=2,
                             subplot_titles=['New Hospitalizations per 100,000 (7-day Moving Avg)','New Cases per 100,000 (7-day Moving Avg)'])

# Get the Express fig broken down as traces and add the traces to the proper plot within in the subplot

for traces in figure1_traces:
    final_fig.append_trace(traces, row=1, col=1)
for traces in figure2_traces:
    final_fig.append_trace(traces, row=1, col=2)

final_fig.update_layout(
                   xaxis1_title='Date',
                   yaxis1_title='Daily Hospitalizations',
                   xaxis2_title='Date',
                   yaxis2_title='Daily Cases',
                  hovermode="x unified",
                  title_text=f"Overview of Covid Cases & Hospitalizations in Quebec, CA by Vaccine Status ({datetime.today().strftime('%d/%m/%Y')})",
                    title_x=0.5
                  )
final_fig.update_annotations(font_size=12)
final_fig.update_xaxes(nticks=20)
final_fig.update_xaxes(rangeslider_visible=True)
final_fig.add_annotation(
    text = ("Hospitalization & Cases Data:  https://www.donneesquebec.ca/recherche/dataset/covid-19-portrait-quotidien-des-cas-confirmes<br>"
            "Vaccination Status Data: https://www.inspq.qc.ca/covid-19/donnees/vaccination (Figure 2.1)"),
    showarrow=False,
    xref='x domain',
    x=0,
    yref='y domain',
    y=-0.55,
    font=dict(size=9, color="grey"),
    align="left",)

final_fig.write_html(ASSET_PATH)
