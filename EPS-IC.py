import sys
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
from os import path
import numpy as np
from matplotlib.image import imread
from PIL import Image, ImageOps
import shutil
import ntpath
import configparser
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

from convert_sra import convert_sra
import helptext as ht

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
rstfletog = 0
stmtog = 0
baltog = 0

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
    lndsra_var.set(filename) # add this
def toposraget():
    filename = askopenfilename(filetypes=(("sra files","*.sra"),("All files","*.*")))
    tposra_var.set(filename) # add this
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
def rstrtfleget():
    filename = askopenfilename(filetypes=(("restart files","*.00000"),("All files","*.*")))
    restrtfle_var.set(filename) # add this
def rstrtfletoggle():
    global rstfletog
    if rstfletog == 0:
        rstfletog = 1
        restrtfle_n.config(state='enabled')
        restrtfle_b.config(state='enabled')
    elif rstfletog == 1:
        rstfletog = 0
        restrtfle_n.config(state='disabled')
        restrtfle_b.config(state='disabled')
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
    if day_check1 - round(float(day_check1)) <= 0.00001:
        if day_check2 == round(day_check2):
            print("Day: Nominal")
        else:
            print("WARNING: Current day length places ratio between (runsteps/12) and ((day*1440)/timestep) at "+str(day_check2)+" which may cause problems with ExoPlaSim.")
            print("Changeing this to an integer will work better.")
    else:
        print("WARNING: Current day length places ratio between (day*1440) and timestep at "+str(day_check1)+" which may cause problems with ExoPlaSim.")
        print("Changing this to an integer will work better.")

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
    param = [str(name_var.get()),str(year_var.get()),str(output_var.get()),str(cpu_var.get()),str(pres_var.get()),str(res_var.get()),str(crash_var.get()),str(layers_var.get()),str(recom_var.get()),str(startemp_var.get()),str(flux_var.get()),str(orbp_var.get()),str(ecc_var.get()),str(obli_var.get()),str(lon_var.get()),str(fixed_var.get()),str(rot_var.get()),str(tidal_var.get()),str(stellon_var.get()),str(desync_var.get()),str(tempcon_var.get()),str(gravity_var.get()),str(radius_var.get()),str(orogph_var.get()),str(aquap_var.get()),str(desertp_var.get()),str(vegetat_var.get()),str(vegacce_var.get()),str(nfrtgrw_var.get()),str(initgrw_var.get()),str(initstcd_var.get()),str(initrgh_var.get()),str(initslc_var.get()),str(initplc_var.get()),str(wetso_var.get()),str(soilalbtog_var.get()),str(soilalb_var.get()),str(soildepthtog_var.get()),str(soildepth_var.get()),str(capsoiltog_var.get()),str(capsoil_var.get()),str(soilwcptog_var.get()),str(soilwcp_var.get()),str(soilsattog_var.get()),str(soilsat_var.get()),str(snowalbtog_var.get()),str(snowalb_var.get()),str(mxsnowtog_var.get()),str(mxsnow_var.get()),str(seaice_var.get()),str(oceanalbtog_var.get()),str(oceanalb_var.get()),str(mldepthtog_var.get()),str(mldepth_var.get()),str(oceanzen_var.get()),str(imgsratogtog_var.get()),str(hghtmpimg_var.get()),str(waterhres_var.get()),str(highelev_var.get()),str(lowelev_var.get()),str(imgdebugtog_var.get()),str(sranme_var.get()),str(lndsra_var.get()),str(tposra_var.get()),str(pressuretog_var.get()),str(pressure_var.get()),str(gascontog_var.get()),str(gascon_var.get()),str(drycoretog_var.get()),str(ozone_var.get()),str(partialptog_var.get()),str(pH2_var.get()),str(pHe_var.get()),str(pN2_var.get()),str(pO2_var.get()),str(pAr_var.get()),str(pNe_var.get()),str(pKr_var.get()),str(pH2O_var.get()),str(pCO2_var.get()),str(glacialtog_var.get()),str(inith_var.get()),str(mndph_var.get()),str(tmestp_var.get()),str(runstp_var.get()),str(snpsht_var.get()),str(nsptw_var.get()),str(restrtfle_var.get()),str(restrtfletog_var.get()),str(phyfilt1_var.get()),str(phyfilt2_var.get()),str(stormcltog_var.get()),str(highcadtog_var.get()),str(rntbaltog_var.get()),str(runtme_var.get()),str(trshld_var.get()),str(bselne_var.get()),str(maxyr_var.get()),str(minyr_var.get()),str(cshibrktog_var.get()),str(cleantog_var.get()),str(allyrstog_var.get()),str(kprststog_var.get())]
    print("Inputs gathered...")

    """Convert heightmap image to SRA files."""
    if param[24] == "False":
        aquaplanetext = ''
        if param[55] == "False":
            convert_sra(
                filepath=filepath,
                infile=param[56],
                grav=float(param[21]),
                debug_img= (param[60]=="True"),
                desert_planet=(param[25]=="True"),
                floor_value=int(param[57]),
                peak_value=float(param[58]),
                trench_value=float(param[59]),
                resotext=param[5],
                sra_name=param[61]
            )
            landmaptext = 'landmap="SRA/'+param[61]+'_surf_0172.sra",'
            topomaptext = 'topomap="SRA/'+param[61]+'_surf_0129.sra",'
        else:
            lndsrafle = ntpath.basename(param[62])
            tposrafle = ntpath.basename(param[63])
            sra_path = path.dirname(filepath)+'/SRA'
            lnd_path = sra_path+"/"+lndsrafle
            tpo_path = sra_path+"/"+tposrafle
            try:
                os.makedirs(sra_path)
            except FileExistsError:
                # directory already exists
                pass
            shutil.copyfile(param[62], lnd_path)
            shutil.copyfile(param[63], tpo_path)
            landmaptext = 'landmap="SRA/'+lndsrafle+'",'
            topomaptext = 'topomap="SRA/'+tposrafle+'",'
    else:
        print("Formatting...")
        aquaplanetext = 'aquaplanet=True,'
        landmaptext = ''
        topomaptext = ''
    if param[25] == "True":
        dsrtplanetext = 'desertplanet=True,'
    else:
        dsrtplanetext = ''

    #Conditions
    if param[6] == "True":
        crashtext = ',crashtolerant='+param[6]
    else:
        crashtext = ''
    if param[8] == "True":
        recomtext = ',recompile='+param[8]
    else:
        recomtext = ''
    if param[17] == "True":
        rottext = 'synchronous='+param[17]+',substellarlon='+param[18]+',desync='+param[19]+',tlcontrast='+param[20]
    else:
        rottext = 'rotationperiod='+param[16]
    if param[23] != "1.0":
        orographtext = ',orography='+param[23]
    else:
        orographtext = ''
    if param[26] == "None":
        vegetationtext = ''
    else:
        if param[26] == "Proscribed":
            vegstat = '				  vegetation=1'+',vegaccel='+param[27]+',nforestgrowth='+param[28]+',initgrowth='+param[29]
        elif param[26] == "Dynamic":
            vegstat = '				  vegetation=2'+',vegaccel='+param[27]+',nforestgrowth='+param[28]+',initgrowth='+param[29]
        vegetationtext = vegstat+',initstomcond='+param[30]+',initrough='+param[31]+',initsoilcarbon='+param[32]+',initplantcarbon='+param[33]+',\n'
    if param[35] == "True":
        soilalbtext = ",soilalbedo="+param[36]
    else:
        soilalbtext = ''
    if param[37] == "True":
        soildepthtext = ",soildepth="+param[38]
    else:
        soildepthtext = ''
    if param[39] == "True":
        soilhcaptext = ",cpsoil="+param[40]
    else:
        soilhcaptext = ''
    if param[41] == "True":
        soilwcaptext = ",soilwatercap="+param[42]
    else:
        soilwcaptext = ''
    if param[43] == "True":
        soilsattext = ",soilsaturation="+param[44]
    else:
        soilsattext = ''
    if param[45] == "True":
        snowalbtext = ",snowicealbedo="+param[46]
    else:
        snowalbtext = ''
    if param[47] == "True":
        maxsnowtext = ",maxsnow="+param[48]
    else:
        maxsnowtext = ''
    if param[50] == "True":
        oceanalbtext = ",oceanalbedo="+param[51]
    else:
        oceanalbtext = ''
    if param[52] == "True":
        mixedlyrtext = ",mldepth="+param[53]
    else:
        mixedlyrtext = ''
    surfacetext1 = param[34]+soilalbtext+soildepthtext+soilhcaptext+soilwcaptext+soilsattext+snowalbtext
    surfacetext2 = maxsnowtext+',seaice='+param[49]+oceanalbtext+mixedlyrtext+',oceanzenith="'+param[54]+'",\n'
    if param[64] == "True":
        atmospheretext = "pressure="+param[65]+','
    else:
        atmospheretext = ''
    if param[66] == "True":
        atmospheretext = atmospheretext+'gascon='+param[67]+','
    else:
        atmospheretext = atmospheretext+''
    if param[68] == "True":
        atmospheretext = atmospheretext+'drycore=True,'
    else:
        atmospheretext = atmospheretext+'drycore=False,'
    if param[69] == "True":
        atmospheretext = atmospheretext+'ozone=True,'
    else:
        atmospheretext = atmospheretext+'ozone=False,'
    if param[70] == "True":
        ppressuretext = "				  pH2="+param[71]+',pHe='+param[72]+',pN2='+param[73]+',pO2='+param[74]+',pAr='+param[75]+',pNe='+param[76]+',pKr='+param[77]+',pH2O='+param[78]+',pCO2='+param[79]+',\n'
    else:
        ppressuretext = ''
    if param[80] == "True":
        glacialtext = "				  glaciers={'toggle': True,'mindepth': "+param[82]+",'initialh': "+param[81]+"},\n"
    else:
        glacialtext = ''
    param[85] = int(param[85])
    if param[85] > 0:
        snapshotstext = ',snapshots='+param[85]
    else:
        snapshotstext = ''
    if param[88] == "True":
        rstrtfle = ntpath.basename(param[87])
        ref_path = path.dirname(filepath)+'/Restart'
        rfle_path = ref_path+"/"+rstrtfle
        try:
            os.makedirs(ref_path)
        except FileExistsError:
            # directory already exists
            pass
        shutil.copyfile(param[87], rfle_path)
        filerstrt = ',restartfile="Restart/'+rstrtfle+'"'
    else:
        filerstrt = ""
    if param[89] == "None":
        physicstext = ''
    elif param[89] == "Cesaro":
        if param[90] == "None":
            physicstext = ''
        elif param[90] == "GP":
            physicstext = ",physicsfilter='gp|cesaro'"
        elif param[90] == "SP":
            physicstext = ",physicsfilter='cesaro|sp'"
        elif param[90] == "GP+SP":
            physicstext = ",physicsfilter='gp|cesaro|sp'"
    elif param[89] == "Exp":
        if param[90] == "None":
            physicstext = ''
        elif param[90] == "GP":
            physicstext = ",physicsfilter='gp|exp'"
        elif param[90] == "SP":
            physicstext = ",physicsfilter='exp|sp'"
        elif param[90] == "GP+SP":
            physicstext = ",physicsfilter='gp|exp|sp'"
    elif param[89] == "Lh":
        if param[90] == "None":
            physicstext = ''
        elif param[90] == "GP":
            physicstext = ",physicsfilter='gp|lh'"
        elif param[90] == "SP":
            physicstext = ",physicsfilter='lh|sp'"
        elif param[90] == "GP+SP":
            physicstext = ",physicsfilter='gp|lh|sp'"
    if param[91] == "True":
        if param[92] == "True":
            stormstext = ",\n				  stormcapture={'toggle': 1,'NKTRIGGER': 1},highcadence={'toggle': 1,'start': 320,'interval': 4,'end': 576})\n"
        else:
            stormstext = ",\n				  stormcapture={'toggle': 1,'NKTRIGGER': 1})\n"
    else:
        stormstext = ')\n'
    if param[93] == "True":
        runtext = param[0]+'.runtobalance(threshold='+param[95]+',baseline='+param[96]+',maxyears='+param[97]+',minyears='+param[98]
    else:
        runtext = param[0]+'.run(years='+param[94]
    if param[100] == "True":
        cleantext = ',clean='+param[100]
    else:
        cleantext = ''

