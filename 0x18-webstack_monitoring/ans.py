from datadog import api

# Initialize the Datadog API client with your API key and application key
api_key = '4adb6382e6a0adbf3cbd962876c8b81e'
app_key = '883379f481cdc757dc24c1d1ebd5baa0b6b52d97'
api = api.DatadogApi(api_key, app_key)

# Retrieve the list of dashboards
dashboards = api.Dashboard.get_all()

# Loop through the dashboards and find the one you created earlier
for dashboard in dashboards['dashboards']:
    if dashboard['title'] == "Kelvin D":
        dashboard_id = dashboard['id']
        print("Dashboard ID:", dashboard_id)
        break
