#DATA ACCESS
We know there is a trade-off between the accuracy of results and run-time. So in order to make a fair balance between these two, we will use one of the sub-boxes of Illustris-3. Since the file sizes are smaller to download and easier to work with. And then we will use the 20 GB data we downloaded for further computations.
In this specific test case, 48th snapshot at redshift 5.23 Groupcat is downloaded from here. The more general simulation details are available on the website. Every snapshot ( ~20 GB) has an equivalent Groupcat (~100 MB). It seems like in Groupcats, some information is excluded, and they also have lower resolution.
The file’s format is hdf5 which is typically used in astronomy research applications to distribute and access very large datasets without using a database.
If one would like to have a quick glimpse of data, anytime they want, Here they can download HDF reader.
Thus we used HDF file reader to access data very quickly. The following features are available in Groupcats (Therefore in main datasets):



#SOME SIMPLE CALCULATIONS ON DATA

