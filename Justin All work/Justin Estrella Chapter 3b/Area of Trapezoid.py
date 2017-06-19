#Calculate the area of a trapezoid 
print ("This program calculates the area of a trapezoid")
height_of_trapezoid = input ("Enter height of trapezoid:")
height_of_trapezoid = float (height_of_trapezoid)
#Enter Length
length_of_bottom_base = input ("Enter length of bottom base:")
length_of_bottom_base = float (length_of_bottom_base)
#Enter length of top base
length_of_top_base = input ("Enter length of top base:")
length_of_top_base = float (length_of_top_base)
area = (length_of_bottom_base + length_of_top_base) * height_of_trapezoid / 2
print ("Area of trapezoid", area)