#Formatting
    format_name = "import exoplasim as exo\n"+param[0]+' = exo.Model(workdir="'+param[0]+'",modelname="'+param[0]+'",'
    format_model = "inityear="+param[1]+',outputtype="'+param[2]+'",ncpus='+param[3]+',precision='+param[4]+',resolution="'+param[5]+'"'+crashtext+',layers='+param[7]+recomtext+')\n'
    format_stellar = param[0]+".configure(startemp="+param[9]+',flux='+param[10]+',\n'
    format_orbit = "				  year="+param[11]+',eccentricity='+param[12]+',obliquity='+param[13]+',lonvernaleq='+param[14]+',fixedorbit='+param[15]+',\n'
    format_rotation = "				  "+rottext+',\n'
    format_planet = '				  gravity='+param[21]+',radius='+param[22]+orographtext+',\n'
    format_vegetation = vegetationtext
    format_surface = "				  wetsoil="+surfacetext1+surfacetext2
    format_geography = "				  "+aquaplanetext+dsrtplanetext+landmaptext+topomaptext+'\n'
    format_atmosphere = "				  "+atmospheretext+'\n'
    format_ppressure = ppressuretext
    format_glacier = glacialtext
    format_timekeep = "				  timestep="+param[83]+',runsteps='+param[84]+snapshotstext+",otherargs={'NSTPW@plasim_namelist':'"+param[86]+"'}"+physicstext+filerstrt
    format_storms = stormstext
    format_export = param[0]+".exportcfg()\n"
    format_run = runtext+',crashifbroken='+param[99]+cleantext+')\n'
    format_finalise = param[0]+'.finalize("'+param[0]+'",allyears='+param[101]+',keeprestarts='+param[102]+cleantext+')\n'
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
        print("Saving Complete!")

def save_ini():
    """Save the current parameters."""
    filepath = asksaveasfilename(
        defaultextension="ini",
        filetypes=[("INI Files", "*.ini"), ("All Files", "*.*")],
    )
    if not filepath:
        return
