from django.shortcuts import render, HttpResponse
import requests
from newsapi import NewsApiClient
import json
from covid import Covid



# Create your views here.

def index(request):
    covid = Covid()  

    #India
    india_cases = covid.get_status_by_country_name("India")

    india_confirmed = india_cases['confirmed']
    india_active = india_cases['active']
    india_deaths = india_cases['deaths']
    india_recovered = india_cases['recovered']

    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    data = response.json()

    #print(data)

    maharashtra = data["Maharashtra"]['districtData']
    andaman_n = data["Andaman and Nicobar Islands"]['districtData']
    andhra_p = data["Andhra Pradesh"]['districtData']
    arunachal_p = data["Arunachal Pradesh"]['districtData']
    assam = data["Assam"]['districtData']
    bihar = data["Bihar"]['districtData']

    chandigarh = data["Chandigarh"]['districtData']
    garh_36 = data["Chhattisgarh"]['districtData']
    delhi = data["Delhi"]['districtData']
    dadra_haveli = data["Dadra and Nagar Haveli and Daman and Diu"]['districtData']
    goa = data["Goa"]['districtData']
    gujarat = data["Gujarat"]['districtData']

    hima_p = data["Himachal Pradesh"]['districtData']
    h_yana = data["Haryana"]['districtData']
    j_khand = data["Jharkhand"]['districtData']
    j_k = data["Jammu and Kashmir"]['districtData']
    karnataka = data["Karnataka"]['districtData']
    kerala = data["Kerala"]['districtData']

    ladakh = data["Ladakh"]['districtData']
    lakshadweep = data["Lakshadweep"]['districtData']
    meghalaya = data["Meghalaya"]['districtData']
    manipur = data["Manipur"]['districtData']
    m_p = data["Madhya Pradesh"]['districtData']
    mizoram = data["Mizoram"]['districtData']

    n_land = data["Nagaland"]['districtData']
    odisha = data["Odisha"]['districtData']
    puducherry = data["Puducherry"]['districtData']
    sikkim = data["Sikkim"]['districtData']
    telangana = data["Telangana"]['districtData']
    t_n = data["Tamil Nadu"]['districtData']

    u_p = data["Uttar Pradesh"]['districtData']
    u_k = data["Uttarakhand"]['districtData']
    west_b = data["West Bengal"]['districtData']

    #print(west_b)

    #news-api to fetch news from top sources
    newsapi = NewsApiClient(api_key ='c7eb470395e04da68d1a0002d3f4ca8c')
    #news-api to fetch news from top sources

    health_headlines = newsapi.get_top_headlines(country='in', category='health')
    l = health_headlines['articles']
    url =[]
    pub =[]
    desc =[]
    news =[]
    img =[]
    
    for i in range(len(l)):
        f = l[i]
        url.append(f['url'])
        pub.append(f['publishedAt'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    india_health_list = zip(url, pub, news, desc, img)
    

    context = {
        #'data': data,
        'india_confirmed': india_confirmed,
        'india_active': india_active,
        'india_deaths': india_deaths,
        'india_recovered': india_recovered,

        'maharashtra':maharashtra,
        'andaman_n': andaman_n,
        'andhra_p': andhra_p,
        'arunachal_p': arunachal_p,
        'assam': assam,
        'bihar': bihar,

        'chandigarh': chandigarh,
        'garh_36': garh_36,
        'delhi': delhi,
        'dadra_haveli': dadra_haveli,
        'goa': goa,
        'gujarat': gujarat,

        'hima_p': hima_p,
        'h_yana': h_yana,
        'j_khand': j_khand,
        'j_k': j_k,
        'karnataka': karnataka,
        'kerala': kerala,

        'ladakh': ladakh,
        'lakshadweep': lakshadweep,
        'meghalaya': meghalaya,
        'manipur': manipur,
        'm_p': m_p,
        'mizoram': mizoram,

        'n_land': n_land,
        'odisha': odisha,
        'puducherry': puducherry,
        'sikkim': sikkim,
        'telangana': telangana,
        't_n': t_n,

        'u_p': u_p,
        'u_k': u_k,
        'west_b': west_b,


        'india_health_list': india_health_list
    }

    return render(request, 'stats/home.html', context)