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

the goal of this project is to find a mapping between N_body simulation and baryonic matter distribution in the hydrodynamic simulation. so we need dark matter distribution in n_body simulation and galaxy distribution in hydrodynamic simulation. 
we  download some features for the whole simulation box(75 X 75 X 75 MPC). we used illustris-3 (hydro dynamic simulation) and illustris-3-dark( N-body dark matter simulation).in this case, 135th snapshot at redshift 0 is downloaded. data includes only dark matter particles position(from illustris-3 dark) and galaxy position(from illustris-3).The data has 94,196,375 dark matter particles and 121,208 galaxies.

![alt text](https://raw.githubusercontent.com/sraeisi/MLP19-Comsology_group/zahrabaghkhani-patch-1/Data/1.jpg)
![alt text](https://raw.githubusercontent.com/sraeisi/MLP19-Comsology_group/zahrabaghkhani-patch-1/Data/2.jpg)
![alt text](https://raw.githubusercontent.com/sraeisi/MLP19-Comsology_group/zahrabaghkhani-patch-1/Data/3dgalaxy.jpg)