#Getting input text
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    param = [str(name_var.get()),str(year_var.get()),str(output_var.get()),str(cpu_var.get()),str(pres_var.get()),str(res_var.get()),str(crash_var.get()),str(layers_var.get()),str(recom_var.get()),str(startemp_var.get()),str(flux_var.get()),str(orbp_var.get()),str(ecc_var.get()),str(obli_var.get()),str(lon_var.get()),str(fixed_var.get()),str(rot_var.get()),str(tidal_var.get()),str(stellon_var.get()),str(desync_var.get()),str(tempcon_var.get()),str(gravity_var.get()),str(radius_var.get()),str(orogph_var.get()),str(aquap_var.get()),str(desertp_var.get()),str(vegetat_var.get()),str(vegacce_var.get()),str(nfrtgrw_var.get()),str(initgrw_var.get()),str(initstcd_var.get()),str(initrgh_var.get()),str(initslc_var.get()),str(initplc_var.get()),str(wetso_var.get()),str(soilalbtog_var.get()),str(soilalb_var.get()),str(soildepthtog_var.get()),str(soildepth_var.get()),str(capsoiltog_var.get()),str(capsoil_var.get()),str(soilwcptog_var.get()),str(soilwcp_var.get()),str(soilsattog_var.get()),str(soilsat_var.get()),str(snowalbtog_var.get()),str(snowalb_var.get()),str(mxsnowtog_var.get()),str(mxsnow_var.get()),str(seaice_var.get()),str(oceanalbtog_var.get()),str(oceanalb_var.get()),str(mldepthtog_var.get()),str(mldepth_var.get()),str(oceanzen_var.get()),str(imgsratogtog_var.get()),str(hghtmpimg_var.get()),str(waterhres_var.get()),str(highelev_var.get()),str(lowelev_var.get()),str(imgdebugtog_var.get()),str(sranme_var.get()),str(lndsra_var.get()),str(tposra_var.get()),str(pressuretog_var.get()),str(pressure_var.get()),str(gascontog_var.get()),str(gascon_var.get()),str(drycoretog_var.get()),str(ozone_var.get()),str(partialptog_var.get()),str(pH2_var.get()),str(pHe_var.get()),str(pN2_var.get()),str(pO2_var.get()),str(pAr_var.get()),str(pNe_var.get()),str(pKr_var.get()),str(pH2O_var.get()),str(pCO2_var.get()),str(glacialtog_var.get()),str(inith_var.get()),str(mndph_var.get()),str(tmestp_var.get()),str(runstp_var.get()),str(snpsht_var.get()),str(nsptw_var.get()),str(restrtfle_var.get()),str(restrtfletog_var.get()),str(phyfilt1_var.get()),str(phyfilt2_var.get()),str(stormcltog_var.get()),str(highcadtog_var.get()),str(rntbaltog_var.get()),str(runtme_var.get()),str(trshld_var.get()),str(bselne_var.get()),str(maxyr_var.get()),str(minyr_var.get()),str(cshibrktog_var.get()),str(cleantog_var.get()),str(allyrstog_var.get()),str(kprststog_var.get())]
    print("Inputs gathered...")
    config = configparser.ConfigParser()#
    config['Model Parameters'] = {'Project Name': param[0],
                                  'Start Year': param[1],
                                  'Output Type': param[2],
                                  'CPU Count': param[3],
                                  'Precision': param[4],
                                  'Resolution': param[5],
                                  'Crash Tolerant': param[6],
                                  'Layers': param[7],
                                  'Recompile': param[8]}
    config['Stellar Parameters'] = {'Star Temperature': param[9],
                                    'Stellar Flux': param[10]}
    config['Orbital Parameters'] = {'Year Length': param[11],
                                    'Day Length': param[16],
                                    'Eccentricity': param[12],
                                    'Obliquity': param[13],
                                    'Longitude Of Periapsis': param[14],
                                    'Fixed Orbit': param[15]}
    config['Rotational Parameters'] = {'Tidally Locked': param[17],
                                       'Substellar Longitude': param[18],
                                       'Substellar Desync': param[19],
                                       'Temperature Contrast': param[20]}
    config['Planetary Parameters'] = {'Gravity': param[21],
                                      'Radius': param[22],
                                      'Orography': param[23],
                                      'Aqua Planet': param[24],
                                      'Desert Planet': param[25]}
    config['Vegetation Parameters'] = {'Vegetation': param[26],
                                       'Vegetation Acceleration': param[27],
                                       'Biomass Growth': param[28],
                                       'Inital Growth': param[29],
                                       'Stomatal Conductance': param[30],
                                       'Vegetation Roughness': param[31],
                                       'Soil Carbon Content': param[32],
                                       'Plant Carbon Content': param[33]}
    config['Surface Parameters'] = {'Wet Soil': param[34],
                                    'Soil Albedo Toggle': param[35],
                                    'Soil Albedo Value': param[36],
                                    'Soil Depth Toggle': param[37],
                                    'Soil Depth Value': param[38],
                                    'Soil Heat Capacity Toggle': param[39],
                                    'Soil Heat Capacity Value': param[40],
                                    'Soil Water Capacity Toggle': param[41],
                                    'Soil Water Capacity Value': param[42],
                                    'Soil Saturation Toggle': param[43],
                                    'Soil Saturation Value': param[44],
                                    'Snow Albedo Toggle': param[45],
                                    'Snow Albedo Value': param[46],
                                    'Max Snow Toggle': param[47],
                                    'Max Snow Value': param[48],
                                    'Sea Ice': param[49],
                                    'Ocean Albedo Toggle': param[50],
                                    'Ocean Albedo Value': param[51],
                                    'Mixed Layer Depth Toggle': param[52],
                                    'Mixed Layer Depth Value': param[53],
                                    'Ocean Zenith': param[54]}
    config['Geographic Parameters'] = {'Image/SRA Toggle': param[55],
                                       'Height Map Image': param[56],
                                       'Water Threshold': param[57],
                                       'Highest Elevation': param[58],
                                       'Lowest Elevation': param[59],
                                       'Image Debug': param[60],
                                       'SRA Name': param[61],
                                       'Land SRA': param[62],
                                       'Topographic SRA': param[63]}
    config['Atmospheric Parameters'] = {'Pressure Toggle': param[64],
                                        'Pressure Value': param[65],
                                        'Gas Constant Toggle': param[66],
                                        'Gas Constant Value': param[67],
                                        'Dry Core': param[68],
                                        'Ozone': param[69],
                                        'Partial Pressure': param[70],
                                        'Hydrogen': param[71],
                                        'Helium': param[72],
                                        'Nitrogen': param[73],
                                        'Oxygen': param[74],
                                        'Argon': param[75],
                                        'Neon': param[76],
                                        'Krypton': param[77],
                                        'Water': param[78],
                                        'Carbon Dioxide': param[79]}
    config['Glacial Parameters'] = {'Glaciers': param[80],
                                    'Height': param[81],
                                    'Threshold': param[82]}
    config['Model Dynamic Parameters'] = {'Timestep': param[83],
                                          'Runsteps': param[84],
                                          'Snapshots': param[85],
                                          'NSPTW': param[86],
                                          'Restart File Toggle': param[87],
                                          'Restart File Path': param[88],
                                          'Physics Filter': param[89],
                                          'Filter Application': param[90],
                                          'Storm Climatology': param[91],
                                          'High Cadence': param[92],
                                          'Run To Balance': param[93],
                                          'Run Time': param[94],
                                          'Threshold': param[95],
                                          'Baseline': param[96],
                                          'Maximum Year': param[97],
                                          'Minimum Year': param[98],
                                          'Crash If Broken': param[99],
                                          'Clean': param[100],
                                          'All Years': param[101],
                                          'Keep Restarts': param[102]}
    with open(filepath, "w") as output_file:
        config.write(output_file)
    print('Config saved!')

def load_ini():
    filepath = askopenfilename(
        defaultextension="ini",
        filetypes=[("INI Files", "*.ini"), ("All Files", "*.*")])
    if not filepath:
        return
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    param = [name_var,year_var,output_var,cpu_var,pres_var,res_var,crash_var,layers_var,recom_var,startemp_var,flux_var,orbp_var,ecc_var,obli_var,lon_var,fixed_var,rot_var,tidal_var,stellon_var,desync_var,tempcon_var,gravity_var,radius_var,orogph_var,aquap_var,desertp_var,vegetat_var,vegacce_var,nfrtgrw_var,initgrw_var,initstcd_var,initrgh_var,initslc_var,initplc_var,wetso_var,soilalbtog_var,soilalb_var,soildepthtog_var,soildepth_var,capsoiltog_var,capsoil_var,soilwcptog_var,soilwcp_var,soilsattog_var,soilsat_var,snowalbtog_var,snowalb_var,mxsnowtog_var,mxsnow_var,seaice_var,oceanalbtog_var,oceanalb_var,mldepthtog_var,mldepth_var,oceanzen_var,imgsratogtog_var,hghtmpimg_var,waterhres_var,highelev_var,lowelev_var,imgdebugtog_var,sranme_var,lndsra_var,tposra_var,pressuretog_var,pressure_var,gascontog_var,gascon_var,drycoretog_var,ozone_var,partialptog_var,pH2_var,pHe_var,pN2_var,pO2_var,pAr_var,pNe_var,pKr_var,pH2O_var,pCO2_var,glacialtog_var,inith_var,mndph_var,tmestp_var,runstp_var,snpsht_var,nsptw_var,restrtfle_var,restrtfletog_var,phyfilt1_var,phyfilt2_var,stormcltog_var,highcadtog_var,rntbaltog_var,runtme_var,trshld_var,bselne_var,maxyr_var,minyr_var,cshibrktog_var,cleantog_var,allyrstog_var,kprststog_var]
    print('Loading Config parameters...')
    cfg = configparser.ConfigParser()
    cfg.read(filepath)
    mdelprm = cfg['Model Parameters']
    param[0].set(mdelprm.get('Project Name'))
    param[1].set(mdelprm.get('Start Year'))
    param[2].set(mdelprm.get('Output Type'))
    param[3].set(mdelprm.get('CPU Count'))
    param[4].set(mdelprm.get('Precision'))
    param[5].set(mdelprm.get('Resolution'))
    param[6].set(mdelprm.get('Crash Tolerant'))
    param[7].set(mdelprm.get('Layers'))
    param[8].set(mdelprm.get('Recompile'))
    stlrprm = cfg['Stellar Parameters']
    param[9].set(stlrprm.get('Star Temperature'))
    param[10].set(stlrprm.get('Stellar Flux'))
    obtlprm = cfg['Orbital Parameters']
    param[11].set(obtlprm.get('Year Length'))
    param[12].set(obtlprm.get('Eccentricity'))
    param[13].set(obtlprm.get('Obliquity'))
    param[14].set(obtlprm.get('Longitude Of Periapsis'))
    param[15].set(obtlprm.get('Fixed Orbit'))
    param[16].set(obtlprm.get('Day Length'))
    rtnlprm = cfg['Rotational Parameters']
    param[17].set(rtnlprm.get('Tidally Locked'))
    param[18].set(rtnlprm.get('Substellar Longitude'))
    param[19].set(rtnlprm.get('Substellar Desync'))
    param[20].set(rtnlprm.get('Temperature Contrast'))
    plntprm = cfg['Planetary Parameters']
    param[21].set(plntprm.get('Gravity'))
    param[22].set(plntprm.get('Radius'))
    param[23].set(plntprm.get('Orography'))
    param[24].set(plntprm.get('Aqua Planet'))
    param[25].set(plntprm.get('Desert Planet'))
    vgtnprm = cfg['Vegetation Parameters']
    param[26].set(vgtnprm.get('Vegetation'))
    param[27].set(vgtnprm.get('Vegetation Acceleration'))
    param[28].set(vgtnprm.get('Biomass Growth'))
    param[29].set(vgtnprm.get('Inital Growth'))
    param[30].set(vgtnprm.get('Stomatal Conductance'))
    param[31].set(vgtnprm.get('Vegetation Roughness'))
    param[32].set(vgtnprm.get('Soil Carbon Content'))
    param[33].set(vgtnprm.get('Plant Carbon Content'))
    srfcprm = cfg['Surface Parameters']
    param[34].set(srfcprm.get('Wet Soil'))
    param[35].set(srfcprm.get('Soil Albedo Toggle'))
    param[36].set(srfcprm.get('Soil Albedo Value'))
    param[37].set(srfcprm.get('Soil Depth Toggle'))
    param[38].set(srfcprm.get('Soil Depth Value'))
    param[39].set(srfcprm.get('Soil Heat Capacity Toggle'))
    param[40].set(srfcprm.get('Soil Heat Capacity Value'))
    param[41].set(srfcprm.get('Soil Water Capacity Toggle'))
    param[42].set(srfcprm.get('Soil Water Capacity Value'))
    param[43].set(srfcprm.get('Soil Saturation Toggle'))
    param[44].set(srfcprm.get('Soil Saturation Value'))
    param[45].set(srfcprm.get('Snow Albedo Toggle'))
    param[46].set(srfcprm.get('Snow Albedo Value'))
    param[47].set(srfcprm.get('Max Snow Toggle'))
    param[48].set(srfcprm.get('Max Snow Value'))
    param[49].set(srfcprm.get('Sea Ice'))
    param[50].set(srfcprm.get('Ocean Albedo Toggle'))
    param[51].set(srfcprm.get('Ocean Albedo Value'))
    param[52].set(srfcprm.get('Mixed Layer Depth Toggle'))
    param[53].set(srfcprm.get('Mixed Layer Depth Value'))
    param[54].set(srfcprm.get('Ocean Zenith'))
    geogprm = cfg['Geographic Parameters']
    param[55].set(geogprm.get('Image/SRA Toggle'))
    param[56].set(geogprm.get('Height Map Image'))
    param[57].set(geogprm.get('Water Threshold'))
    param[58].set(geogprm.get('Highest Elevation'))
    param[59].set(geogprm.get('Lowest Elevation'))
    param[60].set(geogprm.get('Image Debug'))
    param[61].set(geogprm.get('SRA Name'))
    param[62].set(geogprm.get('Land SRA'))
    param[63].set(geogprm.get('Topographic SRA'))
    atmoprm = cfg['Atmospheric Parameters']
    param[64].set(atmoprm.get('Pressure Toggle'))
    param[65].set(atmoprm.get('Pressure Value'))
    param[66].set(atmoprm.get('Gas Constant Toggle'))
    param[67].set(atmoprm.get('Gas Constant Value'))
    param[68].set(atmoprm.get('Dry Core'))
    param[69].set(atmoprm.get('Ozone'))
    param[70].set(atmoprm.get('Partial Pressure'))
    param[71].set(atmoprm.get('Hydrogen'))
    param[72].set(atmoprm.get('Helium'))
    param[73].set(atmoprm.get('Nitrogen'))
    param[74].set(atmoprm.get('Oxygen'))
    param[75].set(atmoprm.get('Argon'))
    param[76].set(atmoprm.get('Neon'))
    param[77].set(atmoprm.get('Krypton'))
    param[78].set(atmoprm.get('Water'))
    param[79].set(atmoprm.get('Carbon Dioxide'))
    glclprm = cfg['Glacial Parameters']
    param[80].set(glclprm.get('Glaciers'))
    param[81].set(glclprm.get('Height'))
    param[82].set(glclprm.get('Threshold'))
    mdldprm = cfg['Model Dynamic Parameters']
    param[83].set(mdldprm.get('Timestep'))
    param[84].set(mdldprm.get('Runsteps'))
    param[85].set(mdldprm.get('Snapshots'))
    param[86].set(mdldprm.get('NSPTW'))
    param[87].set(mdldprm.get('Restart File Toggle'))
    param[88].set(mdldprm.get('Restart File Path'))
    param[89].set(mdldprm.get('Physics Filter'))
    param[90].set(mdldprm.get('Filter Application'))
    param[91].set(mdldprm.get('Storm Climatology'))
    param[92].set(mdldprm.get('High Cadence'))
    param[93].set(mdldprm.get('Run To Balance'))
    param[94].set(mdldprm.get('Run Time'))
    param[95].set(mdldprm.get('Threshold'))
    param[96].set(mdldprm.get('Baseline'))
    param[97].set(mdldprm.get('Maximum Year'))
    param[98].set(mdldprm.get('Minimum Year'))
    param[99].set(mdldprm.get('Crash If Broken'))
    param[100].set(mdldprm.get('Clean'))
    param[101].set(mdldprm.get('All Years'))
    param[102].set(mdldprm.get('Keep Restarts'))
    print('Config parameters loaded!')

