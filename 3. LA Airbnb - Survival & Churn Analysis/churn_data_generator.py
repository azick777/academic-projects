import pandas as pd
import numpy as np

churn_list=[]
for i in range(1,6):
    filename1=f'Data/calendar_20200{i}.csv'
    list_df= pd.read_csv(filename1)
    list_id=list_df.listing_id.unique()
    filename2=f'Data/calendar_20200{i+1}.csv'
    list_df2= pd.read_csv(filename2)
    df_tmp=list_df2[~list_df2.listing_id.isin(list_id)]['listing_id']
    list_id2=df_tmp.unique()
    print(f'{i}. {filename1} vs {filename2} > Found Churn {len(list_id2)}')
    churn_list.extend(list_id2)
print(f'ChurnList: {len(churn_list)}')
churn_list = np.unique(churn_list)
print(f'ChurnList Unique: {len(churn_list)}')

final_data= pd.read_csv(f'final_data_airbnb_covid.csv').drop(columns=['Unnamed: 0']).sort_values('Date').drop_duplicates(keep='last')


final_data=final_data.groupby('id').agg({
                         'suceessful':'sum', 
                         'Date':'last', 
                         'revenue': 'sum', 
                         'covid_cases_zip': 'last', 
                         'covid_cases_city': 'last', 
                         'covid_cases_state': 'last', 
                         'covid_cases_usa': 'last', 
                         'reviews_per_month': 'last', 
                         'review_scores_rating': 'mean', 
                         'number_of_reviews_ltm': 'last', 
                         'review_scores_accuracy': 'last', 
                         'number_of_reviews':  'last', 
                         'review_scores_cleanliness':  'last',
                         'review_scores_checkin':  'last',
                         'review_scores_communication':  'last', 
                         'review_scores_location':  'last', 
                         'review_scores_value':  'last',
                         'calculated_host_listings_count':  'last',
                         'calculated_host_listings_count_entire_homes':  'last',
                         'calculated_host_listings_count_private_rooms':  'last',
                         'host_response_time': 'mean',
                         'host_response_rate': 'mean', 
                         'host_acceptance_rate': 'mean',
                         'host_is_superhost': 'last',
                         'zipcode': 'last',
                         'security_deposit': 'last',
                         'cleaning_fee': 'last',
                         'guests_included': 'last',
                         'extra_people': 'last',
                         'minimum_nights': 'last',
                         'minimum_minimum_nights': 'mean',
                         'maximum_minimum_nights': 'mean',
                         'minimum_maximum_nights': 'mean',
                         'maximum_maximum_nights': 'mean',
                         'minimum_nights_avg_ntm': 'mean',
                         'maximum_nights_avg_ntm': 'mean',
                         'availability_365': 'last'})

final_data['churn']=np.where(final_data.index.isin(churn_list), 1, 0)
final_data = final_data.reset_index()
final_data.to_csv('airbnb_customer_exist.csv')
