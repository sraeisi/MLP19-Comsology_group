#DATA ACCESS

We know there is a trade-off between the accuracy of results and run-time. So in order to make a fair balance between these two, we will use one of the sub-boxes of Illustris-3. Since the file sizes are smaller to download and easier to work with. And then we will use the 20 GB data we downloaded for further computations.
In this specific test case, 48th snapshot at redshift 5.23 Groupcat is downloaded from here. The more general simulation details are available on the website. Every snapshot ( ~20 GB) has an equivalent Groupcat (~100 MB). It seems like in Groupcats, some information is excluded, and they also have lower resolution.
The file’s format is hdf5 which is typically used in astronomy research applications to distribute and access very large datasets without using a database.
If one would like to have a quick glimpse of data, anytime they want, Here they can download HDF reader.
Thus we used HDF file reader to access data very quickly. The following features are available in Groupcats (Therefore in main datasets):

![alt text](https://github.com/sraeisi/MLP19-Comsology_group/blob/SetarehForoozan-patch-2/Screen%20Shot%202019-03-16%20at%2012.12.12%20AM.png)

#SOME SIMPLE CALCULATIONS ON DATA

![alt text](https://github.com/sraeisi/MLP19-Comsology_group/blob/SetarehForoozan-patch-2/Halo_distribution_in_space.png)

![alt text](https://github.com/sraeisi/MLP19-Comsology_group/blob/SetarehForoozan-patch-2/Histogram_In_XY_Plane.png)

![alt text](https://github.com/sraeisi/MLP19-Comsology_group/blob/SetarehForoozan-patch-2/Star%20Formation%20Rate%20vs%20Halo%20Mass.png)

![alt text](https://github.com/sraeisi/MLP19-Comsology_group/blob/SetarehForoozan-patch-2/Velocity_Histogram.png)

I use illustris-3 (hydro dynamic simulation) and illustris-3-dark( N-body dark matter simulation). I take the position of dark matter particles(from illusris3_dark) and galaxies(from illustris 3). The data has 94,196,375 dark matter particles and 121,208 galaxies. I plot 2d histogram of them and 3d plot of galaxies in box(75 X 75 Mpc). 

![alt text](https://raw.githubusercontent.com/zahrabaghkhani/cosmology/new/data/1.jpg?token=AtrysU7eE74UZQC5EgQaC6BbtA2mjbRYks5cjC9TwA%3D%3D)
![alt text](https://raw.githubusercontent.com/zahrabaghkhani/cosmology/new/data/2.jpg?token=Atrysda6jlowdVkn9iFACB6UI4IKbeKoks5cjC-JwA%3D%3D)
![alt text](https://raw.githubusercontent.com/zahrabaghkhani/cosmology/new/data/3.jpg?token=AtrysfvczsvVMStgTBn7gIedHlHcx2NEks5cjC-xwA%3D%3D)
