from floodsystem import geo, stationdata

stations = stationdata.build_station_list()

river_stations = geo.stations_by_river(stations)

stations = stationdata.build_station_list()

print(geo.rivers_by_station_number(stations, 9))

