import sys
import os
from os import path
import numpy as np
from matplotlib.image import imread
from PIL import Image, ImageOps
import shutil
import ntpath
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Toggle Values
tidaltog = 0
aquatog = 0
desertog = 0
soilalbtog = 0
soildepthtog = 0
capsoiltog = 0
soilwcptog = 0
soilsattog = 0
snowalbtog = 0
mxsnowtog = 0
mldepthtog = 0
oceanalbtog = 0
imgsratogtog = 0
pressuretog = 0
gascontog = 0
ptog = 0
gtog = 0
stmtog = 0
baltog = 0

#Help Prompts
####Model Parameters
def helpjctnme(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Project Name
The name of your project, this is not the same as the name for the output file/folder""")
def helpstrtyr(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Start Year
1 by default; What number year the project should start at (eg. '2000' will have the model start at 2000).
This is arbitrary, however must be positive.""")
def helpotptype(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Output Type
.nc by default; File extension to use for the output, if using the pyburn postprocessor.
If using any of .hdf5, .he5, or .h5, then h5py must be installed.""")
def helpcpucnt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: CPU Count
4 by default; Number of CPUs for ExoPlaSim to use.""")
def helpresision(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Precision
8 by default; Precision (in bytes) of some internal numbers used, either 4 or 8.
4 will run a tad faster, but may be less stable and more prone to crashing.""")
def helpresolution(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Resolution
T21 by default; Sets the resolution used for modelling the planet’s surface,
thus the resolution of the geography one can import into the model and the output one will get.
These are the resolutions ExoPlaSim can handle, and the associated codes to input here:

Code|Height|Width
 T21|  32  |  64
 T42|  64  | 128
 T63|  96  | 192
 T85| 128  | 256
T106| 160  | 320
T127| 192  | 384
T170| 256  | 512""")
def helpcrshtlrnt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Crash Tolorant
False by default; If set to True, then if the model crashes (and at least 10 years have been simulated),it will rewind 10 years and try again.
This can help get around some crashes caused by essentially just random noise in the model, without requiring manually restarting it each time.

On the other hand, if there’s some more fundamental issue with the model
(e.g., it’s warming to the point that the oceans start boiling away) then this feature could cause it to be trapped in an infinite loop; 
So it’s probably best to leave it off if you’re “exploring” new configurations, and to check up on the model when you do turn it on.""")
def helplayers(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Layers
10 by default; Number of atmospheric layers modeled—in essence, the vertical resolution of the model grid.
Low-resolution models seem to work fine with 5, which saves a good deal of computing time.
Higher-resolution models may require more layers for best accuracy, but would further extend the runtime.""")
def helprecompile(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Recompile
False by default; If set to True, forces exoplasim to compile again before running.
May be useful if you’ve altered some of the source files.""")

####Stellar Parameters
def helpstrtmp(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Star Temperature
5772.0 by default; The effective temperature of the star in Kelvin, will be used to adjust atmospheric absorption and surface albedo.
It does not affect flux or year length, and if not set, a sunlike star will be assumed.""")
def helpstlrflx(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Stellar Flux
1367.0 by default; The flux of sunlight hitting the top of the planet’s atmosphere, in watts/meter^2.
Value represents Earth's Stellar Flux.""")

####Orbital Parameters
def helpyrlngth(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Year Length
365.25 by default; Length of the year, in 24-hour Earth days.
This controls the period the planet takes to orbit its star, not the length of the years used for the output files and the model run controls;
Those are set by the runsteps parameter, though generally speaking they should probably be the same, except for very short orbital periods.

To properly produce Koppen maps from the output files, this should be the same length of time as the model year.
year * 1440 = runsteps * timestep""")
def helpdaylngth(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Day Length
1.0 by default; Rotation period of the planet, compared to Earth.
This is a sidereal day (23 hours 56 minutes for Earth).
For planets with many orbits per year it should be an insignificant difference from a solar day.

Ideally there should be a whole number of timesteps in a solar day, and a whole number of solar days in a month.
(rotationperiod * 1440) / timestep = an integer
runsteps / times = (rotationperiod * 1440 / timestep) * an integer""")
def helpeccentr(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Eccentricity
0.016715 by default; Eccentricity of the planet’s orbit.""")
def helpoblqty(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Obliquity
23.441 by default; Obliquity, A.K.A. axial tilt, in degrees.""")
def helplngpri(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Longitude of Periapsis
102.7 by default; Longitude (angle along the orbit) of periapsis (point when the planet is closest to the star) in degrees.
Measured from the autumnal equinox, which is used to orient the planet’s rotational axis relative to its orbit.""")
def helpfxdobt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Fixed Orbit
True by default; True forces the orbit to remain unchanged throughout the simulation.
False allows for ExoPlaSim to calculate Milankovitch cycles to alter the planet’s orbit and orientation.

The latter feature is still under development, so it’s probably best to keep this on for now.""")

####Rotational Parameters
def helptdlkd(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Tidally Locked
False by Default; True locks the sun to one longitude.""")
def helpsbstlrlng(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Substellar Longitude
180 by Default; Longitude of the substellar point, in degrees.
If importing geography with 0 longitude at the center, the geography will be offset 180 degrees from the model’s coordinate system.
The default of 180 would places the substellar point at 0 longitude.""")
def helpsbstlrdsync(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Substellar Desync
0.0 by Default; Rate at which the substellar point drifts from its initial longitude, in degrees per minute.
One could use this to approximate spin-orbit resonances other than 1:1
(eg. drift of 180 degrees per orbit would approximate the 3:2 resonance)

But the effects of eccentricity on the movement of the substellar point are not properly modelled in the current version of ExoPlaSim.
Can be positive or negative.""")
def helptmpcntrst(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Temperature Contrast
0.0 by Default; Adds an initial temperature contrast between the substellar point and the antistellar point, in Kelvin.
Increasing it to, 100 may help the model balance faster.""")

####Planet Parameters
def helpgrvty(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Gravity
9.80665 by Default; Acceleration due to gravity at the planet’s surface, in meters/second^2.""")
def helprdus(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Radius
1.0 by Default; Radius of the planet relative to Earth.""")
def helporgrphy(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Orography
1.0 by Default; Scaling factor applied to the above-defined topography, down to flat continents at 0.0.
Extreme conditions on high mountain peaks or deep valley floors can sometimes cause crashes, so flattening out the topography can help tell if that’s the issue.""")
def helpaquaplnt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Aqua Planet
False by Default; True erases land surfaces (including the default earth geography) and gives a uniform, all-ocean planet.
May run a bit faster, so it can be useful for debugging or quick tests of other factors.""")
def helpdsrtplnt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Desert Planet
False by Default; True erases all seas and gives a fully land-covered planet.""")

####Vegetation Parameters
def helpvgtn(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Vegetation
None by Default; Controls a vegetation model, which will impact surface albedo and humidity.
Not a very advanced model and probably won’t handle particularly exotic climates too well, but it’s still nice to have.

None will leave the model off
"Diagnostic" vegetation is fixed to an initial value of vegetation cover across all land
"Dynamic" will activate a vegetation model that will grow and die back in response to the local climate, producing an estimate of the resulting forest cover in the output.
This will probably slow down the model to some extent, so one might want to leave it off until putting together a final model.""")
def helpvgaclrtn(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Vegetation Acceleration
1 by Default; Accelerates the rate of vegetation growth.""")
def helpbiomsgrwth(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Biomass Growth
1.0 by Default; Amount of biomass produced by vegetation in tonnes/hectare/year.""")
def helpintlgrth(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Initial Growth
0.5 by Default; Adds vegetation cover to all land at the start of the model.
Might save some time running the model to equilibrium and make the resulting climate somewhat less arid than it would be if it started without vegetation.
Should be between 0 and 1.""")
def helpstmtlcndtnce(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Initial Stomatal Conductance
1.0 by Default; Rate at which CO2 enters or water vapour exits through the stomata of leaves at the start of the simulation.""")
def helpvgtnrghns(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Initial Vegetation Roughness
2.0 by Default; Determines how much vegetation slows down wind speeds at the start of the simulation.""")
def helpslcbncntnt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Initial Soil Carbon Content
0.0 by Default; How much carbon is stored within soil at the start of the simulation.""")
def helplntcbncntnt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Initial Plant Carbon Content
0.0 by Default; How much carbon is stored within plants at the start of the simulation.""")

####Surface Parameters
def helpwtsl(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Wet Soil
False by Default; True alters the albedo of land surfaces based on how wet they are; wetter land has a lower albedo, so it reflects less light.""")
def helpslalbdo(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Soil Albedo
Disabled by Default; Can be set to a fixed albedo value that will be used for all land.
Usually shouldn’t do this for Earthlike planets, could use it to model some sort of unusual desert planet covered in more reflective desert sand or salt.""")
def helpsldpth(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Soil Depth
Disabled by Default; Scaling factor for the depth of soil layers in meters.""")
def helpslhtcpsty(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Soil Heat Capacity
Disabled by Default; Heat capacity of the soil, in (10^6)J/m^3/K""")
def helpslwtrcpsty(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Soil Water Capacity
Disabled by Default; Water capacity of the soil, in meters.""")
def helpslstrtn(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Initial Soil Saturation
Disabled by Default; Initial fractional saturation of the soil.""")
def helpsnwalb(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Snow/Ice Albedo
Disabled by Default; Can be set to a fixed albedo value that will be used for all snow and ice.""")
def helpmxsnw(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Max Snow
Disabled by Default; Maximum snow depth in meters. Set to -1 to have no limit.""")
def helpseaice(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Sea Ice
True by Default; If False, disables radiative effects of sea ice (although sea ice itself is still computed).""")
def helpocnalb(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Ocean Albedo
Disabled by Default; Can be set to a fixed albedo value that will be used for all oceans.""")
def helpmxdlyrdpth(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Mixed Layer Depth
50.0 by Default; Depth of the mixed-layer ocean in meters.""")
def helpocnznth(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Ocean Zenith
ECHAM-3 by Default; The zenith-angle dependence to use for blue-light reflectance from the ocean.""")

####Geographic Parameters
def helpimgsratog(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Image/SRA Toggle
False by Default; Determines whether to produce SRA files through images (False) or use existing SRA files (True).""")
def helphghtmpimg(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Height Map Image
N/A by Default; Path to a (ideally) black and white .png image, with black as lowest elevation and white as highest.
Resolution of the image must be some multiple of the model resolution.""")
def helpwtrthrshld(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Water Threshold
0 by Default; Colour value at which sea level is at.
When making a height map, one may have also included ocean topography, and thus sea level may not be where black(0) is.""")
def helphghstelvtn(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Highest Elevation
8849.0 by Default; The highest point of land (in meters).""")
def helplwstelvtn(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Lowest Elevation
-11034.0 by Default; The lowest point of land (in meters), used if the planet has no oceans.""")
def helpimgdbg(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Image Debug
False by Default; If True will produce debug images showing the land mask during the process of converting images to SRA files.""")
def helpsranme(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: SRA Name
Set the name to be used for the output SRA files.""")
def helplndsra(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Land SRA
N/A by Default; Path to a .sra file containing a land/sea mask for the planet’s geography.
It’ll default to Earth’s geography (at least for T21 and T42 runs) if not set.""")
def helptposra(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Topographic SRA
N/A by Default; Path to a .sra file containing the planet’s topography.""")

####Atmospheric Parameters
def helprsure(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Pressure
1.0 by Default; Total surface pressure in bars.
Unnecessary if one has already set all the partial pressures of the component gasses in your atmosphere,
Though one can combine this with the partial pressures of some of the component gasses (in which case one should set a gas constant as well).""")
def helpgscnstnt(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Gas Constant
287.0 by Default; Effective gas constant, in Joules / (kilograms * Kelvin).
Can be calculated as the molar gas constant (8.314 J / K*mol) divided by the average molar mass of the atmosphere, in kg/mol.""")
def helpdrycre(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Dry Core
False by Default; If True, evaporation is turned off, and a dry atmosphere will be used.""")
def helpozne(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Ozone
False by Default; True adds an ozone layer, which slightly increases greenhouse heating, among other effects.
Any planet with oxygen should probably have some ozone as well.
However ExoPlaSim’s handling of ozone has been tuned to match Earth and may not be very accurate for significantly different atmospheres or stars.

Maybe still use it for Earthlike planets with significant atmospheric oxygen orbiting sunlike stars
Possibly best to exclude otherwise, even though this may cause a slight underestimate in greenhouse heating.""")
def helpgsprsurs(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Gas Pressures (AKA Partial Pressures)
False by Default; Enabling allows one to set partial pressures(bar) of various gasses:
H2 - Hydrogen
He - Helium
N2 - Nitrogen
O2 - Oxygen
Ar - Argon
Ne - Neon
Kr - Krypton
H20 - Water Vapour
CO2 - Carbon Dioxide

NOTE: Other than ozone, CO2 is the only greenhouse gas one can directly set.
H20 only affects surface pressure and the gas constant;
It is not referenced in determining humidity, any aspect of the water cycle, or greenhouse heating by water vapour.""")

####Glacial Parameters
def helpglcrs(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Glaciers
False by Default; True allows for new glaciers to form.""")
def helpgrhght(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Glacier Height
0.0 by Default; A value of 0 or greater will place glaciers with that depth in meters over all land surfaces when the model starts.
A value of -1 will not add any initial glaciers.""")
def helpgrthrshld(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Glacier Threshold
2.0 by Default; Sets the minimum depth of accumulated snow required for glaciers to form, in meters.""")

