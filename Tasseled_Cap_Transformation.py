#-------------------------------------------------------------------------------
# Name: Term Project
# Author: Christopher Lee
# Student Number: 7292360
# Institution: University of Ottawa
# Description: This program allows the user to input landsat 7 or landsat 8
#               bands, and the program outputs the brightness, wetness, and
#               greenness Tasseled Cap Transformation images.
#-------------------------------------------------------------------------------

# EXAMPLE TEST FILES
# (Note these locations may change depending on where you save the data)
# E:/Term Project/Input Files/LC80160282017001LGN00_MTL.txt
# E:/Term Project/Input Files/LC80160282017001LGN00_B2.TIF
# E:/Term Project/Input Files/LC80160282017001LGN00_B3.TIF
# E:/Term Project/Input Files/LC80160282017001LGN00_B4.TIF
# E:/Term Project/Input Files/LC80160282017001LGN00_B5.TIF
# E:/Term Project/Input Files/LC80160282017001LGN00_B6.TIF
# E:/Term Project/Input Files/LC80160282017001LGN00_B7.TIF


# IMPORT STATEMENTS
import os
import sys
import time

# Point to specific file paths used for the GDAL installation in the lab
os.environ['PATH'] = "C:/OSGeo4W64/bin" + ';' + os.environ['PATH']
sys.path.append('C:/OSGeo4W64/apps/Python27/Lib/site-packages/')

# More import statements
from osgeo import gdal
import numpy as np

# Log the start time of the program
start_time = time.clock()


# FUNCTIONS
# Function to bring Landsat 7 bands into the program
def Landsat7_bands():
    # Prompt for band 1
    # If the location cannot be opened, it prompts the user to enter a location for band 1 again
    n = 0
    while n == 0:
        band1 = raw_input("Please enter the location for the Landsat 7 band 1 image:")
        ds_b1 = gdal.Open(band1)
        if ds_b1 is None:
            print ("Error unable to find file located at: " + band1)
            n = 0
        else:
            n = 1

    # Prompt for band 2
    # If the location cannot be opened, it prompts the user to enter a location for band 2 again
    o = 0
    while o == 0:
        band2 = raw_input("Please enter the location for the Landsat 7 band 2 image:")
        ds_b2 = gdal.Open(band2)
        if ds_b2 is None:
            print ("Error unable to find file located at: " + band2)
            o = 0
        else:
            o = 1

    # Prompt for band 3
    # If the location cannot be opened, it prompts the user to enter a location for band 3 again
    p = 0
    while p == 0:
        band3 = raw_input("Please enter the location for the Landsat 7 band 3 image:")
        ds_b3 = gdal.Open(band3)
        if ds_b3 is None:
            print ("Error unable to find file located at: " + band3)
            p = 0
        else:
            p = 1

    # Prompt for band 4
    # If the location cannot be opened, it prompts the user to enter a location for band 4 again
    q = 0
    while q == 0:
        band4 = raw_input("Please enter the location for the Landsat 7 band 4 image:")
        ds_b4 = gdal.Open(band4)
        if ds_b4 is None:
            print ("Error unable to find file located at: " + band4)
            q = 0
        else:
          q = 1

    # Prompt for band 5
    # If the location cannot be opened, it prompts the user to enter a location for band 5 again
    r = 0
    while r == 0:
        band5 = raw_input("Please enter the location for the Landsat 7 band 5 image:")
        ds_b5 = gdal.Open(band5)
        if ds_b5 is None:
            print ("Error unable to find file located at: " + band5)
            r = 0
        else:
            r = 1

    # Prompt for band 7
    # If the location cannot be opened, it prompts the user to enter a location for band 7 again
    s = 0
    while s == 0:
        band7 = raw_input("Please enter the location for the Landsat 7 band 7 image:")
        ds_b7 = gdal.Open(band7)
        if ds_b7 is None:
            print ("Error unable to find file located at: " + band7)
            s = 0
        else:
            s = 1

    # Create the array with all the bands
    bands = [ds_b1.GetRasterBand(1),ds_b2.GetRasterBand(1),ds_b3.GetRasterBand(1),ds_b4.GetRasterBand(1),ds_b5.GetRasterBand(1),ds_b7.GetRasterBand(1)]

    # Find raster dimensions, projection and geotransform
    xsize = ds_b2.RasterXSize
    ysize = ds_b2.RasterYSize
    projection = ds_b2.GetProjection()
    geotransform = ds_b2.GetGeoTransform()

    # Create an empty list called "arrays", then loop through the bands and put then in this list
    arrays = []
    for i in range(6):
        arrays.append(bands[i].ReadAsArray(0,0,xsize,ysize))

    # return the array with the bands, the raster dimension, projection, and geotransform back to the main program
    return arrays, xsize, ysize, projection, geotransform

