world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

country = 'Италия'
world_champions.update({2022:'Аргентина'})

if country in world_champions.values():
    for year, champion in world_champions.items():
        print(f'{year} - {champion}')
        if champion == country and 2001 <= year <= 2100:
            print('Италия cтановилась чемпионом мира по футболу в 21 веке!')    
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')