####Model Dynamic Parameters
def helptimestep(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Timestep
45.0 by default; How much time passes in each step of the simulation, in minutes.
Longer timesteps will make the simulation run faster, but it may be less stable and accurate.

For tidal-locked planets 30.0 is recommended, in general if a crash occurs, reduce the timestep
(especially if the Konsole output refers to “non-finite temperatures”).

Generally seems to work better if there are a whole number of timesteps in a 24-hour day.
Timesteps of 5, 6, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, and 60 minutes are all decent options.
(24 * 60) / timestep = an integer""")
def helprunsteps(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Runsteps
11520 by default; How often averaged data is written to an output file(a simulation year), in number of timesteps.
By default this is set for a 360-day year, ExoPlaSim will automatically adjust to different timesteps if not configured here.

This does not alter the simulated planet’s orbital period, or really any aspect of its climate;
it merely alters the period of time referred to in later steps that run the model for a period of years, and the length of time represented in the output files.

Should contain a whole number of NSTPW intervals.
runsteps / NSTPW = an integer""")
def helpsnapshots(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Snapshots
If set, the program will produce a “snapshot” whenever this number of timesteps passes, recording the state of the model at that particular moment.
If using this, it’s recommended to set it to be equal to around 15 days such that it doesn’t slow down the model too much
(480 for a 45-minute timestep. 720 for a 30-minute timestep etc.).""")
def helpnstpw(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: NSTPW (Number of STeps Per Write)
160 by Default; Controls how often data recorded from the model is averaged together, in number of timesteps.

The amount of time this represents should be kept close to 120 hours.
It need not necessarily be a whole number of solar days, though that may be convenient to help keep things straight.
"~4 < (NSTPW * timestep) / 1440 < ~6" should be best.""")
def helphysfltr(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Physics Filter
None by Default; In some cases, it may be necessary to include physics filters.
This typically becomes necessary when sharp features are projected on the model’s smallest spectral modes, causing Gibbs “ripples”.
Earth-like models typically do not require filtering, but tidally-locked models do.
Filtering may be beneficial for Earth-like models at very high resolutions as well, or if there is sharp topography.

Three filter functional forms are included in ExoPlaSim: Cesaro, exponential, and Lander-Hoskins.""")
def helpfltrapp(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Filter Application
None by Default; Physics filters can be applied at two different points;
Either at the transform from gridpoint to spectral (GP), or the reverse (SP). In most cases, the ideal usage is to use both.

Generally, a gridpoint->spectral filter is good for dealing with oscillations caused by sharp jumps and small features in the gridpoint tendencies.
Conversely, a spectral->gridpoint filter is good for dealing with oscillations from small features in spectral fields causing small features to appear in gridpoint tendencies.
Any oscillations not removed by one filter will be amplified through physical feedbacks if not suppressed by the other filter.""")
def helpstmclmtlgy(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Storm Climatology
False by Default; Toggles whether or not storm climatology should be computed.
If True, output fields related to storm climatology will be added to standard output files.

NOTE: Enabling this mode currently roughly doubles the computational cost of the model.""")
def helphghcdnce(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: High Cadence
False by Default; Allows more data to be collected, especially during storm activity.
May allow one to track the development of individual storms, but may not be accurate at low resolutions.""")
def helprntbal(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Run To Balance
False by Default; Runs the model until it appears to have reached equilibrium.
Judged by the balance between average incoming sunlight and outgoing heat remaining unchanged over several years.""")
def helprntme(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Run Time
100 by Default; If Run To Balance not enabled, will run the model for specified amount of years.""")
def helpthrshld(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Threshold
0.0005 by Default; Energy balance threshold model should run to, if using Run To Balance.
In W/m^2/yr average drift in surface energy balance over 45-year timescales.""")
def helpbslne(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Baseline
10 by Default; How many years the simulation has to remain at equilibrium before it is determined to be at balance
(i.e., the amount of drift per year in the balance of incoming and outgoing energy has to remain below the threshold for this many years).""")
def helpmxyr(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Maximum Year
100 by Default; The maximum number of years for the simulation to run, even if it hasn’t reached balance by the end.""")
def helpmnyr(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Minimum Year
10 by Default; The minimum number of years for the simulation to run, even if it has reached balance by the end.""")
def helpcrshibrkn(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Crash If Broken
False by Default; This just helps make crashes a little more graceful and gives somewhat more useful error reports.""")
def helpcln(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Clean
False by Default; Deletes temporary files produced each year once an output has been created.
Should help limit the amount of hard drive space used while running.""")
def helpalrstrts(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: All Years
False by Default; If set to True, moves the output files from every year of the model run; Otherwise, it only moves the final year.
These output files can take up a good bit of hard drive space.

Using this will one average together the data from multiple years when making a koppen map.""")
def helpkprstrts(event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("""Help: Keep Restarts
False by Default; If set to True, moves the restart files—which can be used to restart and continue running the model—as well as the outputs.""")

#Toggle Functions
def tidaltoggle():
    global tidaltog
    if tidaltog == 0:
        tidaltog = 1
        stellon_n.config(state='enabled')
        desync_n.config(state='enabled')
        tempcon_n.config(state='enabled')
    elif tidaltog == 1:
        tidaltog = 0
        stellon_n.config(state='disabled')
        desync_n.config(state='disabled')
        tempcon_n.config(state='disabled')
def aquatoggle():
    global aquatog
    global imgsratogtog
    if aquatog == 0:
        aquatog = 1
        desertp_n.config(state='disabled')
        imgsratogtog_n.config(state='disabled')
        hghtmpimg_n.config(state='disabled')
        hghtmpimg_b.config(state='disabled')
        waterhres_n.config(state='disabled')
        highelev_n.config(state='disabled')
        lowelev_n.config(state='disabled')
        imgdebugtog_n.config(state='disabled')
        sranme_n.config(state='disabled')
        lndsra_n.config(state='disabled')
        lndsra_b.config(state='disabled')
        tposra_n.config(state='disabled')
        tposra_b.config(state='disabled')
    elif aquatog == 1:
        aquatog = 0
        desertp_n.config(state='enabled')
        imgsratogtog_n.config(state='enabled')
        if imgsratogtog == 0:
            hghtmpimg_n.config(state='enabled')
            hghtmpimg_b.config(state='enabled')
            waterhres_n.config(state='enabled')
            highelev_n.config(state='enabled')
            imgdebugtog_n.config(state='enabled')
            sranme_n.config(state='enabled')
            lndsra_n.config(state='disabled')
            lndsra_b.config(state='disabled')
            tposra_n.config(state='disabled')
            tposra_b.config(state='disabled')
        elif imgsratogtog == 1:
            hghtmpimg_n.config(state='disabled')
            hghtmpimg_b.config(state='disabled')
            waterhres_n.config(state='disabled')
            highelev_n.config(state='disabled')
            imgdebugtog_n.config(state='disabled')
            sranme_n.config(state='disabled')
            lndsra_n.config(state='enabled')
            lndsra_b.config(state='enabled')
            tposra_n.config(state='enabled')
            tposra_b.config(state='enabled')
def dsrtoggle():
    global desertog
    global imgsratogtog
    if desertog == 0:
        desertog = 1
        aquap_n.config(state='disabled')
        if imgsratogtog == 0:
            lowelev_n.config(state='enabled')
    elif desertog == 1:
        desertog = 0
        aquap_n.config(state='enabled')
        lowelev_n.config(state='disabled')
def soilalbtoggle():
    global soilalbtog
    if soilalbtog == 0:
        soilalbtog = 1
        soilalb_n.config(state='enabled')
    elif soilalbtog == 1:
        soilalbtog = 0
        soilalb_n.config(state='disabled')
def soildepthtoggle():
    global soildepthtog
    if soildepthtog == 0:
        soildepthtog = 1
        soildepth_n.config(state='enabled')
    elif soildepthtog == 1:
        soildepthtog = 0
        soildepth_n.config(state='disabled')
def capsoiltoggle():
    global capsoiltog
    if capsoiltog == 0:
        capsoiltog = 1
        capsoil_n.config(state='enabled')
    elif capsoiltog == 1:
        capsoiltog = 0
        capsoil_n.config(state='disabled')
def soilwcptoggle():
    global soilwcptog
    if soilwcptog == 0:
        soilwcptog = 1
        soilwcp_n.config(state='enabled')
    elif soilwcptog == 1:
        soilwcptog = 0
        soilwcp_n.config(state='disabled')
def soilsattoggle():
    global soilsattog
    if soilsattog == 0:
        soilsattog = 1
        soilsat_n.config(state='enabled')
    elif soilsattog == 1:
        soilsattog = 0
        soilsat_n.config(state='disabled')
def vegtoggle(self):
    global vegetat_var
    vegetat_variable = vegetat_var.get()
    if vegetat_variable == "None":
        vegacce_n.config(state='disabled')
        initgrw_n.config(state='disabled')
        nfrtgrw_n.config(state='disabled')
        initstcd_n.config(state='disabled')
        initrgh_n.config(state='disabled')
        initslc_n.config(state='disabled')
        initplc_n.config(state='disabled')
    if vegetat_variable != "None":
        vegacce_n.config(state='enabled')
        initgrw_n.config(state='enabled')
        nfrtgrw_n.config(state='enabled')
        initstcd_n.config(state='enabled')
        initrgh_n.config(state='enabled')
        initslc_n.config(state='enabled')
        initplc_n.config(state='enabled')
def snowalbtoggle():
    global snowalbtog
    if snowalbtog == 0:
        snowalbtog = 1
        snowalb_n.config(state='enabled')
    elif snowalbtog == 1:
        snowalbtog = 0
        snowalb_n.config(state='disabled')
def mxsnowtoggle():
    global mxsnowtog
    if mxsnowtog == 0:
        mxsnowtog = 1
        mxsnow_n.config(state='enabled')
    elif mxsnowtog == 1:
        mxsnowtog = 0
        mxsnow_n.config(state='disabled')
def mldepthtoggle():
    global mldepthtog
    if mldepthtog == 0:
        mldepthtog = 1
        mldepth_n.config(state='enabled')
    elif mldepthtog == 1:
        mldepthtog = 0
        mldepth_n.config(state='disabled')
def oceanalbtoggle():
    global oceanalbtog
    if oceanalbtog == 0:
        oceanalbtog = 1
        oceanalb_n.config(state='enabled')
    elif oceanalbtog == 1:
        oceanalbtog = 0
        oceanalb_n.config(state='disabled')
def imgsratoggle():
    global imgsratogtog
    global desertog
    if imgsratogtog == 0:
        imgsratogtog = 1
        aquap_n.config(state='disabled')
        desertp_n.config(state='disabled')
        hghtmpimg_n.config(state='disabled')
        hghtmpimg_b.config(state='disabled')
        waterhres_n.config(state='disabled')
        highelev_n.config(state='disabled')
        lowelev_n.config(state='disabled')
        imgdebugtog_n.config(state='disabled')
        sranme_n.config(state='disabled')
        lndsra_n.config(state='enabled')
        lndsra_b.config(state='enabled')
        tposra_n.config(state='enabled')
        tposra_b.config(state='enabled')
    elif imgsratogtog == 1:
        imgsratogtog = 0
        aquap_n.config(state='enabled')
        desertp_n.config(state='enabled')
        hghtmpimg_n.config(state='enabled')
        hghtmpimg_b.config(state='enabled')
        waterhres_n.config(state='enabled')
        highelev_n.config(state='enabled')
        if desertog == 1:
            lowelev_n.config(state='enabled')
        imgdebugtog_n.config(state='enabled')
        sranme_n.config(state='enabled')
        lndsra_n.config(state='disabled')
        lndsra_b.config(state='disabled')
        tposra_n.config(state='disabled')
        tposra_b.config(state='disabled')
def hghtimgget():
    filename = askopenfilename(filetypes=(("png files","*.png"),("All files","*.*")))
    hghtmpimg_var.set(filename) # add this
def landsraget():
    filename = askopenfilename(filetypes=(("sra files","*.sra"),("All files","*.*")))
    hghtmpimg_var.set(filename) # add this
def toposraget():
    filename = askopenfilename(filetypes=(("sra files","*.sra"),("All files","*.*")))
    hghtmpimg_var.set(filename) # add this
def pressuretoggle():
    global pressuretog
    if pressuretog == 0:
        pressuretog = 1
        pressure_n.config(state='enabled')
    elif pressuretog == 1:
        pressuretog = 0
        pressure_n.config(state='disabled')
def gascontoggle():
    global gascontog
    if gascontog == 0:
        gascontog = 1
        gascon_n.config(state='enabled')
    elif gascontog == 1:
        gascontog = 0
        gascon_n.config(state='disabled')
def ptoggle():
    global ptog
    if ptog == 0:
        ptog = 1
        pH2_n.config(state='enabled')
        pHe_n.config(state='enabled')
        pN2_n.config(state='enabled')
        pO2_n.config(state='enabled')
        pAr_n.config(state='enabled')
        pNe_n.config(state='enabled')
        pKr_n.config(state='enabled')
        pH2O_n.config(state='enabled')
        pCO2_n.config(state='enabled')
    elif ptog == 1:
        ptog = 0
        pH2_n.config(state='disabled')
        pHe_n.config(state='disabled')
        pN2_n.config(state='disabled')
        pO2_n.config(state='disabled')
        pAr_n.config(state='disabled')
        pNe_n.config(state='disabled')
        pKr_n.config(state='disabled')
        pH2O_n.config(state='disabled')
        pCO2_n.config(state='disabled')
def gtoggle():
    global gtog
    if gtog == 0:
        gtog = 1
        inith_n.config(state='enabled')
        mndph_n.config(state='enabled')
    elif gtog == 1:
        gtog = 0
        inith_n.config(state='disabled')
        mndph_n.config(state='disabled')
def stmtoggle():
    global stmtog
    if stmtog == 0:
        stmtog = 1
        highcadtog_n.config(state='enabled')
    elif stmtog == 1:
        stmtog = 0
        highcadtog_n.config(state='disabled')
def baltoggle ():
    global baltog
    if baltog == 0:
        baltog = 1
        runtme_n.config(state='disabled')
        trshld_n.config(state='enabled')
        bselne_n.config(state='enabled')
        maxyr_n.config(state='enabled')
        minyr_n.config(state='enabled')
    elif baltog ==1:
        baltog = 0
        runtme_n.config(state='enabled')
        trshld_n.config(state='disabled')
        bselne_n.config(state='disabled')
        maxyr_n.config(state='disabled')
        minyr_n.config(state='disabled')

#Functions
txtcol = '#0f0f9f'

def system_check():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Configuration Compatability Check:")
    check_year = orbp_var.get()
    check_day = rot_var.get()
    check_time = tmestp_var.get()
    check_run = runstp_var.get()
    check_nsptw = nsptw_var.get()
    time_check = (24*60)/check_time
    if time_check == round(time_check):
        print("Timestep: Nominal")
    else:
        print("WARNING: Current Timestep setting places ratio between (24*60) and timestep at "+str(time_check)+" which may cause problems with ExoPlaSim.")
        time_corct = (24*60)/round(time_check)
        print("Setting it to "+str(time_corct)+" or a factor of a 24 hour day will work better.")
    nsptw_check = (check_nsptw*check_time)/1440
    if 4 <= nsptw_check <= 6:
        print("NSPTW: Nominal")
    else:
        print("WARNING: Current NSPTW setting places day interval at "+str(nsptw_check)+" which may cause problems with ExoPlaSim.")
        print("Changing this to be between 4 and 6 will work better.")
    run_check = check_run/check_nsptw
    if run_check == round(run_check):
        print("Runsteps: Nominal")
    else:
        print("WARNING: Current Runsteps setting places ratio between runsteps and NSPTW at "+str(run_check)+" which may cause problems with ExoPlaSim.")
        print("Setting it to a factor of a 24 hour day will work better.")
    year_check = (check_year*1440)/(check_run*check_time)
    if year_check == 1:
        print("Year: Nominal")
    else:
        print("WARNING: Current Year length places the ratio between (year*1440) and (runsteps*timestep) at "+str(round(year_check, 6))+" which may cause problems with ExoPlaSim.")
        year_corct = (round(year_check)*(check_run*check_time))/1440
        print("Changing this to "+str(year_corct)+" will work better.")
    day_check1 = (check_day*1440)/check_time
    day_check2 = (check_run/12)/((check_day*1440)/check_time)
    if day_check1 == round(day_check1):
        if day_check2 == round(day_check2):
            print("Day: Nominal")
        else:
            print("WARNING: Current day length places ratio between (runsteps/12) and ((day*1440)/timestep) at "+str(day_check2)+" which may cause problems with ExoPlaSim.")
            print("Changeing this to an integer will work better.")
    else:
        print("WARNING: Current day length places ratio between (day*1440) and timestep at "+str(day_check1)+" which may cause problems with ExoPlaSim.")
        print("Changing this to an integer will work better.")

def writeSRA(path,name,kcode,fmap,NLAT,NLON): #Format array and header into sra file, as well as saving it!
    """Write a lat-lon field to a formatted .sra file."""
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass
    sra_label=path+name+'_surf_%04d.sra'%kcode
    sra_header=[kcode,0,11111111,0,NLON,NLAT,0,0]
    sheader = ''
    for h in sra_header:
        sheader+=" %9d"%h
    lines=[]
    i=0
    while i<NLAT*NLON/8:
        l=''
        for n in fmap[i,:]:
            l+=' %9.3f'%n
        lines.append(l)
        i+=1
    sra_text=sheader+'\n'+'\n'.join(lines)
    with open(sra_label, "w") as f:
        #f=open(sra_label,'w')
        f.write(sra_text)
        f.close()

def chunk(arr, nrows, ncols): #Split an array into chunks
    '''
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    '''
    h, w = arr.shape
    assert h % nrows == 0, "{} rows is not evenly divisble by {}".format(h, nrows)
    assert w % ncols == 0, "{} cols is not evenly divisble by {}".format(w, ncols)
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

def color_ocean(inarray, outlist, w, h): #turn 0/1 array to black/white (ocean/land) array
	for y in range(w):
		for x in range(h):
			col = inarray[x,y]
			if col > 0:
				rgb = (int(col*255),int(col*255),int(col*255))
			else:
				rgb = (0,0,0)
			outlist.append(rgb)
def color_land(inarray, outlist, w, h): #turn array to white (land) array
	for y in range(w):
		for x in range(h):
			rgb = (255,255,255)
			outlist.append(rgb)

def save_file():
    """Save the current file."""
    filepath = asksaveasfilename(
        defaultextension="py",
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")],
    )
    if not filepath:
        return
#Getting input text
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    nametext = str(name_var.get())
    yeartext = str(year_var.get())
    typetext = str(output_var.get())
    cpustext = str(cpu_var.get())
    prestext = str(pres_var.get())
    resotext = str(res_var.get())
    crastext = str(crash_var.get())
    layertext = str(layers_var.get())
    recomptext = str(recom_var.get())
    startext = str(startemp_var.get())
    fluxtext = str(flux_var.get())
    orbptext = str(orbp_var.get())
    eccetext = str(ecc_var.get())
    oblitext = str(obli_var.get())
    lonvtext = str(lon_var.get())
    fixotext = str(fixed_var.get())
    rotptext = str(rot_var.get())
    tidltext = str(tidal_var.get())
    steltext = str(stellon_var.get())
    dsynctext = str(desync_var.get())
    tmpcntext = str(tempcon_var.get())
    gravtext = str(gravity_var.get())
    radustext = str(radius_var.get())
    orogtext = str(orogph_var.get())
    aquaptext = str(aquap_var.get())
    dsrtptext = str(desertp_var.get())
    vegtext = str(vegetat_var.get())
    vacctext = str(vegacce_var.get())
    biogrwtext = str(nfrtgrw_var.get())
    initgrwtext = str(initgrw_var.get())
    stomatext = str(initstcd_var.get())
    vroughtext = str(initrgh_var.get())
    slcartext = str(initslc_var.get())
    pltcartext = str(initplc_var.get())
    wtsoiltext = str(wetso_var.get())
    slalbtext = str(soilalbtog_var.get())
    solalbtext = str(soilalb_var.get())
    sldpthtext = str(soildepthtog_var.get())
    soldpthtext = str(soildepth_var.get())
    cpsltext = str(capsoiltog_var.get())
    capsoltext = str(capsoil_var.get())
    slwcptext = str(soilwcptog_var.get())
    solwcptext = str(soilwcp_var.get())
    slsattext = str(soilsattog_var.get())
    solsattext = str(soilsat_var.get())
    snwalbtext = str(snowalbtog_var.get())
    snowalbtext = str(snowalb_var.get())
    mxsnwtext = str(mxsnowtog_var.get())
    maxsnwtext = str(mxsnow_var.get())
    sicetext = str(seaice_var.get())
    ocnalbtext = str(oceanalbtog_var.get())
    oceanalbtext = str(oceanalb_var.get())
    mldphtext = str(mldepthtog_var.get())
    mixldphtext = str(mldepth_var.get())
    ocnzntext = str(oceanzen_var.get())
    imgsratext = str(imgsratogtog_var.get())
    hghtimgpath = hghtmpimg_var.get()
    wtrthreshtext = str(waterhres_var.get())
    hghelvtext = str(highelev_var.get())
    lwelvtext = str(lowelev_var.get())
    imgdbgtext = str(imgdebugtog_var.get())
    sranmetext = str(sranme_var.get())
    landsratext = str(lndsra_var.get())
    toposratext = str(tposra_var.get())
    prssretogtext = str(pressuretog_var.get())
    pressuretext = str(pressure_var.get())
    gascontogtext = str(gascontog_var.get())
    gascontext = str(gascon_var.get())
    drycretext = str(drycoretog_var.get())
    ozonetext = str(ozone_var.get())
    prtlprssretext = str(partialptog_var.get())
    H2text = str(pH2_var.get())
    Hetext = str(pHe_var.get())
    N2text = str(pN2_var.get())
    O2text = str(pO2_var.get())
    Artext = str(pAr_var.get())
    Netext = str(pNe_var.get())
    Krtext = str(pKr_var.get())
    H2Otext = str(pH2O_var.get())
    CO2text = str(pCO2_var.get())
    glaciertext = str(glacialtog_var.get())
    initheightext = str(inith_var.get())
    mindepthtext = str(mndph_var.get())
    timesteptext = str(tmestp_var.get())
    runsteptext = str(runstp_var.get())
    snapshotext = str(snpsht_var.get())
    nsptwtext = str(nsptw_var.get())
    physics1text = str(phyfilt1_var.get())
    physics2text = str(phyfilt2_var.get())
    stormtext = str(stormcltog_var.get())
    highcadtext = str(highcadtog_var.get())
    runtobaltext = str(rntbaltog_var.get())
    runtimetext = str(runtme_var.get())
    thresholdtext = str(trshld_var.get())
    baselinetext = str(bselne_var.get())
    maxyeartext = str(maxyr_var.get())
    minyeartext = str(minyr_var.get())
    crashbrkntext = str(cshibrktog_var.get())
    cleantext = str(cleantog_var.get())
    allyearstext = str(allyrstog_var.get())
    keeprstrtstext = str(kprststog_var.get())
    print("Inputs gathered...")

    """Convert heightmap image to SRA files."""
    if aquaptext == "False":
        aquaplanetext = ''
        if imgsratext == "False":
            print("Beginning Image -> SRA Conversion...")
            sra_path = path.dirname(filepath)+'/'
            infile = hghtimgpath
            grav = float(gravtext)
            if imgdbgtext == "True":
                debug_img = 1
                print("Debug Images Enabled...")
            else:
                debug_img = 0
            red_img = imread(infile)[:,:,0] #opens red channel
            green_img = imread(infile)[:,:,1] #opens green channel
            blue_img = imread(infile)[:,:,2] #opens blue channel
            grey_img = (red_img+green_img+blue_img)/3 #averages color channels and scales from 0-1
            img_width = len(grey_img[0]) #finds image width
            img_height = len(grey_img) #finds image height
            img_rgb = []
            if dsrtptext == "False":
                floor_value = int(wtrthreshtext)
                peak_value = float(hghelvtext)
                greyscale_img = grey_img*255 #converts 0-1 to 0-255
                max_img = 255-(floor_value) #max value lowered by floor value
                rescaled_img = (greyscale_img-(floor_value)) #array lowered by floor value
                rescaled_img[rescaled_img <= 0] = 0 #any negative value becomes 0 (ocean)
                rescaled_img = (rescaled_img/max_img)*peak_value*grav #array converted to 0-1, before multiplied by max height and gravity (geopotential)
                min = float(np.min(rescaled_img)) #finds the min height (should be 0)
                max = float(np.max(rescaled_img)) #finds the max height (should be near absolute max height)
                color_ocean(rescaled_img, img_rgb, img_width, img_height)
            else:
                trench_value = float(lwelvtext)
                peak_value = float(hghelvtext)
                range_value = peak_value-trench_value
                rescaled_img = ((grey_img*range_value)-trench_value)*grav #converts 0-1 to trench-peak times gravity (geopotential)
                min = float(np.min(rescaled_img)) #finds the min height (should be near deepest depth)
                max = float(np.max(rescaled_img)) #finds the max height (should be near absolute max height)
                color_land(rescaled_img, img_rgb, img_width, img_height)
            if debug_img == 1:
                img = Image.new('RGB',(img_height,img_width)) #print original image
                img.putdata(img_rgb)
                img = img.transpose(Image.ROTATE_90)
                img = ImageOps.flip(img)
                img.save(sra_path+"LandMaskOriginal.png")
                print("Debug Image 1 printed...")
            options = {"T21": 32,"T42": 64,"T63": 96,"T85": 128,"T106": 160,"T127": 192,"T170": 256}
            for i in range(1000000):
                if resotext in options:
                    height = options[resotext]
                    width = 2*height
            scale_width = img_width/width #finds the ratio between starting and final width
            scale_height = img_height/height #finds the ratio between starting and final height
            print("Width ratio: "+str(scale_width))
            print("Height ratio: "+str(scale_height))
            #tests to see whether original image is a multiple of desired resolution, before splitting the array into chunks if it is
            if scale_width == round(scale_width):
                if scale_height == round(scale_height):
                    width_ratio = int(scale_width) #width ratio between original and resized image
                    height_ratio = int(scale_height) #height ratio between original and resized image
                    chunked = chunk(rescaled_img, height_ratio, width_ratio) #splits the geopotential array into a 3d array
                    length_ratio = len(chunked) #finds the length of the 3d array
                    print("All ratios are good!")
                else:
                    print("Height ratio incompatible, please try to have the image resolution as a multiple of the output resolution.")
            else:
                print("Width ratio incompatible, please try to have the image resolution as a multiple of the output resolution.")
            img_rgb = []
            if dsrtptext == "False":
                b_w = chunked.copy()[:,:,:] #new empty 3d array, avoids overriding original array!
                for x in range(length_ratio):
                    for y in range(width_ratio):
                        for z in range(height_ratio):
                            checker = chunked[x,y,z]
                            if checker > 0: #converts 3d geopotential array to 3d land mask array
                                b_w[x,y,z] = 1
                            else:
                                b_w[x,y,z] = 0
                b_w = b_w.mean(axis=(1,2)) #averages land mask array into 1d list
                dechunked = chunked.mean(axis=(1,2)) #simpler approach, since there's no ocean there's no need to check for it, so just average all the land to 1d list
                dechunked = np.reshape(dechunked, (height, width)) #reshapes list to equirectangular 2d array
                b_w = np.reshape(b_w, (height, width))
                color_ocean(b_w, img_rgb, width, height) #converts to land mask
            else:
                dechunked = chunked.mean(axis=(1,2)) #simpler approach, since there's no ocean there's no need to check for it, so just average all the land to 1d list
                dechunked = np.reshape(dechunked, (height, width)) #reshapes list to equirectangular 2d array
                b_w = dechunked + 1
                color_land(dechunked, img_rgb, width, height) #converts to land mask
            if debug_img == 1:
                img = Image.new('RGB',(height,width)) #print resized image
                img.putdata(img_rgb)
                img = img.transpose(Image.ROTATE_90)
                img = ImageOps.flip(img)
                img.save(sra_path+"LandMaskSmall.png")
                print("Debug Image 2 printed...")
            list_image = dechunked.flatten() #Flattens 2d array into list
            b_w = b_w.flatten()
            sra_129 = np.array(list_image).reshape(-1, 8) #Rearranges list into 2d array that matches sra format
            sra_172 = np.array(b_w).reshape(-1, 8)
            if dsrtptext == "False":
                sra_172[:,:] = 1 #Everything becomes land
            fl_height = float(height) #Apparently it doesn't like integers
            fl_width = float(width)
            sra_name = sranmetext
            sra_final_path = sra_path+'SRA/'
            writeSRA(sra_final_path,sra_name,172,sra_172,fl_height,fl_width)
            writeSRA(sra_final_path,sra_name,129,sra_129,fl_height,fl_width)
            print("Conversion successful!") #Nice!
            print("Formatting...")
            landmaptext = 'landmap="SRA/'+sranmetext+'_surf_0172.sra",'
            topomaptext = 'topomap="SRA/'+sranmetext+'_surf_0129.sra",'
        else:
            lndsrafle = ntpath.basename(landsratext)
            tposrafle = ntpath.basename(toposratext)
            sra_path = path.dirname(filepath)+'/SRA'
            try:
                os.makedirs(sra_path)
            except FileExistsError:
                # directory already exists
                pass
            shutil.copyfile(landsratext, sra_path)
            shutil.copyfile(toposratext, sra_path)
            landmaptext = 'landmap="SRA/'+lndsrafle+'",'
            topomaptext = 'topomap="SRA/'+tposrafle+'"<'
    else:
        print("Formatting...")
        aquaplanetext = 'aquaplanet=True,'
        landmaptext = ''
        topomaptext = ''
    if dsrtptext == "True":
        dsrtplanetext = 'desertplanet=True,'
    else:
        dsrtplanetext = ''

    #Conditions
    if crastext == "True":
        crashtext = ',crashtolerant='+crastext
    else:
        crashtext = ''
    if recomptext == "True":
        recomtext = ',recompile='+recomptext
    else:
        recomtext = ''
    if tidltext == "True":
        rottext = 'synchronous='+tidltext+',substellarlon='+steltext+',desync='+dsynctext+',tlcontrast='+tmpcntext
    else:
        rottext = 'rotationperiod='+rotptext
    if vegtext == "None":
        vegetationtext = ''
    else:
        if vegtext == "Proscribed":
            vegstat = '				  vegetation=1'+',vegaccel='+vacctext+',nforestgrowth='+biogrwtext+',initgrowth='+initgrwtext
        elif vegtext == "Dynamic":
            vegstat = '				  vegetation=2'+',vegaccel='+vacctext+',nforestgrowth='+biogrwtext+',initgrowth='+initgrwtext
        vegetationtext = vegstat+',initstomcond='+stomatext+',initrough='+vroughtext+',initsoilcarbon='+slcartext+',initplantcarbon='+pltcartext+',\n'
    if slalbtext == "True":
        soilalbtext = ",soilalbedo="+solalbtext
    else:
        soilalbtext = ''
    if sldpthtext == "True":
        soildepthtext = ",soildepth="+soldpthtext
    else:
        soildepthtext = ''
    if cpsltext == "True":
        soilhcaptext = ",cpsoil="+capsoltext
    else:
        soilhcaptext = ''
    if slwcptext == "True":
        soilwcaptext = ",soilwatercap="+solwcptext
    else:
        soilwcaptext = ''
    if slsattext == "True":
        soilsattext = ",soilsaturation="+solsattext
    else:
        soilsattext = ''
    if snwalbtext == "True":
        snowalbtext = ",snowicealbedo="+snowalbtext
    else:
        snowalbtext = ''
    if mxsnwtext == "True":
        maxsnowtext = ",maxsnow="+maxsnwtext
    else:
        maxsnowtext = ''
    if ocnalbtext == "True":
        oceanalbtext = ",oceanalbedo="+oceanalbtext
    else:
        oceanalbtext = ''
    if mldphtext == "True":
        mixedlyrtext = ",mldepth="+mixldphtext
    else:
        mixedlyrtext = ''
    surfacetext1 = wtsoiltext+soilalbtext+soildepthtext+soilhcaptext+soilwcaptext+soilsattext+snowalbtext
    surfacetext2 = maxsnowtext+',seaice='+sicetext+oceanalbtext+mixedlyrtext+',oceanzenith="'+ocnzntext+'",\n'
    if prssretogtext == "True":
        atmospheretext = "pressure="+pressuretext+','
    else:
        atmospheretext = ''
    if gascontogtext == "True":
        atmospheretext = atmospheretext+'gascon='+gascontext+','
    else:
        atmospheretext = atmospheretext+''
    if drycretext == "True":
        atmospheretext = atmospheretext+'drycore=True,'
    else:
        atmospheretext = atmospheretext+'drycore=False,'
    if ozonetext == "True":
        atmospheretext = atmospheretext+'ozone=True,'
    else:
        atmospheretext = atmospheretext+'ozone=False,'
    if prtlprssretext == "True":
        ppressuretext = "				  pH2="+H2text+',pHe='+Hetext+',pN2='+N2text+',pO2='+O2text+',pAr='+Artext+',pNe='+Netext+',pKr='+Krtext+',pH2O='+H2Otext+',pCO2='+CO2text+',\n'
    else:
        ppressuretext = ''
    if glaciertext == "True":
        glacialtext = "				  glacier={‘toggle’: True, ‘mindepth’: "+mindepthtext+', ‘initialh’: '+initheightext+'},\n'
    else:
        glacialtext = ''
    snapshotext = int(snapshotext)
    if snapshotext > 0:
        snapshotstext = ',snapshots='+snapshotext
    else:
        snapshotstext = ''
    if physics1text == "None":
        physicstext = ''
    elif physics1text == "Cesaro":
        if physics2text == "None":
            physicstext = ''
        elif physics2text == "GP":
            physicstext = ",physicsfilter='gp|cesaro'"
        elif physics2text == "SP":
            physicstext = ",physicsfilter='cesaro|sp'"
        elif physics2text == "GP + SP":
            physicstext = ",physicsfilter='gp|cesaro|sp'"
    elif physics1text == "Exp":
        if physics2text == "None":
            physicstext = ''
        elif physics2text == "GP":
            physicstext = ",physicsfilter='gp|exp'"
        elif physics2text == "SP":
            physicstext = ",physicsfilter='exp|sp'"
        elif physics2text == "GP + SP":
            physicstext = ",physicsfilter='gp|exp|sp'"
    elif physics1text == "Lh":
        if physics2text == "None":
            physicstext = ''
        elif physics2text == "GP":
            physicstext = ",physicsfilter='gp|lh'"
        elif physics2text == "SP":
            physicstext = ",physicsfilter='lh|sp'"
        elif physics2text == "GP + SP":
            physicstext = ",physicsfilter='gp|lh|sp'"
    if stormtext == "True":
        if highcadtext == "True":
            stormstext = ",\n				  stormcapture={'toggle': 1,'NKTRIGGER': 1},highcadence={'toggle': 1,'start': 320,'interval': 4,'end': 576})\n"
        else:
            stormstext = ",\n				  stormcapture={'toggle': 1,'NKTRIGGER': 1})\n"
    else:
        stormstext = ')\n'
    if runtobaltext == "True":
        runtext = nametext+'.runtobalance(threshold='+thresholdtext+',baseline='+baselinetext+',maxyears='+maxyeartext+',minyears='+minyeartext
    else:
        runtext = nametext+'.run(years='+runtimetext

#Formatting
    format_name = "import exoplasim as exo\n"+nametext+' = exo.Model(workdir="'+nametext+'",modelname="'+nametext+'",'
    format_model = "inityear="+yeartext+',outputtype="'+typetext+'",ncpus='+cpustext+',precision='+prestext+',resolution='+resotext+crashtext+',layers='+layertext+recomtext+')\n'
    format_stellar = nametext+".configure(startemp="+startext+',flux='+fluxtext+',\n'
    format_orbit = "				  year="+orbptext+',eccentricity='+eccetext+',obliquity='+oblitext+',lonvernaleq='+lonvtext+',fixedorbit='+fixotext+',\n'
    format_rotation = "				  "+rottext+',\n'
    format_planet = '				  gravity='+gravtext+',radius='+radustext+',orography='+orogtext+',\n'
    format_vegetation = vegetationtext
    format_surface = "				  wetsoil="+surfacetext1+surfacetext2
    format_geography = "				  "+aquaplanetext+dsrtplanetext+landmaptext+topomaptext+'\n'
    format_atmosphere = "				  "+atmospheretext+'\n'
    format_ppressure = ppressuretext
    format_glacier = glacialtext
    format_timekeep = "				  timestep="+timesteptext+',runsteps='+runsteptext+snapshotstext+",otherargs={'NSTPW@plasim_namelist':'"+nsptwtext+"'}"+physicstext
    format_storms = stormstext
    format_export = nametext+".exportcfg()\n"
    format_run = runtext+',crashifbroken='+crashbrkntext+',clean='+cleantext+')\n'
    format_finalise = nametext+'.finalize(allyears='+allyearstext+',keeprestarts='+keeprstrtstext+')\n'
    format_save = nametext+'.save()'
    print("Formatting Complete...")
#Writing to file
    print("Saving Main File...")
    with open(filepath, "w") as output_file:
        output_file.write(format_name)
        output_file.write(format_model)
        output_file.write(format_stellar)
        output_file.write(format_orbit)
        output_file.write(format_rotation)
        output_file.write(format_planet)
        output_file.write(format_vegetation)
        output_file.write(format_surface)
        output_file.write(format_geography)
        output_file.write(format_atmosphere)
        output_file.write(format_ppressure)
        output_file.write(format_glacier)
        output_file.write(format_timekeep)
        output_file.write(format_storms)
        output_file.write(format_export)
        output_file.write(format_run)
        output_file.write(format_finalise)
        output_file.write(format_save)
        print("Saving Complete!")

window = Tk()# Start the application
window.title("ExoPlaSim: Input Configurator (EPS:IC)")
window.rowconfigure([2], minsize=10, weight=0)
window.columnconfigure([2,4,6,8], minsize=10, weight=1)

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=7)
text_font = font.nametofont("TkTextFont")
text_font.configure(size=7)

#------------------------------------------------------------------------------------------------------------ DONE
#------------------------------------------------------------------------------------------------------------ DONE
#------------------------------------------------------------------------------------------------------------ DONE

col_one_frame = Frame()
col_one_frame.grid(row=1,column=1,sticky="n")
col_one_frame.rowconfigure([2,4,6], minsize=10, weight=1)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Model Parameter Frame
modpar_frame = Frame(master=col_one_frame,relief=GROOVE,borderwidth=3)
modpar_frame.grid(row=1,column=1,sticky="new")
modpar_frame.rowconfigure([1,2,3,4,5,6,7,8,9], minsize=20)

modelparam = Label(master=modpar_frame,text="Model Parameters")
modelparam.grid(row=0, column=1,columnspan=2,sticky="n")

#Project Name
project = Label(master=modpar_frame,text="Project Name: ",foreground=txtcol)
project.bind("<Button-1>", helpjctnme)
project.grid(row=1, column=1, sticky="w")
name_var = StringVar()
name_var.set('Earth')
name = Entry(master=modpar_frame,width=7, textvariable=name_var)
name.grid(row=1, column=2, sticky="w")

#Start Year
year = Label(master=modpar_frame,text="Start Year: ",foreground=txtcol)
year.bind("<Button-1>", helpstrtyr)
year.grid(row=2, column=1, sticky="w")
year_var = IntVar()
year_var.set(1)
year_n = Entry(master=modpar_frame,textvariable=year_var, width=7)
year_n.grid(row=2, column=2, sticky="w")

#Output Type
outputtype = Label(master=modpar_frame,text="Output Type: ",foreground=txtcol)
outputtype.bind("<Button-1>", helpotptype)
outputtype.grid(row=3, column=1, sticky="w")
output_options = [".nc", ".nc", ".npy", ".npz", ".hdf5", ".he5", ".h5", ".csv", ".gz", ".txt", ".tar", ".tar.gz", ".tar.xz", ".tar.bz2"]
output_var = StringVar()
output_var.set(output_options[0])
outputtxt = OptionMenu(modpar_frame, output_var, *output_options)
outputtxt.config(width=6)
outputtxt.grid(row=3,column=2, sticky="w")

#CPU Count
cpu = Label(master=modpar_frame,text="CPU Count: ",foreground=txtcol)
cpu.bind("<Button-1>", helpcpucnt)
cpu.grid(row=4, column=1, sticky="w")
cpu_var = IntVar()
cpu_var.set(4)
cpu_n = Entry(master=modpar_frame,textvariable=cpu_var, width=7)
cpu_n.grid(row=4, column=2, sticky="w")

#Precision
pres = Label(master=modpar_frame,text="Precision: ",foreground=txtcol)
pres.bind("<Button-1>", helpresision)
pres.grid(row=5, column=1, sticky="w")
pres_options = ["8", "4", "8"]
pres_var = StringVar()
pres_var.set(pres_options[0])
pres_n = OptionMenu(modpar_frame, pres_var, *pres_options)
pres_n.config(width=6)
pres_n.grid(row=5, column=2, sticky="w")

#Resolution
resolution = Label(master=modpar_frame,text="Resolution: ",foreground=txtcol)
resolution.bind("<Button-1>", helpresolution)
resolution.grid(row=6, column=1, sticky="w")
res_options = ["T21", "T21", "T42", "T63", "T85", "T106", "T127", "T170"]
res_var = StringVar()
res_var.set(res_options[0])
res = OptionMenu(modpar_frame, res_var, *res_options)
res.config(width=6)
res.grid(row=6,column=2, sticky="w")

#Crash Tolerant
crash = resolution = Label(master=modpar_frame,text="Crash Tolerant: ",foreground=txtcol)
crash.bind("<Button-1>", helpcrshtlrnt)
crash.grid(row=7, column=1, sticky="w")
crash_var = StringVar()
crash_var.set("False")
crashtol = Checkbutton(master=modpar_frame,variable=crash_var, onvalue='True', offvalue='False')
crashtol.grid(row=7, column=2, sticky="w")

#Layers
layers = Label(master=modpar_frame,text="Layers: ",foreground=txtcol)
layers.bind("<Button-1>", helplayers)
layers.grid(row=8, column=1, sticky="w")
layers_var = IntVar()
layers_var.set(10)
layers_n = Entry(master=modpar_frame,textvariable=layers_var, width=7)
layers_n.grid(row=8, column=2, sticky="w")

#Recompile
recom = resolution = Label(master=modpar_frame,text="Recompile: ",foreground=txtcol)
recom.bind("<Button-1>", helprecompile)
recom.grid(row=9, column=1, sticky="w")
recom_var = StringVar()
recom_var.set("False")
recom_n = Checkbutton(master=modpar_frame,variable=recom_var, onvalue='True', offvalue='False')
recom_n.grid(row=9, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Stellar Parameter Frame
stelpar_frame = Frame(master=col_one_frame,relief=GROOVE,borderwidth=3)
stelpar_frame.grid(row=3,column=1,sticky="new")
stelpar_frame.rowconfigure([1,2], minsize=20)

modelparam = Label(master=stelpar_frame,text="Stellar Parameters")
modelparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Star Temperature
startemp = Label(master=stelpar_frame,text="Star Temp. (K): ",foreground=txtcol)
startemp.bind("<Button-1>", helpstrtmp)
startemp.grid(row=1, column=1, sticky="w")
startemp_var = DoubleVar()
startemp_var.set(5772.0)
startemp_n = Entry(master=stelpar_frame,textvariable=startemp_var, width=7)
startemp_n.grid(row=1, column=2, sticky="w")

#Stellar Flux
flux = Label(master=stelpar_frame,text="Stellar Flux (W/m²): ",foreground=txtcol)
flux.bind("<Button-1>", helpstlrflx)
flux.grid(row=2, column=1, sticky="w")
flux_var = DoubleVar()
flux_var.set(1367.0)
flux_n = Entry(master=stelpar_frame,textvariable=flux_var, width=7)
flux_n.grid(row=2, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Orbital Parameter Frame
orbitpar_frame = Frame(master=col_one_frame,relief=GROOVE,borderwidth=3)
orbitpar_frame.grid(row=5,column=1,sticky="new")
orbitpar_frame.rowconfigure([1,2,3,4,5,6], minsize=20)

orbitparam = Label(master=orbitpar_frame,text="Orbital Parameters")
orbitparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Orbital Period
orbp = Label(master=orbitpar_frame,text="Year Length (E. Days): ",foreground=txtcol)
orbp.bind("<Button-1>", helpyrlngth)
orbp.grid(row=1, column=1, sticky="w")
orbp_var = DoubleVar()
orbp_var.set(365.25)
orbp_n = Entry(master=orbitpar_frame,textvariable=orbp_var, width=7)
orbp_n.grid(row=1, column=2, sticky="w")

#Rotation Period
rot = Label(master=orbitpar_frame,text="Day Length (E. Days): ",foreground=txtcol)
rot.bind("<Button-1>", helpdaylngth)
rot.grid(row=2, column=1, sticky="w")
rot_var = DoubleVar()
rot_var.set(1.0)
rot_n = Entry(master=orbitpar_frame,textvariable=rot_var, width=7)
rot_n.grid(row=2, column=2, sticky="w")

#Eccentricity
ecc = Label(master=orbitpar_frame,text="Eccentricity: ",foreground=txtcol)
ecc.bind("<Button-1>", helpeccentr)
ecc.grid(row=3, column=1, sticky="w")
ecc_var = DoubleVar()
ecc_var.set(0.016715)
ecc_n = Entry(master=orbitpar_frame,textvariable=ecc_var, width=7)
ecc_n.grid(row=3, column=2, sticky="w")

#Obliquity
obli = Label(master=orbitpar_frame,text="Obliquity (°): ",foreground=txtcol)
obli.bind("<Button-1>", helpoblqty)
obli.grid(row=4, column=1, sticky="w")
obli_var = DoubleVar()
obli_var.set(23.441)
obli_n = Entry(master=orbitpar_frame,textvariable=obli_var, width=7)
obli_n.grid(row=4, column=2, sticky="w")

#Longitude of Periapsis
lon = Label(master=orbitpar_frame,text="Long. of Periapsis (°): ",foreground=txtcol)
lon.bind("<Button-1>", helplngpri)
lon.grid(row=5, column=1, sticky="w")
lon_var = DoubleVar()
lon_var.set(102.7)
lon_n = Entry(master=orbitpar_frame,textvariable=lon_var, width=7)
lon_n.grid(row=5, column=2, sticky="w")

#Fixed Orbit
fixed = Label(master=orbitpar_frame,text="Fixed Orbit: ",foreground=txtcol)
fixed.bind("<Button-1>", helpfxdobt)
fixed.grid(row=6, column=1, sticky="w")
fixed_var = StringVar()
fixed_var.set('True')
fixedorb = Checkbutton(master=orbitpar_frame,variable=fixed_var, onvalue='True', offvalue='False')
fixedorb.grid(row=6, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_two_frame = Frame()
col_two_frame.grid(row=1,column=3,sticky="n")
col_two_frame.rowconfigure([2,4], minsize=10, weight=1)

#---------------------------------------------------------------------------DONE
#---------------------------------------------------------------------------DONE
#---------------------------------------------------------------------------DONE

#Rotational Parameter Frame
rotatpar_frame = Frame(master=col_two_frame,relief=GROOVE,borderwidth=3)
rotatpar_frame.grid(row=1,column=1,sticky="new")
rotatpar_frame.rowconfigure([1,2,3,4], minsize=20)
rotatpar_frame.columnconfigure([2], minsize=60)

rotatparam = Label(master=rotatpar_frame,text="Rotational Parameters")
rotatparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Tidally Locked
tidal = Label(master=rotatpar_frame,text="Tidally Locked: ",foreground=txtcol)
tidal.bind("<Button-1>", helptdlkd)
tidal.grid(row=1, column=1, sticky="w")
tidal_var = StringVar()
tidal_var.set('False')
tidalock = Checkbutton(master=rotatpar_frame,variable=tidal_var,command=tidaltoggle, onvalue='True', offvalue='False')
tidalock.grid(row=1, column=2, sticky="w")

#Substellar Longitude
stellon = Label(master=rotatpar_frame,text="Substellar Longitude (°): ",foreground=txtcol)
stellon.bind("<Button-1>", helpsbstlrlng)
stellon.grid(row=2, column=1, sticky="w")
stellon_var = DoubleVar()
stellon_var.set(180)
stellon_n = Entry(master=rotatpar_frame,textvariable=stellon_var, width=7)
stellon_n.config(state='disabled')
stellon_n.grid(row=2, column=2, sticky="w")

#Desync
desync = Label(master=rotatpar_frame,text="Substellar Desync (°/min): ",foreground=txtcol)
desync.bind("<Button-1>", helpsbstlrdsync)
desync.grid(row=3, column=1, sticky="w")
desync_var = DoubleVar()
desync_var.set(0.0)
desync_n = Entry(master=rotatpar_frame,textvariable=desync_var, width=7)
desync_n.config(state='disabled')
desync_n.grid(row=3, column=2, sticky="w")

#Temp. Contrast
tempcon = Label(master=rotatpar_frame,text="Temp. Contrast (K): ",foreground=txtcol)
tempcon.bind("<Button-1>", helptmpcntrst)
tempcon.grid(row=4, column=1, sticky="w")
tempcon_var = DoubleVar()
tempcon_var.set(0.0)
tempcon_n = Entry(master=rotatpar_frame,textvariable=tempcon_var, width=7)
tempcon_n.config(state='disabled')
tempcon_n.grid(row=4, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Planetary Parameters Frame
planetpar_frame = Frame(master=col_two_frame,relief=GROOVE,borderwidth=3)
planetpar_frame.grid(row=3,column=1,sticky="new")
planetpar_frame.rowconfigure([1,2,3,4,5], minsize=20)
planetpar_frame.columnconfigure([2], minsize=100)

planetparam = Label(master=planetpar_frame,text="Planetary Parameters")
planetparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Surface Gravity
gravity = Label(master=planetpar_frame,text="Gravity (m/s²): ",foreground=txtcol)
gravity.bind("<Button-1>", helpgrvty)
gravity.grid(row=1, column=1, sticky="w")
gravity_var = DoubleVar()
gravity_var.set(9.80665)
gravity_n = Entry(master=planetpar_frame,textvariable=gravity_var, width=7)
gravity_n.grid(row=1, column=2, sticky="w")

#Radius
radius = Label(master=planetpar_frame,text="Radius (E. Radii): ",foreground=txtcol)
radius.bind("<Button-1>", helprdus)
radius.grid(row=2, column=1, sticky="w")
radius_var = DoubleVar()
radius_var.set(1.0)
radius_n = Entry(master=planetpar_frame,textvariable=radius_var, width=7)
radius_n.grid(row=2, column=2, sticky="w")

#Orography
orogph = Label(master=planetpar_frame,text="Orography: ",foreground=txtcol)
orogph.bind("<Button-1>", helporgrphy)
orogph.grid(row=3, column=1, sticky="w")
orogph_var = DoubleVar()
orogph_var.set(1.0)
orogph_n = Entry(master=planetpar_frame,textvariable=orogph_var, width=7)
orogph_n.grid(row=3, column=2, sticky="w")

#Aqua Planet
aquap = Label(master=planetpar_frame,text="Aqua Planet: ",foreground=txtcol)
aquap.bind("<Button-1>", helpaquaplnt)
aquap.grid(row=4, column=1, sticky="w")
aquap_var = StringVar()
aquap_var.set('False')
aquap_n = Checkbutton(master=planetpar_frame,variable=aquap_var,command=aquatoggle, onvalue='True', offvalue='False')
aquap_n.config(state='enabled')
aquap_n.grid(row=4, column=2, sticky="w")

#Desert Planet
desertp = Label(master=planetpar_frame,text="Desert Planet: ",foreground=txtcol)
desertp.bind("<Button-1>", helpdsrtplnt)
desertp.grid(row=5, column=1, sticky="w")
desertp_var = StringVar()
desertp_var.set('False')
desertp_n = Checkbutton(master=planetpar_frame,variable=desertp_var,command=dsrtoggle, onvalue='True', offvalue='False')
desertp_n.config(state='enabled')
desertp_n.grid(row=5, column=2, sticky="w")

#---------------------------------------------------------------------------DONE
#---------------------------------------------------------------------------DONE
#---------------------------------------------------------------------------DONE

#Vegetation Parameter Frame
vegpar_frame = Frame(master=col_two_frame,relief=GROOVE,borderwidth=3)
vegpar_frame.grid(row=5,column=1,sticky="new")
vegpar_frame.rowconfigure([1,2,3,4,5,6,7,8], minsize=20)

vegparam = Label(master=vegpar_frame,text="Vegetation Parameters")
vegparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Vegetation
vegetat = Label(master=vegpar_frame,text="Vegetation: ",foreground=txtcol)
vegetat.bind("<Button-1>", helpvgtn)
vegetat.grid(row=1, column=1, sticky="w")
vegetat_options = ["None", "None", "Proscribed", "Dynamic"]
vegetat_var = StringVar()
vegetat_var.set(vegetat_options[0])
vegetat_n = OptionMenu(vegpar_frame, vegetat_var, *vegetat_options, command=vegtoggle)
vegetat_n.config(width=7)
vegetat_n.grid(row=1, column=2, sticky="w")

#Veg. Acceleration
vegacce = Label(master=vegpar_frame,text="Veg. Acceleration: ",foreground=txtcol)
vegacce.bind("<Button-1>", helpvgaclrtn)
vegacce.grid(row=2, column=1, sticky="w")
vegacce_var = IntVar()
vegacce_var.set(1)
vegacce_n = Entry(master=vegpar_frame,textvariable=vegacce_var, width=7)
vegacce_n.config(state='disabled')
vegacce_n.grid(row=2, column=2, sticky="w")

#Biomass Growth
nfrtgrw = Label(master=vegpar_frame,text="Biomass Growth: ",foreground=txtcol)
nfrtgrw.bind("<Button-1>", helpbiomsgrwth)
nfrtgrw.grid(row=3, column=1, sticky="w")
nfrtgrw_var = DoubleVar()
nfrtgrw_var.set(1.0)
nfrtgrw_n = Entry(master=vegpar_frame,textvariable=nfrtgrw_var, width=7)
nfrtgrw_n.config(state='disabled')
nfrtgrw_n.grid(row=3, column=2, sticky="w")

#Initial Growth
initgrw = Label(master=vegpar_frame,text="Initial Growth: ",foreground=txtcol)
initgrw.bind("<Button-1>", helpintlgrth)
initgrw.grid(row=4, column=1, sticky="w")
initgrw_var = DoubleVar()
initgrw_var.set(0.5)
initgrw_n = Entry(master=vegpar_frame,textvariable=initgrw_var, width=7)
initgrw_n.config(state='disabled')
initgrw_n.grid(row=4, column=2, sticky="w")

#Initial Stomatal Conductance
initstcd = Label(master=vegpar_frame,text="Stomatal Conductance: ",foreground=txtcol)
initstcd.bind("<Button-1>", helpstmtlcndtnce)
initstcd.grid(row=5, column=1, sticky="w")
initstcd_var = DoubleVar()
initstcd_var.set(1.0)
initstcd_n = Entry(master=vegpar_frame,textvariable=initstcd_var, width=7)
initstcd_n.config(state='disabled')
initstcd_n.grid(row=5, column=2, sticky="w")

#Initial Vegetative Surface Roughness
initrgh = Label(master=vegpar_frame,text="Vegetation Roughness: ",foreground=txtcol)
initrgh.bind("<Button-1>", helpvgtnrghns)
initrgh.grid(row=6, column=1, sticky="w")
initrgh_var = DoubleVar()
initrgh_var.set(2.0)
initrgh_n = Entry(master=vegpar_frame,textvariable=initrgh_var, width=7)
initrgh_n.config(state='disabled')
initrgh_n.grid(row=6, column=2, sticky="w")

#Initial Soil Carbon Content
initslc = Label(master=vegpar_frame,text="Soil Carbon Content: ",foreground=txtcol)
initslc.bind("<Button-1>", helpslcbncntnt)
initslc.grid(row=7, column=1, sticky="w")
initslc_var = DoubleVar()
initslc_var.set(0.0)
initslc_n = Entry(master=vegpar_frame,textvariable=initslc_var, width=7)
initslc_n.config(state='disabled')
initslc_n.grid(row=7, column=2, sticky="w")

#Initial Vegetative Carbon Content
initplc = Label(master=vegpar_frame,text="Plant Carbon Content: ",foreground=txtcol)
initplc.bind("<Button-1>", helplntcbncntnt)
initplc.grid(row=8, column=1, sticky="w")
initplc_var = DoubleVar()
initplc_var.set(0.0)
initplc_n = Entry(master=vegpar_frame,textvariable=initplc_var, width=7)
initplc_n.config(state='disabled')
initplc_n.grid(row=8, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_three_frame = Frame()
col_three_frame.grid(row=1,column=5,sticky="n")
col_three_frame.rowconfigure([2], minsize=10, weight=1)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Surface Parameter Frame
surfpar_frame = Frame(master=col_three_frame,relief=GROOVE,borderwidth=3)
surfpar_frame.grid(row=1,column=1,sticky="new")
surfpar_frame.rowconfigure([1,2,3,4,5,6,7,8,9,10,11,12], minsize=20)

surfparam = Label(master=surfpar_frame,text="Surface Parameters")
surfparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Wet Soil
wetso = Label(master=surfpar_frame,text="Wet Soil: ",foreground=txtcol)
wetso.bind("<Button-1>", helpwtsl)
wetso.grid(row=1, column=1, sticky="w")
wetso_var = StringVar()
wetso_var.set("False")
wetsoil = Checkbutton(master=surfpar_frame,variable=wetso_var, onvalue='True', offvalue='False')
wetsoil.grid(row=1, column=2, sticky="w")

#Soil Albedo
soilalb = Label(master=surfpar_frame,text="Soil Albedo: ",foreground=txtcol)
soilalb.bind("<Button-1>", helpslalbdo)
soilalb.grid(row=2, column=1, sticky="w")
soilalb_var = DoubleVar()
soilalb_n = Entry(master=surfpar_frame,textvariable=soilalb_var, width=7)
soilalb_n.config(state='disabled')
soilalb_n.grid(row=2, column=2, sticky="w")
##Soil Albedo Toggle
soilalbtog_var = StringVar()
soilalbtog_var.set('False')
soilalbtog_n = Checkbutton(master=surfpar_frame,variable=soilalbtog_var,command=soilalbtoggle, onvalue='True', offvalue='False')
soilalbtog_n.grid(row=2, column=3, sticky="w")

#Soil Depth
soildepth = Label(master=surfpar_frame,text="Soil Depth (m): ",foreground=txtcol)
soildepth.bind("<Button-1>", helpsldpth)
soildepth.grid(row=3, column=1, sticky="w")
soildepth_var = DoubleVar()
soildepth_var.set(12.4)
soildepth_n = Entry(master=surfpar_frame,textvariable=soildepth_var, width=7)
soildepth_n.config(state='disabled')
soildepth_n.grid(row=3, column=2, sticky="w")
##Soil Depth Toggle
soildepthtog_var = StringVar()
soildepthtog_var.set('False')
soildepthtog_n = Checkbutton(master=surfpar_frame,variable=soildepthtog_var,command=soildepthtoggle, onvalue='True', offvalue='False')
soildepthtog_n.grid(row=3, column=3, sticky="w")

#Soil Heat Capacity
capsoil = Label(master=surfpar_frame,text="Soil Heat Capacity: ",foreground=txtcol)
capsoil.bind("<Button-1>", helpslhtcpsty)
capsoil.grid(row=4, column=1, sticky="w")
capsoil_var = DoubleVar()
capsoil_var.set(2.4)
capsoil_n = Entry(master=surfpar_frame,textvariable=capsoil_var, width=7)
capsoil_n.config(state='disabled')
capsoil_n.grid(row=4, column=2, sticky="w")
##Soil Heact Capacity Toggle
capsoiltog_var = StringVar()
capsoiltog_var.set('False')
capsoiltog_n = Checkbutton(master=surfpar_frame,variable=capsoiltog_var,command=capsoiltoggle, onvalue='True', offvalue='False')
capsoiltog_n.grid(row=4, column=3, sticky="w")

#Soil Water Capacity
soilwcp = Label(master=surfpar_frame,text="Soil Water Capacity: ",foreground=txtcol)
soilwcp.bind("<Button-1>", helpslwtrcpsty)
soilwcp.grid(row=5, column=1, sticky="w")
soilwcp_var = DoubleVar()
soilwcp_var.set(0.5)
soilwcp_n = Entry(master=surfpar_frame,textvariable=soilwcp_var, width=7)
soilwcp_n.config(state='disabled')
soilwcp_n.grid(row=5, column=2, sticky="w")
##Soil Water Capacity Toggle
soilwcptog_var = StringVar()
soilwcptog_var.set('False')
soilwcptog_n = Checkbutton(master=surfpar_frame,variable=soilwcptog_var,command=soilwcptoggle, onvalue='True', offvalue='False')
soilwcptog_n.grid(row=5, column=3, sticky="w")

#Soil Saturation
soilsat = Label(master=surfpar_frame,text="Soil Saturation: ",foreground=txtcol)
soilsat.bind("<Button-1>", helpslstrtn)
soilsat.grid(row=6, column=1, sticky="w")
soilsat_var = DoubleVar()
soilsat_var.set(0.0)
soilsat_n = Entry(master=surfpar_frame,textvariable=soilsat_var, width=7)
soilsat_n.config(state='disabled')
soilsat_n.grid(row=6, column=2, sticky="w")
##Soil Water Capacity Toggle
soilsattog_var = StringVar()
soilsattog_var.set('False')
soilsattog_n = Checkbutton(master=surfpar_frame,variable=soilsattog_var,command=soilsattoggle, onvalue='True', offvalue='False')
soilsattog_n.grid(row=6, column=3, sticky="w")

#Snow Albedo
snowalb = Label(master=surfpar_frame,text="Snow Albedo: ",foreground=txtcol)
snowalb.bind("<Button-1>", helpsnwalb)
snowalb.grid(row=7, column=1, sticky="w")
snowalb_var = DoubleVar()
snowalb_n = Entry(master=surfpar_frame,textvariable=snowalb_var, width=7)
snowalb_n.config(state='disabled')
snowalb_n.grid(row=7, column=2, sticky="w")
##Snow Albedo Toggle
snowalbtog_var = StringVar()
snowalbtog_var.set('False')
snowalbtog_n = Checkbutton(master=surfpar_frame,variable=snowalbtog_var,command=snowalbtoggle, onvalue='True', offvalue='False')
snowalbtog_n.grid(row=7, column=3, sticky="w")

#Max Snow
mxsnow = Label(master=surfpar_frame,text="Max Snow (m): ",foreground=txtcol)
mxsnow.bind("<Button-1>", helpmxsnw)
mxsnow.grid(row=8, column=1, sticky="w")
mxsnow_var = DoubleVar()
mxsnow_var.set(5.0)
mxsnow_n = Entry(master=surfpar_frame,textvariable=mxsnow_var, width=7)
mxsnow_n.config(state='disabled')
mxsnow_n.grid(row=8, column=2, sticky="w")
##Snow Albedo Toggle
mxsnowtog_var = StringVar()
mxsnowtog_var.set('False')
mxsnowtog_n = Checkbutton(master=surfpar_frame,variable=mxsnowtog_var,command=mxsnowtoggle, onvalue='True', offvalue='False')
mxsnowtog_n.grid(row=8, column=3, sticky="w")

#Sea Ice
seaice = Label(master=surfpar_frame,text="Sea Ice: ",foreground=txtcol)
seaice.bind("<Button-1>", helpseaice)
seaice.grid(row=9, column=1, sticky="w")
seaice_var = StringVar()
seaice_var.set('True')
seaice_n = Checkbutton(master=surfpar_frame,variable=seaice_var, onvalue='True', offvalue='False')
seaice_n.grid(row=9, column=2, sticky="w")

#Ocean Albedo
oceanalb = Label(master=surfpar_frame,text="Ocean Albedo: ",foreground=txtcol)
oceanalb.bind("<Button-1>", helpocnalb)
oceanalb.grid(row=10, column=1, sticky="w")
oceanalb_var = DoubleVar()
oceanalb_n = Entry(master=surfpar_frame,textvariable=snowalb_var, width=7)
oceanalb_n.config(state='disabled')
oceanalb_n.grid(row=10, column=2, sticky="w")
##Snow Albedo Toggle
oceanalbtog_var = StringVar()
oceanalbtog_var.set('False')
oceanalbtog_n = Checkbutton(master=surfpar_frame,variable=oceanalbtog_var,command=oceanalbtoggle, onvalue='True', offvalue='False')
oceanalbtog_n.grid(row=10, column=3, sticky="w")

#Mixed Ocean Depth
mldepth = Label(master=surfpar_frame,text="Mixed Layer Depth (m): ",foreground=txtcol)
mldepth.bind("<Button-1>", helpmxdlyrdpth)
mldepth.grid(row=11, column=1, sticky="w")
mldepth_var = DoubleVar()
mldepth_var.set(50.0)
mldepth_n = Entry(master=surfpar_frame,textvariable=mldepth_var, width=7)
mldepth_n.config(state='disabled')
mldepth_n.grid(row=11, column=2, sticky="w")
##Mixed Ocean Depth Toggle
mldepthtog_var = StringVar()
mldepthtog_var.set('False')
mldepthtog_n = Checkbutton(master=surfpar_frame,variable=mldepthtog_var,command=mldepthtoggle, onvalue='True', offvalue='False')
mldepthtog_n.grid(row=11, column=3, sticky="w")

#Ocean Zenith
oceanzen = Label(master=surfpar_frame,text="Ocean Zenith: ",foreground=txtcol)
oceanzen.bind("<Button-1>", helpocnznth)
oceanzen.grid(row=12, column=1, sticky="w")
oceanzen_options = ["ECHAM-3", "Lambertian", "uniform", "ECHAM-3", "plasim", "default", "ECHAM-6"]
oceanzen_var = StringVar()
oceanzen_var.set(oceanzen_options[0])
oceanzen_n = OptionMenu(surfpar_frame, oceanzen_var, *oceanzen_options)
oceanzen_n.config(width=7)
oceanzen_n.grid(row=12,column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Geographic Parameter Frame
geopar_frame = Frame(master=col_three_frame,relief=GROOVE,borderwidth=3)
geopar_frame.grid(row=3,column=1,sticky="new")
geopar_frame.rowconfigure([1,2,3,4,5,6,7,8,9], minsize=20)

geoparam = Label(master=geopar_frame,text="Geographic Parameters")
geoparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Image/SRA Toggle
imgsratog = Label(master=geopar_frame,text="Image/SRA Toggle: ",foreground=txtcol)
imgsratog.bind("<Button-1>", helpimgsratog)
imgsratog.grid(row=1, column=1, sticky="w")
imgsratogtog_var = StringVar()
imgsratogtog_var.set('False')
imgsratogtog_n = Checkbutton(master=geopar_frame,variable=imgsratogtog_var,command=imgsratoggle, onvalue='True', offvalue='False')
imgsratogtog_n.grid(row=1, column=2, sticky="w")

#Height Map Image
hghtmpimg = Label(master=geopar_frame,text="Height Map Image: ",foreground=txtcol)
hghtmpimg.bind("<Button-1>", helphghtmpimg)
hghtmpimg.grid(row=2, column=1, sticky="w")
hghtmpimg_var = StringVar()
hghtmpimg_n = Entry(master=geopar_frame,textvariable=hghtmpimg_var, width=7)
hghtmpimg_n.config(state='enabled')
hghtmpimg_n.grid(row=2, column=2, sticky="w")
hghtmpimg_b = Button(master=geopar_frame,text="Open",command=hghtimgget, width=7)
hghtmpimg_b.config(state='enabled')
hghtmpimg_b.grid(row=2, column=3, sticky="w")

#Water Threshold
waterhres = Label(master=geopar_frame,text="Water Threshold: ",foreground=txtcol)
waterhres.bind("<Button-1>", helpwtrthrshld)
waterhres.grid(row=3, column=1, sticky="w")
waterhres_var = IntVar()
waterhres_var.set(0)
waterhres_n = Entry(master=geopar_frame,textvariable=waterhres_var, width=7)
waterhres_n.config(state='enabled')
waterhres_n.grid(row=3, column=2, sticky="w")

#Highest Elevation
highelev = Label(master=geopar_frame,text="Highest Elevation (m): ",foreground=txtcol)
highelev.bind("<Button-1>", helphghstelvtn)
highelev.grid(row=4, column=1, sticky="w")
highelev_var = DoubleVar()
highelev_var.set(8849.0)
highelev_n = Entry(master=geopar_frame,textvariable=highelev_var, width=7)
highelev_n.config(state='enabled')
highelev_n.grid(row=4, column=2, sticky="w")

#Lowest Elevation
lowelev = Label(master=geopar_frame,text="Lowest Elevation (m): ",foreground=txtcol)
lowelev.bind("<Button-1>", helplwstelvtn)
lowelev.grid(row=5, column=1, sticky="w")
lowelev_var = DoubleVar()
lowelev_var.set(-11034.0)
lowelev_n = Entry(master=geopar_frame,textvariable=lowelev_var, width=7)
lowelev_n.config(state='disabled')
lowelev_n.grid(row=5, column=2, sticky="w")

#Image Debug
imgdebug = Label(master=geopar_frame,text="Image Debug: ",foreground=txtcol)
imgdebug.bind("<Button-1>", helpimgdbg)
imgdebug.grid(row=6, column=1, sticky="w")
imgdebugtog_var = StringVar()
imgdebugtog_var.set('False')
imgdebugtog_n = Checkbutton(master=geopar_frame,variable=imgdebugtog_var, onvalue='True', offvalue='False')
imgdebugtog_n.config(state='enabled')
imgdebugtog_n.grid(row=6, column=2, sticky="w")

#SRA Name
sranme = Label(master=geopar_frame,text="SRA Name: ",foreground=txtcol)
sranme.bind("<Button-1>", helpsranme)
sranme.grid(row=7, column=1, sticky="w")
sranme_var = StringVar()
sranme_var.set("earth")
sranme_n = Entry(master=geopar_frame,textvariable=sranme_var, width=7)
sranme_n.config(state='enabled')
sranme_n.grid(row=7, column=2, sticky="w")

#Land SRA
lndsra = Label(master=geopar_frame,text="Land SRA: ",foreground=txtcol)
lndsra.bind("<Button-1>", helplndsra)
lndsra.grid(row=8, column=1, sticky="w")
lndsra_var = StringVar()
lndsra_n = Entry(master=geopar_frame,textvariable=lndsra_var, width=7)
lndsra_n.config(state='disabled')
lndsra_n.grid(row=8, column=2, sticky="w")
lndsra_b = Button(master=geopar_frame,text="Open",command=landsraget, width=7)
lndsra_b.config(state='disabled')
lndsra_b.grid(row=8, column=3, sticky="w")

#Topo SRA
tposra = Label(master=geopar_frame,text="Topographic SRA: ",foreground=txtcol)
tposra.bind("<Button-1>", helptposra)
tposra.grid(row=9, column=1, sticky="w")
tposra_var = StringVar()
tposra_n = Entry(master=geopar_frame,textvariable=tposra_var, width=7)
tposra_n.config(state='disabled')
tposra_n.grid(row=9, column=2, sticky="w")
tposra_b = Button(master=geopar_frame,text="Open",command=toposraget, width=7)
tposra_b.config(state='disabled')
tposra_b.grid(row=9, column=3, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_four_frame = Frame()
col_four_frame.grid(row=1,column=7,sticky="n")
col_four_frame.rowconfigure([2,4], minsize=10, weight=1)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Atmospheric Parameter Frame
atmpar_frame = Frame(master=col_four_frame,relief=GROOVE,borderwidth=3)
atmpar_frame.grid(row=1,column=1,sticky="new")
atmpar_frame.rowconfigure([1,2,3,4,5,6,7,8,9,10,11,12,13,14], minsize=20)

atmparam = Label(master=atmpar_frame,text="Atmospheric Parameters")
atmparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Pressure
pressure = Label(master=atmpar_frame,text="Pressure (bar): ",foreground=txtcol)
pressure.bind("<Button-1>", helprsure)
pressure.grid(row=1, column=1, sticky="w")
pressure_var = DoubleVar()
pressure_var.set(1.0)
pressure_n = Entry(master=atmpar_frame,textvariable=pressure_var, width=7)
pressure_n.config(state='disabled')
pressure_n.grid(row=1, column=2, sticky="w")
##Pressure Toggle
pressuretog_var = StringVar()
pressuretog_var.set('False')
pressuretog_n = Checkbutton(master=atmpar_frame,variable=pressuretog_var,command=pressuretoggle, onvalue='True', offvalue='False')
pressuretog_n.grid(row=1, column=3, sticky="w")

#Gas Constant
gascon = Label(master=atmpar_frame,text="Gas Constant: ",foreground=txtcol)
gascon.bind("<Button-1>", helpgscnstnt)
gascon.grid(row=2, column=1, sticky="w")
gascon_var = DoubleVar()
gascon_var.set(287.0)
gascon_n = Entry(master=atmpar_frame,textvariable=gascon_var, width=7)
gascon_n.config(state='disabled')
gascon_n.grid(row=2, column=2, sticky="w")
##Gas Constant Toggle
gascontog_var = StringVar()
gascontog_var.set('False')
gascontog_n = Checkbutton(master=atmpar_frame,variable=gascontog_var,command=gascontoggle, onvalue='True', offvalue='False')
gascontog_n.grid(row=2, column=3, sticky="w")

#Dry Core
drycore = Label(master=atmpar_frame,text="Dry Core: ",foreground=txtcol)
drycore.bind("<Button-1>", helpdrycre)
drycore.grid(row=3, column=1, sticky="w")
drycoretog_var = StringVar()
drycoretog_var.set('False')
drycoretog_n = Checkbutton(master=atmpar_frame,variable=drycoretog_var, onvalue='True', offvalue='False')
drycoretog_n.grid(row=3, column=2, sticky="w")

#Ozone
ozone = Label(master=atmpar_frame,text="Ozone: ",foreground=txtcol)
ozone.bind("<Button-1>", helpozne)
ozone.grid(row=4, column=1, sticky="w")
ozone_var = StringVar()
ozone_var.set('False')
ozone_n = Checkbutton(master=atmpar_frame,variable=ozone_var, onvalue='True', offvalue='False')
ozone_n.grid(row=4, column=2, sticky="w")

#Partial Pressure
partialp = Label(master=atmpar_frame,text="Gas Pressure (bar): ",foreground=txtcol)
partialp.bind("<Button-1>", helpgsprsurs)
partialp.grid(row=5, column=1, sticky="w")
partialptog_var = StringVar()
partialptog_var.set('False')
partialptog_n = Checkbutton(master=atmpar_frame,variable=partialptog_var,command=ptoggle, onvalue='True', offvalue='False')
partialptog_n.grid(row=5, column=2, sticky="w")

#pH2
pH2 = Label(master=atmpar_frame,text="H2: ")
pH2.grid(row=6, column=1, sticky="w")
pH2_var = DoubleVar()
pH2_var.set(0.0)
pH2_n = Entry(master=atmpar_frame,textvariable=pH2_var, width=7)
pH2_n.config(state='disabled')
pH2_n.grid(row=6, column=2, sticky="w")

#pHe
pHe = Label(master=atmpar_frame,text="He: ")
pHe.grid(row=7, column=1, sticky="w")
pHe_var = DoubleVar()
pHe_var.set(0.0)
pHe_n = Entry(master=atmpar_frame,textvariable=pHe_var, width=7)
pHe_n.config(state='disabled')
pHe_n.grid(row=7, column=2, sticky="w")

#pN2
pN2 = Label(master=atmpar_frame,text="N2: ")
pN2.grid(row=8, column=1, sticky="w")
pN2_var = DoubleVar()
pN2_var.set(0.7809)
pN2_n = Entry(master=atmpar_frame,textvariable=pN2_var, width=7)
pN2_n.config(state='disabled')
pN2_n.grid(row=8, column=2, sticky="w")

#pO2
pO2 = Label(master=atmpar_frame,text="O2: ")
pO2.grid(row=9, column=1, sticky="w")
pO2_var = DoubleVar()
pO2_var.set(0.2095)
pO2_n = Entry(master=atmpar_frame,textvariable=pO2_var, width=7)
pO2_n.config(state='disabled')
pO2_n.grid(row=9, column=2, sticky="w")

#pAr
pAr = Label(master=atmpar_frame,text="Ar: ")
pAr.grid(row=10, column=1, sticky="w")
pAr_var = DoubleVar()
pAr_var.set(0.0093)
pAr_n = Entry(master=atmpar_frame,textvariable=pAr_var, width=7)
pAr_n.config(state='disabled')
pAr_n.grid(row=10, column=2, sticky="w")

#pNe
pNe = Label(master=atmpar_frame,text="Ne: ")
pNe.grid(row=11, column=1, sticky="w")
pNe_var = DoubleVar()
pNe_var.set(0.0)
pNe_n = Entry(master=atmpar_frame,textvariable=pNe_var, width=7)
pNe_n.config(state='disabled')
pNe_n.grid(row=11, column=2, sticky="w")

#pKr
pKr = Label(master=atmpar_frame,text="Kr: ")
pKr.grid(row=12, column=1, sticky="w")
pKr_var = DoubleVar()
pKr_var.set(0.0)
pKr_n = Entry(master=atmpar_frame,textvariable=pKr_var, width=7)
pKr_n.config(state='disabled')
pKr_n.grid(row=12, column=2, sticky="w")

#pH2O
pH2O = Label(master=atmpar_frame,text="H2O: ")
pH2O.grid(row=13, column=1, sticky="w")
pH2O_var = DoubleVar()
pH2O_var.set(0.0)
pH2O_n = Entry(master=atmpar_frame,textvariable=pH2O_var, width=7)
pH2O_n.config(state='disabled')
pH2O_n.grid(row=13, column=2, sticky="w")

#pCO2
pCO2 = Label(master=atmpar_frame,text="CO2: ")
pCO2.grid(row=14, column=1, sticky="w")
pCO2_var = DoubleVar()
pCO2_var.set(0.0003)
pCO2_n = Entry(master=atmpar_frame,textvariable=pCO2_var, width=7)
pCO2_n.config(state='disabled')
pCO2_n.grid(row=14, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Glacial Parameter Frame
glacpar_frame = Frame(master=col_four_frame,relief=GROOVE,borderwidth=3)
glacpar_frame.grid(row=3,column=1,sticky="new")
glacpar_frame.rowconfigure([1,2,3], minsize=20)
glacpar_frame.columnconfigure([2], minsize=80)

glacparam = Label(master=glacpar_frame,text="Glacial Parameters")
glacparam.grid(row=0,column=1,columnspan=3, sticky="n")

#Glacier Toggle
glacial = Label(master=glacpar_frame,text="Glaciers: ",foreground=txtcol)
glacial.bind("<Button-1>", helpglcrs)
glacial.grid(row=1, column=1, sticky="w")
glacialtog_var = StringVar()
glacialtog_var.set('False')
glacialtog_n = Checkbutton(master=glacpar_frame,variable=glacialtog_var,command=gtoggle, onvalue='True', offvalue='False')
glacialtog_n.grid(row=1, column=2, sticky="w")

#Initial Height
inith = Label(master=glacpar_frame,text="Height (m): ",foreground=txtcol)
inith.bind("<Button-1>", helpgrhght)
inith.grid(row=2, column=1, sticky="w")
inith_var = DoubleVar()
inith_var.set(0.0)
inith_n = Entry(master=glacpar_frame,textvariable=inith_var,width=7)
inith_n.config(state='disabled')
inith_n.grid(row=2, column=2, sticky="w")

#Minimum Snow Depth
mndph = Label(master=glacpar_frame,text="Threshold (m): ",foreground=txtcol)
mndph.bind("<Button-1>", helpgrthrshld)
mndph.grid(row=3, column=1, sticky="w")
mndph_var = DoubleVar()
mndph_var.set(2.0)
mndph_n = Entry(master=glacpar_frame,textvariable=mndph_var,width=7)
mndph_n.config(state='disabled')
mndph_n.grid(row=3, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_five_frame = Frame()
col_five_frame.grid(row=1,column=9,sticky="new")
col_five_frame.rowconfigure([1,2], minsize=10, weight=1)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Model Dynamic Parameters
mdldynpar_frame = Frame(master=col_five_frame,relief=GROOVE,borderwidth=3)
mdldynpar_frame.grid(row=1,column=1,sticky="new")
mdldynpar_frame.rowconfigure([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], minsize=20)

mdldynparam = Label(master=mdldynpar_frame,text="Model Dynamic Parameters")
mdldynparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Timestep
tmestp = Label(master=mdldynpar_frame,text="Timestep (min): ",foreground=txtcol)
tmestp.bind("<Button-1>", helptimestep)
tmestp.grid(row=1, column=1, sticky="w")
tmestp_var = DoubleVar()
tmestp_var.set(45.0)
tmestp_n = Entry(master=mdldynpar_frame,textvariable=tmestp_var, width=7)
tmestp_n.grid(row=1, column=2, sticky="w")

#Runsteps
runstp = Label(master=mdldynpar_frame,text="Runsteps: ",foreground=txtcol)
runstp.bind("<Button-1>", helprunsteps)
runstp.grid(row=2, column=1, sticky="w")
runstp_var = IntVar()
runstp_var.set(11520)
runstp_n = Entry(master=mdldynpar_frame,textvariable=runstp_var, width=7)
runstp_n.grid(row=2, column=2, sticky="w")

#Snapshots
snpsht = Label(master=mdldynpar_frame,text="Snapshots: ",foreground=txtcol)
snpsht.bind("<Button-1>", helpsnapshots)
snpsht.grid(row=3, column=1, sticky="w")
snpsht_var = IntVar()
snpsht_var.set(0)
snpsht_n = Entry(master=mdldynpar_frame,textvariable=snpsht_var, width=7)
snpsht_n.grid(row=3, column=2, sticky="w")

#NSTPW
nsptw = Label(master=mdldynpar_frame,text="NSTPW: ",foreground=txtcol)
nsptw.bind("<Button-1>", helpnstpw)
nsptw.grid(row=4, column=1, sticky="w")
nsptw_var = IntVar()
nsptw_var.set(160)
nsptw_n = Entry(master=mdldynpar_frame,textvariable=nsptw_var, width=7)
nsptw_n.grid(row=4, column=2, sticky="w")

#Physics Filter 1
phyfilt1 = Label(master=mdldynpar_frame,text="Physics Filter: ",foreground=txtcol)
phyfilt1.bind("<Button-1>", helphysfltr)
phyfilt1.grid(row=5, column=1, sticky="w")
phyfilt1_options = ["None", "None", "Cesaro", "Exp", "Lh"]
phyfilt1_var = StringVar()
phyfilt1_var.set(oceanzen_options[0])
phyfilt1_n = OptionMenu(mdldynpar_frame, phyfilt1_var, *phyfilt1_options)
phyfilt1_n.config(width=7)
phyfilt1_n.grid(row=5,column=2, sticky="w")

#Physics Filter 2
phyfilt2 = Label(master=mdldynpar_frame,text="Filter Application: ",foreground=txtcol)
phyfilt2.bind("<Button-1>", helpfltrapp)
phyfilt2.grid(row=6, column=1, sticky="w")
phyfilt2_options = ["None", "None", "GP", "SP", "GP + SP"]
phyfilt2_var = StringVar()
phyfilt2_var.set(oceanzen_options[0])
phyfilt2_n = OptionMenu(mdldynpar_frame, phyfilt2_var, *phyfilt2_options)
phyfilt2_n.config(width=7)
phyfilt2_n.grid(row=6,column=2, sticky="w")

#Storm Climatology
stormcl = Label(master=mdldynpar_frame,text="Storm Climatology: ",foreground=txtcol)
stormcl.bind("<Button-1>", helpstmclmtlgy)
stormcl.grid(row=7, column=1, sticky="w")
stormcltog_var = StringVar()
stormcltog_var.set('False')
stormcltog_n = Checkbutton(master=mdldynpar_frame,variable=stormcltog_var,command=stmtoggle, onvalue='True', offvalue='False')
stormcltog_n.grid(row=7, column=2, sticky="w")

#High Cadence
highcad = Label(master=mdldynpar_frame,text="High Cadence: ",foreground=txtcol)
highcad.bind("<Button-1>", helphghcdnce)
highcad.grid(row=8, column=1, sticky="w")
highcadtog_var = StringVar()
highcadtog_var.set('False')
highcadtog_n = Checkbutton(master=mdldynpar_frame,variable=highcadtog_var, onvalue='True', offvalue='False')
highcadtog_n.config(state='disabled')
highcadtog_n.grid(row=8, column=2, sticky="w")

#Run To Balance
rntbal = Label(master=mdldynpar_frame,text="Run To Balance: ",foreground=txtcol)
rntbal.bind("<Button-1>", helprntbal)
rntbal.grid(row=9, column=1, sticky="w")
rntbaltog_var = StringVar()
rntbaltog_var.set('False')
rntbaltog_n = Checkbutton(master=mdldynpar_frame,variable=rntbaltog_var,command=baltoggle, onvalue='True', offvalue='False')
rntbaltog_n.grid(row=9, column=2, sticky="w")

#Run Time
runtme = Label(master=mdldynpar_frame,text="Run Time (years): ",foreground=txtcol)
runtme.bind("<Button-1>", helprntme)
runtme.grid(row=10, column=1, sticky="w")
runtme_var = IntVar()
runtme_var.set(100)
runtme_n = Entry(master=mdldynpar_frame,textvariable=runtme_var, width=7)
runtme_n.grid(row=10, column=2, sticky="w")

#Threshold
trshld = Label(master=mdldynpar_frame,text="Threshold: ",foreground=txtcol)
trshld.bind("<Button-1>", helpthrshld)
trshld.grid(row=11, column=1, sticky="w")
trshld_var = DoubleVar()
trshld_var.set(0.0005)
trshld_n = Entry(master=mdldynpar_frame,textvariable=trshld_var, width=7)
trshld_n.config(state='disabled')
trshld_n.grid(row=11, column=2, sticky="w")

#Baseline
bselne = Label(master=mdldynpar_frame,text="Baseline (years): ",foreground=txtcol)
bselne.bind("<Button-1>", helpbslne)
bselne.grid(row=12, column=1, sticky="w")
bselne_var = IntVar()
bselne_var.set(10)
bselne_n = Entry(master=mdldynpar_frame,textvariable=bselne_var, width=7)
bselne_n.config(state='disabled')
bselne_n.grid(row=12, column=2, sticky="w")

#Max Years
maxyr = Label(master=mdldynpar_frame,text="Max. Year (years): ",foreground=txtcol)
maxyr.bind("<Button-1>", helpmxyr)
maxyr.grid(row=13, column=1, sticky="w")
maxyr_var = IntVar()
maxyr_var.set(100)
maxyr_n = Entry(master=mdldynpar_frame,textvariable=maxyr_var, width=7)
maxyr_n.config(state='disabled')
maxyr_n.grid(row=13, column=2, sticky="w")

#Min Years
minyr = Label(master=mdldynpar_frame,text="Min. Year (years): ",foreground=txtcol)
minyr.bind("<Button-1>", helpmnyr)
minyr.grid(row=14, column=1, sticky="w")
minyr_var = IntVar()
minyr_var.set(10)
minyr_n = Entry(master=mdldynpar_frame,textvariable=minyr_var, width=7)
minyr_n.config(state='disabled')
minyr_n.grid(row=14, column=2, sticky="w")

#Crash If Broken
cshibrk = Label(master=mdldynpar_frame,text="Crash if Broken: ",foreground=txtcol)
cshibrk.bind("<Button-1>", helpcrshibrkn)
cshibrk.grid(row=15, column=1, sticky="w")
cshibrktog_var = StringVar()
cshibrktog_var.set('False')
cshibrktog_n = Checkbutton(master=mdldynpar_frame,variable=cshibrktog_var, onvalue='True', offvalue='False')
cshibrktog_n.grid(row=15, column=2, sticky="w")

#Clean
clean = Label(master=mdldynpar_frame,text="Clean: ",foreground=txtcol)
clean.bind("<Button-1>", helpcln)
clean.grid(row=16, column=1, sticky="w")
cleantog_var = StringVar()
cleantog_var.set('False')
cleantog_n = Checkbutton(master=mdldynpar_frame,variable=cleantog_var, onvalue='True', offvalue='False')
cleantog_n.grid(row=16, column=2, sticky="w")

#All Years
allyrs = Label(master=mdldynpar_frame,text="All Years: ",foreground=txtcol)
allyrs.bind("<Button-1>", helpalrstrts)
allyrs.grid(row=17, column=1, sticky="w")
allyrstog_var = StringVar()
allyrstog_var.set('False')
allyrstog_n = Checkbutton(master=mdldynpar_frame,variable=allyrstog_var, onvalue='True', offvalue='False')
allyrstog_n.grid(row=17, column=2, sticky="w")

#Keep Restarts
kprsts = Label(master=mdldynpar_frame,text="Keep Restarts: ",foreground=txtcol)
kprsts.bind("<Button-1>", helpkprstrts)
kprsts.grid(row=18, column=1, sticky="w")
kprststog_var = StringVar()
kprststog_var.set('False')
kprststog_n = Checkbutton(master=mdldynpar_frame,variable=kprststog_var, onvalue='True', offvalue='False')
kprststog_n.grid(row=18, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#Check
compat = Label(text="Compatability")
compat.grid(row=3, column=7, sticky="n")
sys_check = Button(text="Compatability Check", command=system_check)
sys_check.grid(row=4, column=7, sticky="n")

#Save
output = Label(text="Output")
output.grid(row=3, column=9, sticky="n")
save = Button(text="Save", command=save_file)
save.grid(row=4, column=9, sticky="n")

window.mainloop()