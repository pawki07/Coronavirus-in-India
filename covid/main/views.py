from django.shortcuts import render
import requests
import json

def home(request):
	url = "https://covid-193.p.rapidapi.com/statistics"

	querystring = {"country":"India"}

	headers = {
    	'x-rapidapi-host': "covid-193.p.rapidapi.com",
    	'x-rapidapi-key': "24e4e3e223msh29ae7000435645ep1f166fjsn4df418b6b3ca"
    }

	response = requests.request("GET", url, headers=headers, params=querystring).json()

	data = response['response']

	d = data[0]

	print(d)

	context = {
	'all': d['cases']['total'],
	'recovered':d['cases']['recovered'],
	'deaths':d['deaths']['total'],
	'new':d['cases']['new'],
	'critical':d['cases']['critical']
	}

	return render(request, 'index.html', context)
