'''
CountryLeaders={'PL':'Duda','US':'Trump'}
#print(CountryLeaders['US'])
#print(CountryLeaders)
CountryLeaders['DE'] = 'Merkel'

#print(CountryLeaders.keys())
#print(CountryLeaders.values())
#print(CountryLeaders.items())
#print(CountryLeaders.popitem())

#print(CountryLeaders.setdefault('FR','Macron'))

print(CountryLeaders)

NewLeaders = {'RU':'Putin','DE':'Shultz'}

CountryLeaders.update(NewLeaders)
print(CountryLeaders)
'''

chanels = {'Google':1480, 'Email':300,'Natural Traffic':440,'TV Spot':700}
print(chanels['Email'])
chanelsUpdate = {'Natural Traffic':520,'News':600}
print(chanels)
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
chanels.pop('Email')
print(chanels)
