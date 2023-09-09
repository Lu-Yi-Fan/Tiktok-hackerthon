import pandas as pd
import ast

ads = pd.read_excel('ad_df_gb.xlsx')
mod = pd.read_excel('mod_df_lr.xlsx')
mod["market"] = mod["queue_market"].apply(lambda x: ast.literal_eval(x))

country_moderator_dict = {}
for index, row in mod.iterrows():
    countries = row['market']
    moderator_id = row['moderator']
    y_pred = row['mod_score_pred']

    for country in countries:
        # Check if the country is already in the dictionary
        if country in country_moderator_dict:
            country_moderator_dict[country].append((moderator_id,y_pred))
        else:
            # If the country is not in the dictionary, create a new entry with a list containing the moderator_id
            country_moderator_dict[country] = [(moderator_id,y_pred)]


mod_sorted_dict = {
    country: sorted(ad_data, key=lambda x: x[1], reverse=True)
    for country, ad_data in country_moderator_dict.items()
}



ads_dict = {}
for index, row in ads.iterrows():
    ad_id = row['ad_id']
    y_pred = row['ad_score_pred']
    country =  row['delivery_country']
    if country in ads_dict:
        ads_dict[country].append((ad_id,y_pred))
    else:
        ads_dict[country] = [(ad_id,y_pred)]

ads_sorted_dict = {
    country: sorted(ad_data, key=lambda x: x[1], reverse=True)
    for country, ad_data in ads_dict.items()
}




print(ads_sorted_dict)




mod_sorted_dict