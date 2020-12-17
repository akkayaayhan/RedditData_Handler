# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:58:01 2020

@author: virgi
"""
from src.reddit_handler import RedditHandler
from src.polarization_classifier import PolarizationClassifier
from src.textstatistics_generator import TextStatisticGenerator

out_folder = 'RedditHandler_Outputs'
extract_post = True # True if you want to extract Post data, False otherwise
extract_comment = True # True if you want to extract Comment data, False otherwise
category = {'Anxiety':['Anxiety', 'Anxietyhelp','anxietysuccess','anxietysupporters','socialanxiety','Healthanxiety','ptsd','PTSDCombat','CPTSD','traumatoolbox','PanicParty','domesticviolence'],'Depression':['depression','depressionregimens','depression_help','StopSelfHarm','SuicideWatch','EOOD','GFD','sad','reasonstolive','selfharm','SelfHarmCommunity','lonely']}
start_date = '01/05/2018'
end_date = '01/07/2018'
n_months = 1  # time_period to consider: if you don't want it n_months = 0
# default post attributes
post_attributes = ['id','author', 'created_utc', 'num_comments', 'over_18', 'is_self', 'score', 'selftext', 'stickied', 'subreddit', 'subreddit_id', 'title']
# default comment attributes
comment_attributes = ['id', 'author', 'created_utc', 'link_id', 'parent_id', 'subreddit', 'subreddit_id', 'body', 'score']
my_handler = RedditHandler(out_folder, extract_post, extract_comment, category, start_date, end_date, n_months=n_months, post_attributes=post_attributes, comment_attributes=comment_attributes)
my_handler.extract_data()
my_handler.create_network()

#PolarizationClassifier

file_model = 'Model/model_glove.json'
file_weights = 'Model/model_glove.h5'
file_tokenizer = 'Model/tokenizer_def.pickle'

my_pol_classifier = PolarizationClassifier(out_folder, extract_post, extract_comment, category, start_date, end_date, file_model, file_weights, file_tokenizer)
my_pol_classifier.compute_polarization()

#TextStatisticGenerator
my_stats_generator = TextStatisticGenerator(out_folder, extract_post, extract_comment, category, start_date, end_date)
my_stats_generator.extract_statistics()