# Function to bring Landsat 8 bands into the program
def Landsat8_bands():
    # Prompt for band 2
    # If the location cannot be opened, it prompts the user to enter a location for band 2 again
    h = 0
    while h == 0:
        band2 = raw_input("Please enter the location for the Landsat 8 band 2 image:")
        ds_b2 = gdal.Open(band2)
        if ds_b2 is None:
            print ("Error unable to find file located at: " + band2)
            h = 0
        else:
            h = 1

    # Prompt for band 3
    # If the location cannot be opened, it prompts the user to enter a location for band 3 again
    i = 0
    while i == 0:
        band3 = raw_input("Please enter the location for the Landsat 8 band 3 image:")
        ds_b3 = gdal.Open(band3)
        if ds_b3 is None:
            print ("Error unable to find file located at: " + band3)
            i = 0
        else:
            i = 1

    # Prompt for band 4
    # If the location cannot be opened, it prompts the user to enter a location for band 4 again
    j = 0
    while j == 0:
        band4 = raw_input("Please enter the location for the Landsat 8 band 4 image:")
        ds_b4 = gdal.Open(band4)
        if ds_b4 is None:
            print ("Error unable to find file located at: " + band4)
            j = 0
        else:
            j = 1

    # Prompt for band 5
    # If the location cannot be opened, it prompts the user to enter a location for band 5 again
    k = 0
    while k == 0:
        band5 = raw_input("Please enter the location for the Landsat 8 band 5 image:")
        ds_b5 = gdal.Open(band5)
        if ds_b5 is None:
            print ("Error unable to find file located at: " + band5)
            k = 0
        else:
            k = 1

    # Prompt for band 6
    # If the location cannot be opened, it prompts the user to enter a location for band 6 again
    l = 0
    while l == 0:
        band6 = raw_input("Please enter the location for the Landsat 8 band 6 image:")
        ds_b6 = gdal.Open(band6)
        if ds_b6 is None:
            print ("Error unable to find file located at: " + band6)
            l = 0
        else:
            l = 1

    # Prompt for band 7
    # If the location cannot be opened, it prompts the user to enter a location for band 7 again
    m = 0
    while m == 0:
        band7 = raw_input("Please enter the location for the Landsat 8 band 7 image:")
        ds_b7 = gdal.Open(band7)
        if ds_b7 is None:
            print ("Error unable to find file located at: " + band7)
            m = 0
        else:
            m = 1

    # Create the array with all the bands
    bands = [ds_b2.GetRasterBand(1),ds_b3.GetRasterBand(1),ds_b4.GetRasterBand(1),ds_b5.GetRasterBand(1),ds_b6.GetRasterBand(1),ds_b7.GetRasterBand(1)]

    # Find raster dimensions, projection and geotransform
    xsize = ds_b2.RasterXSize
    ysize = ds_b2.RasterYSize
    projection = ds_b2.GetProjection()
    geotransform = ds_b2.GetGeoTransform()

    # Create an empty list called "arrays", then loop through the bands and put then in this list
    arrays = []
    for i in range(6):
        arrays.append(bands[i].ReadAsArray(0,0,xsize,ysize))

    # return the array with the bands, the raster dimension, projection, and geotransform back to the main program
    return arrays, xsize, ysize, projection, geotransform

# Function to computed the Tasseled Cap Transformation for Landsat 7 bands
def TCT_Landsat7(bands):
    # Multiples the bands with their proper landsat type coefficients and sum it up to create each Tasseled Cap Transformation
    brightness = (0.3561 * bands[0].astype(float)) + (0.3972 * bands[1]) + (0.3904 * bands[2]) + (0.6966 * bands[3]) + (0.2286 * bands[4]) + (0.1596 * bands[4])
    greenness = (-0.3344 * bands[0].astype(float)) + (-0.3544 * bands[1]) + (-0.4556 * bands[2]) + (0.6966 * bands[3]) + (-0.0242 * bands[4]) + (-0.263 * bands[4])
    wetness = (0.2626 * bands[0].astype(float)) + (0.2141 * bands[1]) + (0.0926 * bands[2]) + (0.0656 * bands[3]) + (-0.7629 * bands[4]) + (-0.5388 * bands[4])

    # Returns the 3 Tasseled Cap Transformations back to the main program
    return brightness, greenness, wetness

# Function to computed the Tasseled Cap Transformation for Landsat 8 bands
def TCT_Landsat8(bands):
    # Multiples the bands with their proper landsat type coefficients and sum it up to create each Tasseled Cap Transformation
    brightness = (0.3029 * bands[0].astype(float)) + (0.2786 * bands[1]) + (0.4733 * bands[2]) + (0.5599 * bands[3]) + (0.508 * bands[4]) + (0.1872 * bands[5])
    greenness = (-0.2941 * bands[0].astype(float)) + (-0.243 * bands[1]) + (-0.5424 * bands[2]) + (0.7276 * bands[3]) + (0.0713 * bands[4]) + (-0.1608 * bands[5])
    wetness = (0.1511 * bands[0].astype(float)) + (0.1973 * bands[1]) + (0.3283 * bands[2]) + (0.3407 * bands[3]) + (-0.7117 * bands[4]) + (-0.4559 * bands[5])

    # Returns the 3 Tasseled Cap Transformations back to the main program
    return brightness, greenness, wetness

