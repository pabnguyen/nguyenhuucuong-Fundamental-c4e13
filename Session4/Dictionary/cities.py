from haversine import haversine

cities = [
    {
        'name' : 'Hải Phòng',
        'lat' : 20.844,
        'lng' : 106.688,
    },
    {
        'name' : 'Hà Nội',
        'lat' :  21.0513,
        'lng' :  105.825,
    },
    {
        'name' : 'Đà Nẵng',
        'lat' :  15.88,
        'lng' : 108.629,
    },
    {
        'name' : 'Huế',
        'lat' :  16.44,
        'lng' : 107.56,
    }

]

n = len(cities)
for i in range (0, n-1):
    for j in range(i+1,n):
        city1 = cities[i]
        city2 = cities[j]


        #haversine
        cord1 = [city1['lat'],city1['lng']]
        cord2 = [city2['lat'],city2['lng']]

        distance = haversine(cord1, cord2)

        print("Khoảng cách từ {0} đến {1} là {2}".format(city1['name'],city2['name'],distance))
