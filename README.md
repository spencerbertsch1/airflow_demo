# airflow demo

Simple Airflow Demo using Plotly/Dash Stock viewer 

This simple dashboard was used as a quick way to get used to implementing 
airflow DAGs to automate the process of refreshing datasets overnight.

There are two things which whould happen every night for this dashboard 
to function normally: pull_data.main() needs to get called, and 
clean_data.main() needs to get called. 

pull_data.main() >> clean_data.main()