# Function to save the previously computed Tasseled Cap Transformations
def Outputs(brightness, greenness, wetness, start_time):
    # Create brightness picture, with the same raster dimensions, projection, and geotransform as the source images
    brightness_pic = "C:/brightness_" + sens_type + ".tif"
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(brightness_pic,xdim,ydim,1,gdal.GDT_Float32)
    dataset.SetGeoTransform(geotransform)
    dataset.SetProjection(projection)
    band = dataset.GetRasterBand(1)
    band.WriteArray(brightness)
    dataset = None

    # Create greenness picture, with the same raster dimensions, projection, and geotransform as the source images
    greenness_pic = "C:/greenness_" + sens_type + ".tif"
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(greenness_pic,xdim,ydim,1,gdal.GDT_Float32)
    dataset.SetGeoTransform(geotransform)
    dataset.SetProjection(projection)
    band = dataset.GetRasterBand(1)
    band.WriteArray(greenness)
    dataset = None

    # Create wetness picture, with the same raster dimensions, projection, and geotransform as the source images
    wetness_pic = "C:/wetness_" + sens_type + ".tif"
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(wetness_pic,xdim,ydim,1,gdal.GDT_Float32)
    dataset.SetGeoTransform(geotransform)
    dataset.SetProjection(projection)
    band = dataset.GetRasterBand(1)
    band.WriteArray(wetness)
    dataset = None

    # Prints the time it takes to complete the Tasseled Cap Transformation task, and the location of each of the images
    print("Task completed successfully in: " + str(round(time.clock() - start_time,1)) + " seconds")
    print("The brightness tasseled cap transformation for " + sens_type + " is saved at location: " + brightness_pic)
    print("The greenness tasseled cap transformation for " + sens_type + " is saved at location: " + greenness_pic)
    print("The wetness tasseled cap transformation for " + sens_type + " is saved at location: " + wetness_pic)


# MAIN PROGRAM

# Counter to run a loop
a = 0

# Run the loop until the user enters the landsat type of their image or a text file that contains the landsat type
while a == 0:
    # Prompts the user to enter a number
    sensor = int(raw_input("Please enter 1 if your images are captured using Landsat 7" + "\n" + "Please enter 2 if your images are captured using Landsat 8" + "\n" + "Please enter 3 to enter the .txt file to find which Landsat sensor"))

    # If the user selects 1, it corresponds to Landsat 7 and proceeds to the function that prompts the user to enter the bands
    # it then takes these bands to do the Tasseled Cap Transformation in a different function
    # it then saves the Tasseled Cap Transformation in a different function
    if sensor == 1:
        sens_type = "landsat_7"
        bands, xdim, ydim, projection, geotransform = Landsat7_bands()
        brightness, greenness, wetness = TCT_Landsat7(bands)
        Outputs(brightness, greenness, wetness, start_time)
        a = 1

    # If the user selects 2, it corresponds to Landsat 8 and proceeds to the function that prompts the user to enter the bands
    # it then takes these bands to do the Tasseled Cap Transformation in a different function
    # it then saves the Tasseled Cap Transformation in a different function
    elif sensor == 2:
        sens_type = "landsat_8"
        bands, xdim, ydim, projection, geotransform = Landsat8_bands()
        brightness, greenness, wetness = TCT_Landsat8(bands)
        Outputs(brightness, greenness, wetness, start_time)
        a = 1

    # If the user selects 3, it prompts the user to enter the text file in which the landsat type might be located in
    # it then proceeds to read the file line by line to find the line that starts with "SPACECRAFT_ID"
    # it then extracts the value to the right of this to see what landsat type it is
    # it then prints the landsat type to the screen
    elif sensor == 3:
        filename = raw_input("Please enter the location of your .txt file: ")
        f = open(filename,"r")
        for line in f:
            splitLine = line.split()
            firstString = splitLine[0]
            if(firstString == "SPACECRAFT_ID"):
                landsat_type = splitLine[2]
                l_sens = str(landsat_type[1:-1])
                print("Landsat type is: " + l_sens)

        # If the landsat type is "LANDSAT_7" it proceeds to the function that prompts the user to enter the bands
        # it then takes these bands to do the Tasseled Cap Transformation in a different function
        # it then saves the Tasseled Cap Transformation in a different function
        if l_sens == "LANDSAT_7":
            sens_type = "landsat_7"
            bands, xdim, ydim, projection, geotransform = Landsat7_bands()
            brightness, greenness, wetness = TCT_Landsat7(bands)
            Outputs(brightness, greenness, wetness, start_time)
            a = 1

        # If the landsat type is "LANDSAT_8" it proceeds to the function that prompts the user to enter the bands
        # it then takes these bands to do the Tasseled Cap Transformation in a different function
        # it then saves the Tasseled Cap Transformation in a different function
        elif l_sens == "LANDSAT_8":
            sens_type = "landsat_8"
            bands, xdim, ydim, projection, geotransform = Landsat8_bands()
            brightness, greenness, wetness = TCT_Landsat8(bands)
            Outputs(brightness, greenness, wetness, start_time)
            a = 1

        # If there is no sensor type detected in the text file it restarts the loop
        else:
            print("No Landsat sensor type detected")
            a = 0

    # If the value enter is not one of the options presented it restarts the loop
    else:
        a = 0