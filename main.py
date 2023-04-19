import numpy
from sys import argv
from math import pow, pi
from matplotlib import pyplot as plot

G = 6.67 * 10 ** -11
M = 10**30
m = 5.97219 * 10 ** 24
seconds_in_a_year = 60*60*24*365
AU = 149597870700

def read_csv(csv_file):
    with open(csv_file, 'r') as file:
        data = file.readlines()
    data = [item[:-1].split(',') for item in data]
    return data

def local_maxima_indexs(data):
    indexs = []
    for index in range(1, len(data)):
        if data[index] > data[index-1] and data[index] > data[index+1]:
            indexs.append(index)
    return indexs

if __name__ == "__main__":
    min_peak = 50
    csv_file = argv[1]
    if len(argv) == 3:
        min_peak = int(argv[2])
    astrometry_data = read_csv(csv_file)
    time, radial_velocity = [int(item[0]) for item in astrometry_data[1:]], [float(item[1]) for item in astrometry_data[1:]]
    time_resolution = time[1] - time[0]
    plot.title("Radial Velocity vs Time (Imported from CSV File)")
    plot.xlabel("Time (in s)")
    plot.ylabel("Radial Velocity (in m/s)")
    plot.plot(time, radial_velocity, 'r-')
    plot.show()

    ft_radial_velocity = numpy.fft.rfft(radial_velocity)
    ft_radial_velocity = [abs(item) for item in ft_radial_velocity]
    ft_radial_velocity[0] = 0
    for index, item in enumerate(ft_radial_velocity):
        if item < min_peak:                  # Filtering Peaks
            ft_radial_velocity[index] = 0
    ft_radial_velocity_frequency = numpy.fft.rfftfreq(len(radial_velocity))
    plot.title("Fourier Transformation of Radial Velocity")
    plot.xlabel("Frequency")
    plot.ylabel("Power")
    plot.plot(ft_radial_velocity_frequency, ft_radial_velocity, 'r-')
    plot.show()

    rft_radial_velocity = numpy.fft.irfft(ft_radial_velocity)
    plot.title("Reverse Fourier Transformation of Radial Velocity")
    plot.xlabel("Time (in s)")
    plot.ylabel("Radial Velocity (in m/s)")
    plot.plot(time, rft_radial_velocity, 'r-')
    plot.show()

    plot.title("Individual Effects on Velocity of Star by Planets")
    plot.xlabel("Time (in s)")
    plot.ylabel("Velocity")
    max_radial_velocity_of_star_due_to_planets_individually = []
    frequency_indexes = local_maxima_indexs(ft_radial_velocity)
    for frequency in frequency_indexes:
        current_graph = ft_radial_velocity.copy()
        for index, value in enumerate(current_graph):
            if value != ft_radial_velocity[frequency]:
                current_graph[index] = 0
        current_graph = numpy.fft.irfft(current_graph)
        max_radial_velocity_of_star_due_to_planets_individually.append(max(current_graph))
        plot.plot(time, current_graph)
    plot.show()

    frequency_of_revolution = [ft_radial_velocity_frequency[index] for index in frequency_indexes]
    time_period_of_revolution = [1/frequency*10**5/seconds_in_a_year for frequency in frequency_of_revolution]
    avg_radius_of_orbit = [pow(G*M*pow(time_period*seconds_in_a_year, 2)/(4*pow(pi, 2)), 1/3) for time_period in time_period_of_revolution]
    tangential_velocity_of_planets, mass_of_planets = [], []
    for radius, time_period, star_velocity in zip(avg_radius_of_orbit, time_period_of_revolution, max_radial_velocity_of_star_due_to_planets_individually):
        tangential_velocity_of_planets.append(2*pi*radius/(time_period*seconds_in_a_year))
        mass_of_planets.append(M*star_velocity/tangential_velocity_of_planets[-1])

    print(f"Total Number of Planets = {len(frequency_indexes)}\n")
    for index in range(len(frequency_indexes)):
        print(f"Planet Number = {index+1}")
        print(f"Mass of the Planet = {mass_of_planets[index]:.2f} kg ({mass_of_planets[index]/m:.2f} Earth Mass)")
        print(f"Average Radius of Revolution = {avg_radius_of_orbit[index]/1000:.2f} km ({avg_radius_of_orbit[index]/AU:.2f} AU)")
        print(f"Time Period of Revolution    = {time_period_of_revolution[index]:.2f} years")
        print()