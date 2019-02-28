# Introduction

One of the most fundamental questions in the studying the Large Scale
Structure of the Universe is the effect of environment on the Galaxy
formation and evolution. In addition to the spatial properties of
galaxies, some of their characteristics such as star formation rate,
metalicity, shape, and spin might depend on the environmental
conditions, which is the dark matter distribution in this context.

## Why Machine Learning?

Due to complicated physics involved in the galaxy formation,
cosmologists usually run simulations to study these processes, which is
time consuming and computationally expensive. In the past few years
machine learning algorithms emerge as a useful assistant for theoretical
and observational cosmologists.

In this project we propose to use deep learning method to establish a
mapping between Galaxies in Hydrodynamic/N-body simulations and its
underlying dark matter distribution, which may cancel the need for
running costly simulations each time after changing the cosmological
model.

# Methods

The first aim of our project is to re-derive the results of a very
recently published paper by Zhang et al. . We divided this project into
sections which are explained below:

  - acquiring Data for sub-boxes of Illustris simulation with
    high/mediate resolutions to study the performance of our algorithm
    in different resolutions.

  - Sampling for training set and testing set

  - Learning the algorithm in the sub-boxes with two resolutions

  - Test the algorithm in other sub-boxes of the simulation

  - Train and test the algorithm for a larger high resolution box

## Data

We will use the data from [IllustrisTNG](http://www.tng-project.org/)
simulation, which is the next generation of
[Illustris](http://www.illustris-project.org/) with more precise
astrophysical models/processes. The IllustrisTNG project is an ongoing
series of large, cosmological magnetohydrodynamical simulations of
galaxy formation, based on \(\Lambda CDM\) cosmology, that uses Planck
2015 results  as model parameters. These simulations include both dark
matter-only and radiative runs which makes them a suitable source for
our project. Indeed, due to computational limitations, our main focus
will be on low resolution runs of IllustrisTNG (\(L_{box} \approx 51.7\)
Mpc) that includes \(2 \times 2160^3\) elements .

## Algorithm

We will use Convolutional Neural Networks (CNN), which are useful when
dealing with high volume data (such as image processing, etc). In order
to prevent over-fitting, several convolution and pooling operations
should be done to reduce number of parameters and make feature maps with
extracting global features of the data.

Several architectures for CNN exist: LeNet, U-Net, ResNet, Inception,
etc. The original paper adopted U-net. However we will decide which
architecture we would use after downloading and analyzing a portion of
the original data. We will use Keras for implementing our CNN.

# Goal and Objectives

The main goal of this project is to find out the relation between dark
matter field and galaxy positions. Besides, we are wishful to answer the
following questions: If this relation exists, what are the parameters?
Can we predict galaxy mass distribution, and more ambitiously, color,
metalicity, star formation rate, etc. from a given dark matter field?
And if there is no such a relation, then what are the other features
that can be used in order to predict statistical properties of galaxies?