window = Tk()# Start the application
window.title("ExoPlaSim: Input Configurator (EPS:IC)")
window.rowconfigure([2], minsize=10, weight=0)
window.columnconfigure([2,4,6,8], minsize=10, weight=1)

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=7)
text_font = font.nametofont("TkTextFont")
text_font.configure(size=7)
help_font = font.nametofont("TkFixedFont")
help_font.configure(size=7)

#Frame creation method
def createColFrame(rowIn, colIn, gridIndex):
    frame = Frame()
    frame.grid(row=rowIn,column=colIn,sticky="n")
    frame.rowconfigure(gridIndex, minsize=10, weight=1)
    return frame

def createParameterFrame(masterIn, rowIn, colIn, gridIndex):
    frame = Frame(master=masterIn,relief=GROOVE,borderwidth=3)
    frame.grid(row=rowIn,column=colIn,sticky="new")
    frame.rowconfigure(gridIndex, minsize=20)
    return frame

def createOptionLabel(masterIn, textIn, helpText, rowIn, colIn):
    label = Label(master=masterIn,text=textIn,foreground=txtcol)
    label.bind("<Motion>", lambda event: ht.helpTextTk(helpText, statusBox , event))
    label.grid(row=rowIn, column=colIn, sticky="w")
    return label

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_one_frame = createColFrame(1, 1, [2,4,6])

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Model Parameter Frame
modpar_frame = createParameterFrame(col_one_frame, 1, 1, [1,2,3,4,5,6,7,8,9])

modelparam = Label(master=modpar_frame,text="Model Parameters")
modelparam.grid(row=0, column=1,columnspan=2,sticky="n")

#Project Name
project = createOptionLabel(masterIn=modpar_frame, textIn="Project Name: ", helpText="helpjctnme", rowIn=1, colIn=1)
name_var = StringVar()
name_var.set('Earth')
name = Entry(master=modpar_frame,width=7, textvariable=name_var)
name.grid(row=1, column=2, sticky="w")

#Start Year
year = createOptionLabel(masterIn=modpar_frame, textIn="Start Year: ", helpText="helpstrtyr", rowIn=2, colIn=1)
year_var = IntVar()
year_var.set(0)
year_n = Entry(master=modpar_frame,textvariable=year_var, width=7)
year_n.grid(row=2, column=2, sticky="w")

#Output Type
outputtype = createOptionLabel(masterIn=modpar_frame, textIn="Output Type: ", helpText="helpotptype", rowIn=3, colIn=1)
output_options = [".nc", ".nc", ".npy", ".npz", ".hdf5", ".he5", ".h5", ".csv", ".gz", ".txt", ".tar", ".tar.gz", ".tar.xz", ".tar.bz2"]
output_var = StringVar()
output_var.set(output_options[0])
outputtxt = OptionMenu(modpar_frame, output_var, *output_options)
outputtxt.config(width=6)
outputtxt.grid(row=3,column=2, sticky="w")

#CPU Count
cpu = createOptionLabel(masterIn=modpar_frame, textIn="CPU Count: ", helpText="helpcpucnt", rowIn=4, colIn=1)
cpu_var = IntVar()
cpu_var.set(4)
cpu_n = Entry(master=modpar_frame,textvariable=cpu_var, width=7)
cpu_n.grid(row=4, column=2, sticky="w")

#Precision
pres = createOptionLabel(masterIn=modpar_frame, textIn="Precision: ", helpText="helpresision", rowIn=5, colIn=1)
pres_options = ["8", "4", "8"]

pres_var = StringVar()
pres_var.set(pres_options[0])
pres_n = OptionMenu(modpar_frame, pres_var, *pres_options)
pres_n.config(width=6)
pres_n.grid(row=5, column=2, sticky="w")

#Resolution
resolution = createOptionLabel(masterIn=modpar_frame, textIn="Resolution: ", helpText="helpresolution", rowIn=6, colIn=1)
res_options = ["T21", "T21", "T42", "T63", "T85", "T106", "T127", "T170"]

res_var = StringVar()
res_var.set(res_options[0])
res = OptionMenu(modpar_frame, res_var, *res_options)
res.config(width=6)
res.grid(row=6,column=2, sticky="w")

#Crash Tolerant
crash = resolution = createOptionLabel(masterIn=modpar_frame, textIn="Crash Tolerant: ", helpText="helpcrshtlrnt", rowIn=7, colIn=1)
crash_var = StringVar()
crash_var.set("False")
crashtol = Checkbutton(master=modpar_frame,variable=crash_var, onvalue='True', offvalue='False')
crashtol.grid(row=7, column=2, sticky="w")

