import os
import tkinter

HELP_DICT = {
    

    "helpjctnme" :
    """Help: Project Name
    The name of your project, this is not the same as the name for the output file/folder""",

    "helpstrtyr" :
    """Help: Start Year
    1 by ault; What number year the project should start at (eg. '2000' will have the model start at 2000).
    This is arbitrary, however must be positive.""",

    "helpotptype" :
    """Help: Output Type
    .nc by ault; File extension to use for the output, if using the pyburn postprocessor.
    If using any of .hdf5, .he5, or .h5, then h5py must be installed.""",

    "helpcpucnt" :
    """Help: CPU Count
    4 by ault; Number of CPUs for ExoPlaSim to use.""",

    "helpresision" :
    """Help: Precision
    8 by ault; Precision (in bytes) of some internal numbers used, either 4 or 8.
    4 will run a tad faster, but may be less stable and more prone to crashing.""",

    "helpresolution" :
    """Help: Resolution
    T21 by ault; Sets the resolution used for modelling the planet’s surface,
    thus the resolution of the geography one can import into the model and the output one will get.

    "These are the resolutions ExoPlaSim can handle, and the associated codes to input here : Code|Height|Width
    T21|  32  |  64
    T42|  64  | 128
    T63|  96  | 192
    T85| 128  | 256
    T106| 160  | 320
    T127| 192  | 384
    T170| 256  | 512""",

    "helpcrshtlrnt" :
    """Help: Crash Tolorant
    False by ault; If set to True, then if the model crashes (and at least 10 years have been simulated),it will rewind 10 years and try again.
    This can help get around some crashes caused by essentially just random noise in the model, without requiring manually restarting it each time.

    On the other hand, if there’s some more fundamental issue with the model
    (e.g., it’s warming to the point that the oceans start boiling away) then this feature could cause it to be trapped in an infinite loop; 
    So it’s probably best to leave it off if you’re “exploring” new configurations, and to check up on the model when you do turn it on.""",

    "helplayers" :
    """Help: Layers
    10 by ault; Number of atmospheric layers modeled—in essence, the vertical resolution of the model grid.
    Low-resolution models seem to work fine with 5, which saves a good deal of computing time.
    Higher-resolution models may require more layers for best accuracy, but would further extend the runtime.""",

    "helprecompile" :
    """Help: Recompile
    False by ault; If set to True, forces exoplasim to compile again before running.
    May be useful if you’ve altered some of the source files.""",

    ####Stellar Parameters

    "helpstrtmp" :
    """Help: Star Temperature
    5772.0 by ault; The effective temperature of the star in Kelvin, will be used to adjust atmospheric absorption and surface albedo.
    It does not affect flux or year length, and if not set, a sunlike star will be assumed.""",

    "helpstlrflx" :
    """Help: Stellar Flux
    1367.0 by ault; The flux of sunlight hitting the top of the planet’s atmosphere, in watts/meter^2.
    Value represents Earth's Stellar Flux.""",

    ####Orbital Parameters

    "helpyrlngth" :
    """Help: Year Length
    365.25 by ault; Length of the year, in 24-hour Earth days.
    This controls the period the planet takes to orbit its star, not the length of the years used for the output files and the model run controls;
    Those are set by the runsteps parameter, though generally speaking they should probably be the same, except for very short orbital periods.

    To properly produce Koppen maps from the output files, this should be the same length of time as the model year.
    year * 1440 = runsteps * timestep""",

    "helpdaylngth" :
    """Help: Day Length
    1.0 by ault; Rotation period of the planet, compared to Earth.
    This is a sidereal day (23 hours 56 minutes for Earth).
    For planets with many orbits per year it should be an insignificant difference from a solar day.

    Ideally there should be a whole number of timesteps in a solar day, and a whole number of solar days in a month.
    (rotationperiod * 1440) / timestep = an integer
    runsteps / times = (rotationperiod * 1440 / timestep) * an integer""",

    "helpeccentr" :
    """Help: Eccentricity
    0.016715 by ault; Eccentricity of the planet’s orbit.""",

    "helpoblqty" :
    """Help: Obliquity
    23.441 by ault; Obliquity, A.K.A. axial tilt, in degrees.""",

    "helplngpri" :
    """Help: Longitude of Periapsis
    102.7 by ault; Longitude (angle along the orbit) of periapsis (point when the planet is closest to the star) in degrees.
    Measured from the autumnal equinox, which is used to orient the planet’s rotational axis relative to its orbit.""",

    "helpfxdobt" :
    """Help: Fixed Orbit
    True by ault; True forces the orbit to remain unchanged throughout the simulation.
    False allows for ExoPlaSim to calculate Milankovitch cycles to alter the planet’s orbit and orientation.

    The latter feature is still under development, so it’s probably best to keep this on for now.""",

    ####Rotational Parameters

    "helptdlkd" :
    """Help: Tidally Locked
    False by Default; True locks the sun to one longitude.""",

    "helpsbstlrlng" :
    """Help: Substellar Longitude
    180 by Default; Longitude of the substellar point, in degrees.
    If importing geography with 0 longitude at the center, the geography will be offset 180 degrees from the model’s coordinate system.
    The ault of 180 would places the substellar point at 0 longitude.""",

    "helpsbstlrdsync" :
    """Help: Substellar Desync
    0.0 by Default; Rate at which the substellar point drifts from its initial longitude, in degrees per minute.
    One could use this to approximate spin-orbit resonances other than 1:1
    (eg. drift of 180 degrees per orbit would approximate the 3:2 resonance)

    But the effects of eccentricity on the movement of the substellar point are not properly modelled in the current version of ExoPlaSim.
    Can be positive or negative.""",

    "helptmpcntrst" :
    """Help: Temperature Contrast
    0.0 by Default; Adds an initial temperature contrast between the substellar point and the antistellar point, in Kelvin.
    Increasing it to, 100 may help the model balance faster.""",

    ####Planet Parameters

    "helpgrvty" :
    """Help: Gravity
    9.80665 by Default; Acceleration due to gravity at the planet’s surface, in meters/second^2.""",

    "helprdus" :
    """Help: Radius
    1.0 by Default; Radius of the planet relative to Earth.""",

    "helporgrphy" :
    """Help: Orography
    1.0 by Default; Scaling factor applied to the above-ined topography, down to flat continents at 0.0.
    Extreme conditions on high mountain peaks or deep valley floors can sometimes cause crashes, so flattening out the topography can help tell if that’s the issue.""",

    "helpaquaplnt" :
    """Help: Aqua Planet
    False by Default; True erases land surfaces (including the ault earth geography) and gives a uniform, all-ocean planet.
    May run a bit faster, so it can be useful for debugging or quick tests of other factors.""",

    "helpdsrtplnt" :
    """Help: Desert Planet
    False by Default; True erases all seas and gives a fully land-covered planet.""",

    ####Vegetation Parameters

    "helpvgtn" :
    """Help: Vegetation
    None by Default; Controls a vegetation model, which will impact surface albedo and humidity.
    Not a very advanced model and probably won’t handle particularly exotic climates too well, but it’s still nice to have.

    None will leave the model off
    \"Diagnostic\" vegetation is fixed to an initial value of vegetation cover across all land
    \"Dynamic\" will activate a vegetation model that will grow and die back in response to the local climate, producing an estimate of the resulting forest cover in the output.
    This will probably slow down the model to some extent, so one might want to leave it off until putting together a final model.""",

    "helpvgaclrtn" :
    """Help: Vegetation Acceleration
    1 by Default; Accelerates the rate of vegetation growth.""",

    "helpbiomsgrwth" :
    """Help: Biomass Growth
    1.0 by Default; Amount of biomass produced by vegetation in tonnes/hectare/year.""",

    "helpintlgrth" :
    """Help: Initial Growth
    0.5 by Default; Adds vegetation cover to all land at the start of the model.
    Might save some time running the model to equilibrium and make the resulting climate somewhat less arid than it would be if it started without vegetation.
    Should be between 0 and 1.""",

    "helpstmtlcndtnce" :
    """Help: Initial Stomatal Conductance
    1.0 by Default; Rate at which CO2 enters or water vapour exits through the stomata of leaves at the start of the simulation.""",

    "helpvgtnrghns" :
    """Help: Initial Vegetation Roughness
    2.0 by Default; Determines how much vegetation slows down wind speeds at the start of the simulation.""",

    "helpslcbncntnt" :
    """Help: Initial Soil Carbon Content
    0.0 by Default; How much carbon is stored within soil at the start of the simulation.""",

    "helplntcbncntnt" :
    """Help: Initial Plant Carbon Content
    0.0 by Default; How much carbon is stored within plants at the start of the simulation.""",

    ####Surface Parameters

    "helpwtsl" :
    """Help: Wet Soil
    False by Default; True alters the albedo of land surfaces based on how wet they are; wetter land has a lower albedo, so it reflects less light.""",

    "helpslalbdo" :
    """Help: Soil Albedo
    Disabled by Default; Can be set to a fixed albedo value that will be used for all land.
    Usually shouldn’t do this for Earthlike planets, could use it to model some sort of unusual desert planet covered in more reflective desert sand or salt.""",

    "helpsldpth" :
    """Help: Soil Depth
    Disabled by Default; Scaling factor for the depth of soil layers in meters.""",

    "helpslhtcpsty" :
    """Help: Soil Heat Capacity
    Disabled by Default; Heat capacity of the soil, in (10^6)J/m^3/K""",

    "helpslwtrcpsty" :
    """Help: Soil Water Capacity
    Disabled by Default; Water capacity of the soil, in meters.""",

    "helpslstrtn" :
    """Help: Initial Soil Saturation
    Disabled by Default; Initial fractional saturation of the soil.""",

    "helpsnwalb" :
    """Help: Snow/Ice Albedo
    Disabled by Default; Can be set to a fixed albedo value that will be used for all snow and ice.""",

    "helpmxsnw" :
    """Help: Max Snow
    Disabled by Default; Maximum snow depth in meters. Set to -1 to have no limit.""",

    "helpseaice" :
    """Help: Sea Ice
    True by Default; If False, disables radiative effects of sea ice (although sea ice itself is still computed).""",

    "helpocnalb" :
    """Help: Ocean Albedo
    Disabled by Default; Can be set to a fixed albedo value that will be used for all oceans.""",

    "helpmxdlyrdpth" :
    """Help: Mixed Layer Depth
    50.0 by Default; Depth of the mixed-layer ocean in meters.""",

    "helpocnznth" :
    """Help: Ocean Zenith
    ECHAM-3 by Default; The zenith-angle dependence to use for blue-light reflectance from the ocean.""",

    ####Geographic Parameters

    "helpimgsratog" :
    """Help: Image/SRA Toggle
    False by Default; Determines whether to produce SRA files through images (False) or use existing SRA files (True).""",

    "helphghtmpimg" :
    """Help: Height Map Image
    N/A by Default; Path to a (ideally) black and white .png image, with black as lowest elevation and white as highest.
    Resolution of the image must be some multiple of the model resolution.""",

    "helpwtrthrshld" :
    """Help: Water Threshold
    0 by Default; Colour value at which sea level is at.
    When making a height map, one may have also included ocean topography, and thus sea level may not be where black(0) is.""",

    "helphghstelvtn" :
    """Help: Highest Elevation
    8849.0 by Default; The highest point of land (in meters).""",

    "helplwstelvtn" :
    """Help: Lowest Elevation
    -11034.0 by Default; The lowest point of land (in meters), used if the planet has no oceans.""",

    "helpimgdbg" :
    """Help: Image Debug
    False by Default; If True will produce debug images showing the land mask during the process of converting images to SRA files.""",

    "helpsranme" :
    """Help: SRA Name
    Set the name to be used for the output SRA files.""",

    "helplndsra" :
    """Help: Land SRA
    N/A by Default; Path to a .sra file containing a land/sea mask for the planet’s geography.
    It’ll ault to Earth’s geography (at least for T21 and T42 runs) if not set.""",

    "helptposra" :
    """Help: Topographic SRA
    N/A by Default; Path to a .sra file containing the planet’s topography.""",

    ####Atmospheric Parameters

    "helprsure" :
    """Help: Pressure
    1.0 by Default; Total surface pressure in bars.
    Unnecessary if one has already set all the partial pressures of the component gasses in your atmosphere,
    Though one can combine this with the partial pressures of some of the component gasses (in which case one should set a gas constant as well).""",

    "helpgscnstnt" :
    """Help: Gas Constant
    287.0 by Default; Effective gas constant, in Joules / (kilograms * Kelvin).
    Can be calculated as the molar gas constant (8.314 J / K*mol) divided by the average molar mass of the atmosphere, in kg/mol.""",

    "helpdrycre" :
    """Help: Dry Core
    False by Default; If True, evaporation is turned off, and a dry atmosphere will be used.""",

    "helpozne" :
    """Help: Ozone
    False by Default; True adds an ozone layer, which slightly increases greenhouse heating, among other effects.
    Any planet with oxygen should probably have some ozone as well.
    However ExoPlaSim’s handling of ozone has been tuned to match Earth and may not be very accurate for significantly different atmospheres or stars.

    Maybe still use it for Earthlike planets with significant atmospheric oxygen orbiting sunlike stars
    Possibly best to exclude otherwise, even though this may cause a slight underestimate in greenhouse heating.""",

    "helpgsprsurs" :
    """Help: Gas Pressures (AKA Partial Pressures)
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
    It is not referenced in determining humidity, any aspect of the water cycle, or greenhouse heating by water vapour.""",

    ####Glacial Parameters

    "helpglcrs" :
    """Help: Glaciers
    False by Default; True allows for new glaciers to form.""",

    "helpgrhght" :
    """Help: Glacier Height
    0.0 by Default; A value of 0 or greater will place glaciers with that depth in meters over all land surfaces when the model starts.
    A value of -1 will not add any initial glaciers.""",

    "helpgrthrshld" :
    """Help: Glacier Threshold
    2.0 by Default; Sets the minimum depth of accumulated snow required for glaciers to form, in meters.""",

    ####Model Dynamic Parameters

    "helptimestep" :
    """Help: Timestep
    45.0 by ault; How much time passes in each step of the simulation, in minutes.
    Longer timesteps will make the simulation run faster, but it may be less stable and accurate.

    For tidal-locked planets 30.0 is recommended, in general if a crash occurs, reduce the timestep
    (especially if the Konsole output refers to “non-finite temperatures”).

    Generally seems to work better if there are a whole number of timesteps in a 24-hour day.
    Timesteps of 5, 6, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, and 60 minutes are all decent options.
    (24 * 60) / timestep = an integer""",

    "helprunsteps" :
    """Help: Runsteps
    11520 by ault; How often averaged data is written to an output file(a simulation year), in number of timesteps.
    By ault this is set for a 360-day year, ExoPlaSim will automatically adjust to different timesteps if not configured here.

    This does not alter the simulated planet’s orbital period, or really any aspect of its climate;
    it merely alters the period of time referred to in later steps that run the model for a period of years, and the length of time represented in the output files.

    Should contain a whole number of NSTPW intervals.
    runsteps / NSTPW = an integer""",

    "helpsnapshots" :
    """Help: Snapshots
    If set, the program will produce a “snapshot” whenever this number of timesteps passes, recording the state of the model at that particular moment.
    If using this, it’s recommended to set it to be equal to around 15 days such that it doesn’t slow down the model too much
    (480 for a 45-minute timestep. 720 for a 30-minute timestep etc.).""",

    "helpnstpw" :
    """Help: NSTPW (Number of STeps Per Write)
    160 by Default; Controls how often data recorded from the model is averaged together, in number of timesteps.

    The amount of time this represents should be kept close to 120 hours.
    It need not necessarily be a whole number of solar days, though that may be convenient to help keep things straight.
    4 < (NSTPW * timestep) / 1440 < ~6 should be best.""",

    "helphysfltr" :
    """Help: Physics Filter
    None by Default; In some cases, it may be necessary to include physics filters.
    This typically becomes necessary when sharp features are projected on the model’s smallest spectral modes, causing Gibbs “ripples”.
    Earth-like models typically do not require filtering, but tidally-locked models do.
    Filtering may be beneficial for Earth-like models at very high resolutions as well, or if there is sharp topography.

    Three filter functional forms are included in ExoPlaSim: Cesaro, exponential, and Lander-Hoskins.""",

    "helpfltrapp" :
    """Help: Filter Application
    None by Default; Physics filters can be applied at two different points;
    Either at the transform from gridpoint to spectral (GP), or the reverse (SP). In most cases, the ideal usage is to use both.

    Generally, a gridpoint->spectral filter is good for dealing with oscillations caused by sharp jumps and small features in the gridpoint tendencies.
    Conversely, a spectral->gridpoint filter is good for dealing with oscillations from small features in spectral fields causing small features to appear in gridpoint tendencies.
    Any oscillations not removed by one filter will be amplified through physical feedbacks if not suppressed by the other filter.""",

    "helpstmclmtlgy" :
    """Help: Storm Climatology
    False by Default; Toggles whether or not storm climatology should be computed.
    If True, output fields related to storm climatology will be added to standard output files.

    NOTE: Enabling this mode currently roughly doubles the computational cost of the model.""",

    "helphghcdnce" :
    """Help: High Cadence
    False by Default; Allows more data to be collected, especially during storm activity.
    May allow one to track the development of individual storms, but may not be accurate at low resolutions.""",

    "helprntbal" :
    """Help: Run To Balance
    False by Default; Runs the model until it appears to have reached equilibrium.
    Judged by the balance between average incoming sunlight and outgoing heat remaining unchanged over several years.""",

    "helprntme" :
    """Help: Run Time
    100 by Default; If Run To Balance not enabled, will run the model for specified amount of years.""",

    "helpthrshld" :
    """Help: Threshold
    0.0005 by Default; Energy balance threshold model should run to, if using Run To Balance.
    In W/m^2/yr average drift in surface energy balance over 45-year timescales.""",

    "helpbslne" :
    """Help: Baseline
    10 by Default; How many years the simulation has to remain at equilibrium before it is determined to be at balance
    (i.e., the amount of drift per year in the balance of incoming and outgoing energy has to remain below the threshold for this many years).""",

    "helpmxyr" :
    """Help: Maximum Year
    100 by Default; The maximum number of years for the simulation to run, even if it hasn’t reached balance by the end.""",

    "helpmnyr" :
    """Help: Minimum Year
    10 by Default; The minimum number of years for the simulation to run, even if it has reached balance by the end.""",

    "helpcrshibrkn" :
    """Help: Crash If Broken
    False by Default; This just helps make crashes a little more graceful and gives somewhat more useful error reports.""",

    "helpcln" :
    """Help: Clean
    False by Default; Deletes temporary files produced each year once an output has been created.
    Should help limit the amount of hard drive space used while running.""",

    "helpalrstrts" :
    """Help: All Years
    False by Default; If set to True, moves the output files from every year of the model run; Otherwise, it only moves the final year.
    These output files can take up a good bit of hard drive space.

    Using this will one average together the data from multiple years when making a koppen map.""",

    "helpkprstrts" :
    """Help: Keep Restarts
    False by Default; If set to True, moves the restart files—which can be used to restart and continue running the model—as well as the outputs.""",
}


def helpTextTk(entry, element, event):

    if isinstance(element, tkinter.Text):
        element.delete('1.0', tkinter.END)
        element.insert('1.0', HELP_DICT[entry])
    helpText(entry, event)

def helpText(entry, event):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(HELP_DICT[entry])