#Layers
layers = createOptionLabel(masterIn=modpar_frame, textIn="Layers: ", helpText="helplayers", rowIn=8, colIn=1)
layers_var = IntVar()
layers_var.set(10)
layers_n = Entry(master=modpar_frame,textvariable=layers_var, width=7)
layers_n.grid(row=8, column=2, sticky="w")

#Recompile
recom = resolution = createOptionLabel(masterIn=modpar_frame, textIn="Recompile: ", helpText="helprecompile", rowIn=9, colIn=1)
recom_var = StringVar()
recom_var.set("False")
recom_n = Checkbutton(master=modpar_frame,variable=recom_var, onvalue='True', offvalue='False')
recom_n.grid(row=9, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Stellar Parameter Frame
stelpar_frame = createParameterFrame(masterIn=col_one_frame, rowIn=3, colIn=1, gridIndex=[1,2])

modelparam = Label(master=stelpar_frame,text="Stellar Parameters")
modelparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Star Temperature
startemp = createOptionLabel(masterIn=stelpar_frame, textIn="Star Temp. (K): ", helpText="helpstrtmp", rowIn=1, colIn=1)
startemp_var = DoubleVar()
startemp_var.set(5772.0)
startemp_n = Entry(master=stelpar_frame,textvariable=startemp_var, width=7)
startemp_n.grid(row=1, column=2, sticky="w")

#Stellar Flux
flux = createOptionLabel(masterIn=stelpar_frame, textIn="Stellar Flux (W/m²): ", helpText="helpstlrflx", rowIn=2, colIn=1)
flux_var = DoubleVar()
flux_var.set(1367.0)
flux_n = Entry(master=stelpar_frame,textvariable=flux_var, width=7)
flux_n.grid(row=2, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Orbital Parameter Frame
orbitpar_frame = createParameterFrame(masterIn=col_one_frame, rowIn=5, colIn=1, gridIndex=[1,2,3,4,5,6])

orbitparam = Label(master=orbitpar_frame,text="Orbital Parameters")
orbitparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Orbital Period
orbp = createOptionLabel(masterIn=orbitpar_frame, textIn="Year Length (E. Days): ", helpText="helpyrlngth", rowIn=1, colIn=1)
orbp_var = DoubleVar()
orbp_var.set(365.25)
orbp_n = Entry(master=orbitpar_frame,textvariable=orbp_var, width=7)
orbp_n.grid(row=1, column=2, sticky="w")

#Rotation Period
rot = createOptionLabel(masterIn=orbitpar_frame, textIn="Day Length (E. Days): ", helpText="helpdaylngth", rowIn=2, colIn=1)
rot_var = DoubleVar()
rot_var.set(1.0)
rot_n = Entry(master=orbitpar_frame,textvariable=rot_var, width=7)
rot_n.grid(row=2, column=2, sticky="w")

#Eccentricity
ecc = createOptionLabel(masterIn=orbitpar_frame, textIn="Eccentricity: ", helpText="helpeccentr", rowIn=3, colIn=1)
ecc_var = DoubleVar()
ecc_var.set(0.016715)
ecc_n = Entry(master=orbitpar_frame,textvariable=ecc_var, width=7)
ecc_n.grid(row=3, column=2, sticky="w")

#Obliquity
obli = createOptionLabel(masterIn=orbitpar_frame, textIn="Obliquity (°): ", helpText="helpoblqty", rowIn=4, colIn=1)
obli_var = DoubleVar()
obli_var.set(23.441)
obli_n = Entry(master=orbitpar_frame,textvariable=obli_var, width=7)
obli_n.grid(row=4, column=2, sticky="w")

#Longitude of Periapsis
lon = createOptionLabel(masterIn=orbitpar_frame, textIn="Long. of Periapsis (°): ", helpText="helplngpri", rowIn=5, colIn=1)
lon_var = DoubleVar()
lon_var.set(102.7)
lon_n = Entry(master=orbitpar_frame,textvariable=lon_var, width=7)
lon_n.grid(row=5, column=2, sticky="w")

#Fixed Orbit
fixed = createOptionLabel(masterIn=orbitpar_frame, textIn="Fixed Orbit: ", helpText="helpfxdobt", rowIn=6, colIn=1)
fixed_var = StringVar()
fixed_var.set('True')
fixedorb = Checkbutton(master=orbitpar_frame,variable=fixed_var, onvalue='True', offvalue='False')
fixedorb.grid(row=6, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_two_frame = createColFrame(1, 3, [2,4])

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Rotational Parameter Frame

rotatpar_frame = createParameterFrame(col_two_frame, 1, 1, [1,2,3,4])
rotatpar_frame.columnconfigure([2], minsize=60)

rotatparam = Label(master=rotatpar_frame,text="Rotational Parameters")
rotatparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Tidally Locked
tidal = createOptionLabel(masterIn=rotatpar_frame, textIn="Tidally Locked: ", helpText="helptdlkd", rowIn=1, colIn=1)
tidal_var = StringVar()
tidal_var.set('False')
tidalock = Checkbutton(master=rotatpar_frame,variable=tidal_var,command=tidaltoggle, onvalue='True', offvalue='False')
tidalock.grid(row=1, column=2, sticky="w")

#Substellar Longitude
stellon = createOptionLabel(masterIn=rotatpar_frame, textIn="Substellar Longitude (°): ", helpText="helpsbstlrlng", rowIn=2, colIn=1)
stellon_var = DoubleVar()
stellon_var.set(180)
stellon_n = Entry(master=rotatpar_frame,textvariable=stellon_var, width=7)
stellon_n.config(state='disabled')
stellon_n.grid(row=2, column=2, sticky="w")

#Desync
desync = createOptionLabel(masterIn=rotatpar_frame, textIn="Substellar Desync (°/min): ", helpText="helpsbstlrdsync", rowIn=3, colIn=1)
desync_var = DoubleVar()
desync_var.set(0.0)
desync_n = Entry(master=rotatpar_frame,textvariable=desync_var, width=7)
desync_n.config(state='disabled')
desync_n.grid(row=3, column=2, sticky="w")

#Temp. Contrast
tempcon = createOptionLabel(masterIn=rotatpar_frame, textIn="Temp. Contrast (K): ", helpText="helptmpcntrst", rowIn=4, colIn=1)
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
gravity = createOptionLabel(masterIn=planetpar_frame, textIn="Gravity (m/s²): ", helpText="helpgrvty", rowIn=1, colIn=1)
gravity_var = DoubleVar()
gravity_var.set(9.80665)
gravity_n = Entry(master=planetpar_frame,textvariable=gravity_var, width=7)
gravity_n.grid(row=1, column=2, sticky="w")

#Radius
radius = createOptionLabel(masterIn=planetpar_frame, textIn="Radius (E. Radii): ", helpText="helprdus", rowIn=2, colIn=1)
radius_var = DoubleVar()
radius_var.set(1.0)
radius_n = Entry(master=planetpar_frame,textvariable=radius_var, width=7)
radius_n.grid(row=2, column=2, sticky="w")

#Orography
orogph = createOptionLabel(masterIn=planetpar_frame, textIn="Orography: ", helpText="helporgrphy", rowIn=3, colIn=1)
orogph_var = DoubleVar()
orogph_var.set(1.0)
orogph_n = Entry(master=planetpar_frame,textvariable=orogph_var, width=7)
orogph_n.grid(row=3, column=2, sticky="w")

#Aqua Planet
aquap = createOptionLabel(masterIn=planetpar_frame, textIn="Aqua Planet: ", helpText="helpaquaplnt", rowIn=4, colIn=1)
aquap_var = StringVar()
aquap_var.set('False')
aquap_n = Checkbutton(master=planetpar_frame,variable=aquap_var,command=aquatoggle, onvalue='True', offvalue='False')
aquap_n.config(state='enabled')
aquap_n.grid(row=4, column=2, sticky="w")

#Desert Planet
desertp = createOptionLabel(masterIn=planetpar_frame, textIn="Desert Planet: ", helpText="helpdsrtplnt", rowIn=5, colIn=1)
desertp_var = StringVar()
desertp_var.set('False')
desertp_n = Checkbutton(master=planetpar_frame,variable=desertp_var,command=dsrtoggle, onvalue='True', offvalue='False')
desertp_n.config(state='enabled')
desertp_n.grid(row=5, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Geographic Parameter Frame
geopar_frame = createParameterFrame(masterIn=col_two_frame, rowIn=5, colIn=1, gridIndex=[1,2,3,4,5,6,7,8,9])

geoparam = Label(master=geopar_frame,text="Geographic Parameters")
geoparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Image/SRA Toggle
imgsratog = createOptionLabel(masterIn=geopar_frame, textIn="Image/SRA Toggle: ", helpText="helpimgsratog", rowIn=1, colIn=1)
imgsratogtog_var = StringVar()
imgsratogtog_var.set('False')
imgsratogtog_n = Checkbutton(master=geopar_frame,variable=imgsratogtog_var,command=imgsratoggle, onvalue='True', offvalue='False')
imgsratogtog_n.grid(row=1, column=2, sticky="w")

#Height Map Image
hghtmpimg = createOptionLabel(masterIn=geopar_frame, textIn="Height Map Image: ", helpText="helphghtmpimg", rowIn=2, colIn=1)
hghtmpimg_var = StringVar()
hghtmpimg_var.set('')
hghtmpimg_n = Entry(master=geopar_frame,textvariable=hghtmpimg_var, width=7)
hghtmpimg_n.config(state='enabled')
hghtmpimg_n.grid(row=2, column=2, sticky="w")
hghtmpimg_b = Button(master=geopar_frame,text="...",command=hghtimgget, width=3)
hghtmpimg_b.config(state='enabled')
hghtmpimg_b.grid(row=2, column=3, sticky="w")

#Water Threshold
waterhres = createOptionLabel(masterIn=geopar_frame, textIn="Water Threshold: ", helpText="helpwtrthrshld", rowIn=3, colIn=1)
waterhres_var = IntVar()
waterhres_var.set(0)
waterhres_n = Entry(master=geopar_frame,textvariable=waterhres_var, width=7)
waterhres_n.config(state='enabled')
waterhres_n.grid(row=3, column=2, sticky="w")

#Highest Elevation
highelev = createOptionLabel(masterIn=geopar_frame, textIn="Highest Elevation (m): ", helpText="helphghstelvtn", rowIn=4, colIn=1)
highelev_var = DoubleVar()
highelev_var.set(8849.0)
highelev_n = Entry(master=geopar_frame,textvariable=highelev_var, width=7)
highelev_n.config(state='enabled')
highelev_n.grid(row=4, column=2, sticky="w")

#Lowest Elevation
lowelev = createOptionLabel(masterIn=geopar_frame, textIn="Lowest Elevation (m): ", helpText="helplwstelvtn", rowIn=5, colIn=1)
lowelev_var = DoubleVar()
lowelev_var.set(-11034.0)
lowelev_n = Entry(master=geopar_frame,textvariable=lowelev_var, width=7)
lowelev_n.config(state='disabled')
lowelev_n.grid(row=5, column=2, sticky="w")

#Image Debug
imgdebug = createOptionLabel(masterIn=geopar_frame, textIn="Image Debug: ", helpText="helpimgdbg", rowIn=6, colIn=1)
imgdebugtog_var = StringVar()
imgdebugtog_var.set('False')
imgdebugtog_n = Checkbutton(master=geopar_frame,variable=imgdebugtog_var, onvalue='True', offvalue='False')
imgdebugtog_n.config(state='enabled')
imgdebugtog_n.grid(row=6, column=2, sticky="w")

#SRA Name
sranme = createOptionLabel(masterIn=geopar_frame, textIn="SRA Name: ", helpText="helpsranme", rowIn=7, colIn=1)
sranme_var = StringVar()
sranme_var.set("earth")
sranme_n = Entry(master=geopar_frame,textvariable=sranme_var, width=7)
sranme_n.config(state='enabled')
sranme_n.grid(row=7, column=2, sticky="w")

#Land SRA
lndsra = createOptionLabel(masterIn=geopar_frame, textIn="Land SRA: ", helpText="helplndsra", rowIn=8, colIn=1)
lndsra_var = StringVar()
lndsra_var.set('')
lndsra_n = Entry(master=geopar_frame,textvariable=lndsra_var, width=7)
lndsra_n.config(state='disabled')
lndsra_n.grid(row=8, column=2, sticky="w")
lndsra_b = Button(master=geopar_frame,text="...",command=landsraget, width=3)
lndsra_b.config(state='disabled')
lndsra_b.grid(row=8, column=3, sticky="w")

#Topo SRA
tposra = createOptionLabel(masterIn=geopar_frame, textIn="Topographic SRA: ", helpText="helptposra", rowIn=9, colIn=1)
tposra_var = StringVar()
tposra_var.set('')
tposra_n = Entry(master=geopar_frame,textvariable=tposra_var, width=7)
tposra_n.config(state='disabled')
tposra_n.grid(row=9, column=2, sticky="w")
tposra_b = Button(master=geopar_frame,text="...",command=toposraget, width=3)
tposra_b.config(state='disabled')
tposra_b.grid(row=9, column=3, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_three_frame = createColFrame(1, 5, [2])

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Surface Parameter Frame
surfpar_frame = createParameterFrame(masterIn=col_three_frame, rowIn=1, colIn=1, gridIndex=[1,2,3,4,5,6,7,8,9,10,11,12])
surfparam = Label(master=surfpar_frame,text="Surface Parameters")
surfparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Wet Soil
wetso = createOptionLabel(masterIn=surfpar_frame, textIn="Wet Soil: ", helpText="helpwtsl", rowIn=1, colIn=1)
wetso_var = StringVar()
wetso_var.set("False")
wetsoil = Checkbutton(master=surfpar_frame,variable=wetso_var, onvalue='True', offvalue='False')
wetsoil.grid(row=1, column=2, sticky="w")

#Soil Albedo
soilalb = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Albedo: ", helpText="helpslalbdo", rowIn=2, colIn=1)
soilalb_var = DoubleVar()
soilalb_var.set(0.0)
soilalb_n = Entry(master=surfpar_frame,textvariable=soilalb_var, width=7)
soilalb_n.config(state='disabled')
soilalb_n.grid(row=2, column=2, sticky="w")
##Soil Albedo Toggle
soilalbtog_var = StringVar()
soilalbtog_var.set('False')
soilalbtog_n = Checkbutton(master=surfpar_frame,variable=soilalbtog_var,command=soilalbtoggle, onvalue='True', offvalue='False')
soilalbtog_n.grid(row=2, column=3, sticky="w")

#Soil Depth
soildepth = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Depth (m): ", helpText="helpsldpth", rowIn=3, colIn=1)
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
capsoil = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Heat Capacity: ", helpText="helpslhtcpsty", rowIn=4, colIn=1)
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
soilwcp = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Water Capacity: ", helpText="helpslwtrcpsty", rowIn=5, colIn=1)
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
soilsat = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Saturation: ", helpText="helpslstrtn", rowIn=6, colIn=1)
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
snowalb = createOptionLabel(masterIn=surfpar_frame, textIn="Snow Albedo: ", helpText="helpsnwalb", rowIn=7, colIn=1)
snowalb_var = DoubleVar()
snowalb_var.set(0.0)
snowalb_n = Entry(master=surfpar_frame,textvariable=snowalb_var, width=7)
snowalb_n.config(state='disabled')
snowalb_n.grid(row=7, column=2, sticky="w")
##Snow Albedo Toggle
snowalbtog_var = StringVar()
snowalbtog_var.set('False')
snowalbtog_n = Checkbutton(master=surfpar_frame,variable=snowalbtog_var,command=snowalbtoggle, onvalue='True', offvalue='False')
snowalbtog_n.grid(row=7, column=3, sticky="w")

#Max Snow
mxsnow = createOptionLabel(masterIn=surfpar_frame, textIn="Max Snow (m): ", helpText="helpmxsnw", rowIn=8, colIn=1)
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
seaice = createOptionLabel(masterIn=surfpar_frame, textIn="Sea Ice: ", helpText="helpseaice", rowIn=9, colIn=1)
seaice_var = StringVar()
seaice_var.set('True')
seaice_n = Checkbutton(master=surfpar_frame,variable=seaice_var, onvalue='True', offvalue='False')
seaice_n.grid(row=9, column=2, sticky="w")

#Ocean Albedo
oceanalb = createOptionLabel(masterIn=surfpar_frame, textIn="Ocean Albedo: ", helpText="helpocnalb", rowIn=10, colIn=1)
oceanalb_var = DoubleVar()
oceanalb_var.set(0.0)
oceanalb_n = Entry(master=surfpar_frame,textvariable=snowalb_var, width=7)
oceanalb_n.config(state='disabled')
oceanalb_n.grid(row=10, column=2, sticky="w")
##Snow Albedo Toggle
oceanalbtog_var = StringVar()
oceanalbtog_var.set('False')
oceanalbtog_n = Checkbutton(master=surfpar_frame,variable=oceanalbtog_var,command=oceanalbtoggle, onvalue='True', offvalue='False')
oceanalbtog_n.grid(row=10, column=3, sticky="w")

#Mixed Ocean Depth
mldepth = createOptionLabel(masterIn=surfpar_frame, textIn="Mixed Layer Depth (m): ", helpText="helpmxdlyrdpth", rowIn=11, colIn=1)
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
oceanzen = createOptionLabel(masterIn=surfpar_frame, textIn="Ocean Zenith: ", helpText="helpocnznth", rowIn=12, colIn=1)
oceanzen_options = ["ECHAM-3", "Lambertian", "uniform", "ECHAM-3", "plasim", "default", "ECHAM-6"]

oceanzen_var = StringVar()
oceanzen_var.set(oceanzen_options[0])
oceanzen_n = OptionMenu(surfpar_frame, oceanzen_var, *oceanzen_options)
oceanzen_n.config(width=7)
oceanzen_n.grid(row=12,column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Vegetation Parameter Frame
vegpar_frame = createParameterFrame(masterIn=col_three_frame, rowIn=3, colIn=1, gridIndex=[1,2,3,4,5,6,7,8])

vegparam = Label(master=vegpar_frame,text="Vegetation Parameters")
vegparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Vegetation
vegetat = createOptionLabel(masterIn=vegpar_frame, textIn="Vegetation: ", helpText="helpvgtn", rowIn=1, colIn=1)
vegetat_options = ["None", "None", "Proscribed", "Dynamic"]

vegetat_var = StringVar()
vegetat_var.set(vegetat_options[0])
vegetat_n = OptionMenu(vegpar_frame, vegetat_var, *vegetat_options, command=vegtoggle)
vegetat_n.config(width=7)
vegetat_n.grid(row=1, column=2, sticky="w")

#Veg. Acceleration
vegacce = createOptionLabel(masterIn=vegpar_frame, textIn="Veg. Acceleration: ", helpText="helpvgaclrtn", rowIn=2, colIn=1)
vegacce_var = IntVar()
vegacce_var.set(1)
vegacce_n = Entry(master=vegpar_frame,textvariable=vegacce_var, width=7)
vegacce_n.config(state='disabled')
vegacce_n.grid(row=2, column=2, sticky="w")

#Biomass Growth
nfrtgrw = createOptionLabel(masterIn=vegpar_frame, textIn="Biomass Growth: ", helpText="helpbiomsgrwth", rowIn=3, colIn=1)
nfrtgrw_var = DoubleVar()
nfrtgrw_var.set(1.0)
nfrtgrw_n = Entry(master=vegpar_frame,textvariable=nfrtgrw_var, width=7)
nfrtgrw_n.config(state='disabled')
nfrtgrw_n.grid(row=3, column=2, sticky="w")

#Initial Growth
initgrw = createOptionLabel(masterIn=vegpar_frame, textIn="Initial Growth: ", helpText="helpintlgrth", rowIn=4, colIn=1)
initgrw_var = DoubleVar()
initgrw_var.set(0.5)
initgrw_n = Entry(master=vegpar_frame,textvariable=initgrw_var, width=7)
initgrw_n.config(state='disabled')
initgrw_n.grid(row=4, column=2, sticky="w")

#Initial Stomatal Conductance
initstcd = createOptionLabel(masterIn=vegpar_frame, textIn="Stomatal Conductance: ", helpText="helpstmtlcndtnce", rowIn=5, colIn=1)
initstcd_var = DoubleVar()
initstcd_var.set(1.0)
initstcd_n = Entry(master=vegpar_frame,textvariable=initstcd_var, width=7)
initstcd_n.config(state='disabled')
initstcd_n.grid(row=5, column=2, sticky="w")

#Initial Vegetative Surface Roughness
initrgh = createOptionLabel(masterIn=vegpar_frame, textIn="Vegetation Roughness: ", helpText="helpvgtnrghns", rowIn=6, colIn=1)
initrgh_var = DoubleVar()
initrgh_var.set(2.0)
initrgh_n = Entry(master=vegpar_frame,textvariable=initrgh_var, width=7)
initrgh_n.config(state='disabled')
initrgh_n.grid(row=6, column=2, sticky="w")

#Initial Soil Carbon Content
initslc = createOptionLabel(masterIn=vegpar_frame, textIn="Soil Carbon Content: ", helpText="helpslcbncntnt", rowIn=7, colIn=1)
initslc_var = DoubleVar()
initslc_var.set(0.0)
initslc_n = Entry(master=vegpar_frame,textvariable=initslc_var, width=7)
initslc_n.config(state='disabled')
initslc_n.grid(row=7, column=2, sticky="w")

#Initial Vegetative Carbon Content
initplc = createOptionLabel(masterIn=vegpar_frame, textIn="Plant Carbon Content: ", helpText="helplntcbncntnt", rowIn=8, colIn=1)
initplc_var = DoubleVar()
initplc_var.set(0.0)
initplc_n = Entry(master=vegpar_frame,textvariable=initplc_var, width=7)
initplc_n.config(state='disabled')
initplc_n.grid(row=8, column=2, sticky="w")

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
atmpar_frame = createParameterFrame(masterIn=col_four_frame, rowIn=1, colIn=1, gridIndex=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])

atmparam = Label(master=atmpar_frame,text="Atmospheric Parameters")
atmparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Pressure
pressure = createOptionLabel(masterIn=atmpar_frame, textIn="Pressure (bar): ", helpText="helprsure", rowIn=1, colIn=1)
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
gascon = createOptionLabel(masterIn=atmpar_frame, textIn="Gas Constant: ", helpText="helpgscnstnt", rowIn=2, colIn=1)
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
drycore = createOptionLabel(masterIn=atmpar_frame, textIn="Dry Core: ", helpText="helpdrycre", rowIn=3, colIn=1)
drycoretog_var = StringVar()
drycoretog_var.set('False')
drycoretog_n = Checkbutton(master=atmpar_frame,variable=drycoretog_var, onvalue='True', offvalue='False')
drycoretog_n.grid(row=3, column=2, sticky="w")

#Ozone
ozone = createOptionLabel(masterIn=atmpar_frame, textIn="Ozone: ", helpText="helpozne", rowIn=4, colIn=1)
ozone_var = StringVar()
ozone_var.set('False')
ozone_n = Checkbutton(master=atmpar_frame,variable=ozone_var, onvalue='True', offvalue='False')
ozone_n.grid(row=4, column=2, sticky="w")

#Partial Pressure
partialp = createOptionLabel(masterIn=atmpar_frame, textIn="Gas Pressure (bar): ", helpText="helpgsprsurs", rowIn=5, colIn=1)
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
glacpar_frame = createParameterFrame(masterIn=col_four_frame, rowIn=3, colIn=1, gridIndex=[1,2,3])
glacpar_frame.columnconfigure([2], minsize=80)

glacparam = Label(master=glacpar_frame,text="Glacial Parameters")
glacparam.grid(row=0,column=1,columnspan=3, sticky="n")

#Glacier Toggle
glacial = createOptionLabel(masterIn=glacpar_frame, textIn="Glaciers: ", helpText="helpglcrs", rowIn=1, colIn=1)
glacialtog_var = StringVar()
glacialtog_var.set('False')
glacialtog_n = Checkbutton(master=glacpar_frame,variable=glacialtog_var,command=gtoggle, onvalue='True', offvalue='False')
glacialtog_n.grid(row=1, column=2, sticky="w")

#Initial Height
inith = createOptionLabel(masterIn=glacpar_frame, textIn="Height (m): ", helpText="helpgrhght", rowIn=2, colIn=1)
inith_var = DoubleVar()
inith_var.set(0.0)
inith_n = Entry(master=glacpar_frame,textvariable=inith_var,width=7)
inith_n.config(state='disabled')
inith_n.grid(row=2, column=2, sticky="w")

#Minimum Snow Depth
mndph = createOptionLabel(masterIn=glacpar_frame, textIn="Threshold (m): ", helpText="helpgrthrshld", rowIn=3, colIn=1)
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
mdldynpar_frame.rowconfigure([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], minsize=20)

mdldynparam = Label(master=mdldynpar_frame,text="Model Dynamic Parameters")
mdldynparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Timestep
tmestp = createOptionLabel(masterIn=mdldynpar_frame, textIn="Timestep (min): ", helpText="helptimestep", rowIn=1, colIn=1)
tmestp_var = DoubleVar()
tmestp_var.set(45.0)
tmestp_n = Entry(master=mdldynpar_frame,textvariable=tmestp_var, width=7)
tmestp_n.grid(row=1, column=2, sticky="w")

#Runsteps
runstp = createOptionLabel(masterIn=mdldynpar_frame, textIn="Runsteps: ", helpText="helprunsteps", rowIn=2, colIn=1)
runstp_var = IntVar()
runstp_var.set(11520)
runstp_n = Entry(master=mdldynpar_frame,textvariable=runstp_var, width=7)
runstp_n.grid(row=2, column=2, sticky="w")

#Snapshots
snpsht = createOptionLabel(masterIn=mdldynpar_frame, textIn="Snapshots: ", helpText="helpsnapshots", rowIn=3, colIn=1)
snpsht_var = IntVar()
snpsht_var.set(0)
snpsht_n = Entry(master=mdldynpar_frame,textvariable=snpsht_var, width=7)
snpsht_n.grid(row=3, column=2, sticky="w")

#NSTPW
nsptw = createOptionLabel(masterIn=mdldynpar_frame, textIn="NSTPW: ", helpText="helpnstpw", rowIn=4, colIn=1)
nsptw_var = IntVar()
nsptw_var.set(160)
nsptw_n = Entry(master=mdldynpar_frame,textvariable=nsptw_var, width=7)
nsptw_n.grid(row=4, column=2, sticky="w")

#Restart File
restrtfle = createOptionLabel(masterIn=mdldynpar_frame, textIn="Restart File: ", helpText="helprestrtfle", rowIn=5, colIn=1)
restrtfle_var = StringVar()
restrtfle_var.set('')
restrtfle_n = Entry(master=mdldynpar_frame,textvariable=restrtfle_var, width=7)
restrtfle_n.config(state='disabled')
restrtfle_n.grid(row=5, column=2, sticky="w")
restrtfle_b = Button(master=mdldynpar_frame,text="...",command=rstrtfleget, width=3)
restrtfle_b.config(state='disabled')
restrtfle_b.grid(row=5, column=3, sticky="w")
restrtfletog_var = StringVar()
restrtfletog_var.set('False')
restrtfle_c = Checkbutton(master=mdldynpar_frame,variable=restrtfletog_var,command=rstrtfletoggle, onvalue='True', offvalue='False')
restrtfle_c.grid(row=5, column=4, sticky="w")

#Physics Filter 1
phyfilt1 = createOptionLabel(masterIn=mdldynpar_frame, textIn="Physics Filter: ", helpText="helphysfltr", rowIn=6, colIn=1)
phyfilt1_options = ["None", "None", "Cesaro", "Exp", "Lh"]

phyfilt1_var = StringVar()
phyfilt1_var.set(oceanzen_options[0])
phyfilt1_n = OptionMenu(mdldynpar_frame, phyfilt1_var, *phyfilt1_options)
phyfilt1_n.config(width=5)
phyfilt1_n.grid(row=6,column=2, sticky="w")

#Physics Filter 2
phyfilt2 = createOptionLabel(masterIn=mdldynpar_frame, textIn="Filter Application: ", helpText="helpfltrapp", rowIn=7, colIn=1)
phyfilt2_options = ["None", "None", "GP", "SP", "GP+SP"]

phyfilt2_var = StringVar()
phyfilt2_var.set(oceanzen_options[0])
phyfilt2_n = OptionMenu(mdldynpar_frame, phyfilt2_var, *phyfilt2_options)
phyfilt2_n.config(width=5)
phyfilt2_n.grid(row=7,column=2, sticky="w")

#Storm Climatology
stormcl = createOptionLabel(masterIn=mdldynpar_frame, textIn="Storm Climatology: ", helpText="helpstmclmtlgy", rowIn=8, colIn=1)
stormcltog_var = StringVar()
stormcltog_var.set('False')
stormcltog_n = Checkbutton(master=mdldynpar_frame,variable=stormcltog_var,command=stmtoggle, onvalue='True', offvalue='False')
stormcltog_n.grid(row=8, column=2, sticky="w")

#High Cadence
highcad = createOptionLabel(masterIn=mdldynpar_frame, textIn="High Cadence: ", helpText="helphghcdnce", rowIn=9, colIn=1)
highcadtog_var = StringVar()
highcadtog_var.set('False')
highcadtog_n = Checkbutton(master=mdldynpar_frame,variable=highcadtog_var, onvalue='True', offvalue='False')
highcadtog_n.config(state='disabled')
highcadtog_n.grid(row=9, column=2, sticky="w")

#Run To Balance
rntbal = createOptionLabel(masterIn=mdldynpar_frame, textIn="Run To Balance: ", helpText="helprntbal", rowIn=10, colIn=1)
rntbaltog_var = StringVar()
rntbaltog_var.set('False')
rntbaltog_n = Checkbutton(master=mdldynpar_frame,variable=rntbaltog_var,command=baltoggle, onvalue='True', offvalue='False')
rntbaltog_n.grid(row=10, column=2, sticky="w")

#Run Time
runtme = createOptionLabel(masterIn=mdldynpar_frame, textIn="Run Time (years): ", helpText="helprntme", rowIn=11, colIn=1)
runtme_var = IntVar()
runtme_var.set(100)
runtme_n = Entry(master=mdldynpar_frame,textvariable=runtme_var, width=7)
runtme_n.grid(row=11, column=2, sticky="w")

#Threshold
trshld = createOptionLabel(masterIn=mdldynpar_frame, textIn="Threshold: ", helpText="helpthrshld", rowIn=12, colIn=1)
trshld_var = DoubleVar()
trshld_var.set(0.0005)
trshld_n = Entry(master=mdldynpar_frame,textvariable=trshld_var, width=7)
trshld_n.config(state='disabled')
trshld_n.grid(row=12, column=2, sticky="w")

#Baseline
bselne = createOptionLabel(masterIn=mdldynpar_frame, textIn="Baseline (years): ", helpText="helpbslne", rowIn=13, colIn=1)
bselne_var = IntVar()
bselne_var.set(10)
bselne_n = Entry(master=mdldynpar_frame,textvariable=bselne_var, width=7)
bselne_n.config(state='disabled')
bselne_n.grid(row=13, column=2, sticky="w")

#Max Years
maxyr = createOptionLabel(masterIn=mdldynpar_frame, textIn="Max. Year (years): ", helpText="helpmxyr", rowIn=14, colIn=1)
maxyr_var = IntVar()
maxyr_var.set(100)
maxyr_n = Entry(master=mdldynpar_frame,textvariable=maxyr_var, width=7)
maxyr_n.config(state='disabled')
maxyr_n.grid(row=14, column=2, sticky="w")

#Min Years
minyr = createOptionLabel(masterIn=mdldynpar_frame, textIn="Min. Year (years): ", helpText="helpmnyr", rowIn=15, colIn=1)
minyr_var = IntVar()
minyr_var.set(10)
minyr_n = Entry(master=mdldynpar_frame,textvariable=minyr_var, width=7)
minyr_n.config(state='disabled')
minyr_n.grid(row=15, column=2, sticky="w")

#Crash If Broken
cshibrk = createOptionLabel(masterIn=mdldynpar_frame, textIn="Crash if Broken: ", helpText="helpcrshibrkn", rowIn=16, colIn=1)
cshibrktog_var = StringVar()
cshibrktog_var.set('False')
cshibrktog_n = Checkbutton(master=mdldynpar_frame,variable=cshibrktog_var, onvalue='True', offvalue='False')
cshibrktog_n.grid(row=16, column=2, sticky="w")

#Clean
clean = createOptionLabel(masterIn=mdldynpar_frame, textIn="Clean: ", helpText="helpcln", rowIn=17, colIn=1)
cleantog_var = StringVar()
cleantog_var.set('False')
cleantog_n = Checkbutton(master=mdldynpar_frame,variable=cleantog_var, onvalue='True', offvalue='False')
cleantog_n.grid(row=17, column=2, sticky="w")

#All Years
allyrs = createOptionLabel(masterIn=mdldynpar_frame, textIn="All Years: ", helpText="helpalrstrts", rowIn=18, colIn=1)
allyrstog_var = StringVar()
allyrstog_var.set('False')
allyrstog_n = Checkbutton(master=mdldynpar_frame,variable=allyrstog_var, onvalue='True', offvalue='False')
allyrstog_n.grid(row=18, column=2, sticky="w")

#Keep Restarts
kprsts = createOptionLabel(masterIn=mdldynpar_frame, textIn="Keep Restarts: ", helpText="helpkprstrts", rowIn=19, colIn=1)
kprststog_var = StringVar()
kprststog_var.set('False')
kprststog_n = Checkbutton(master=mdldynpar_frame,variable=kprststog_var, onvalue='True', offvalue='False')
kprststog_n.grid(row=19, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#Check
compat = Label(text="Compatability")
compat.grid(row=2, column=3, sticky="s")
sys_check = Button(text="Compatability Check", command=system_check)
sys_check.grid(row=3, column=3, sticky="n")

#Load INI
compat = Label(text="Import Parameters")
compat.grid(row=2, column=5, sticky="s")
sys_check = Button(text="Load INI", command=load_ini)
sys_check.grid(row=3, column=5, sticky="n")

#Export INI
compat = Label(text="Export Parameters")
compat.grid(row=2, column=7, sticky="s")
sys_check = Button(text="Export INI", command=save_ini)
sys_check.grid(row=3, column=7, sticky="n")

#Save
output = Label(text="Output")
output.grid(row=2, column=9, sticky="s")
save = Button(text="Save", command=save_file)
save.grid(row=3, column=9, sticky="n")

#Status
statusContainer = LabelFrame(relief=GROOVE, borderwidth=3, text="Status")
statusContainer.grid(padx=10, pady=10, row=4, column=1, rowspan=3, columnspan=9, sticky="new")
statusContainer.rowconfigure(0, weight=1)
statusContainer.columnconfigure(0, weight=1)

statusBox = Text(master=statusContainer, height=8)
statusBox.configure(font=help_font)
statusBox.grid(padx=3, pady=3, row=0, column=0,sticky="nsew")

window.mainloop()
