import os
from os import path
import numpy as np
from matplotlib.image import imread
from PIL import Image, ImageOps

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

#               string,   string  float boolean     boolean         integer     float        float  String, see dict String
def convert_sra(filepath, infile, grav, debug_img, desert_planet, floor_value, peak_value, trench_value, resotext, sra_name):


    #Image setup
    print("Beginning Image -> SRA Conversion...")
    sra_path = path.dirname(filepath)+'/'
    
    if debug_img:
        print("Debug Images Enabled...")
    
    red_img = imread(infile)[:,:,0]             #opens red channel
    green_img = imread(infile)[:,:,1]           #opens green channel
    blue_img = imread(infile)[:,:,2]            #opens blue channel
    grey_img = (red_img+green_img+blue_img)/3   #averages color channels and scales from 0-1

    img_width = len(grey_img[0])                #finds image width
    img_height = len(grey_img)                  #finds image height
    img_rgb = []

    #altitude ranges
    if not desert_planet:
        greyscale_img = grey_img*255                #converts 0-1 to 0-255
        max_img = 255-(floor_value)                 #max value lowered by floor value
        rescaled_img = (greyscale_img-(floor_value))#array lowered by floor value
        rescaled_img[rescaled_img <= 0] = 0         #any negative value becomes 0 (ocean)
        rescaled_img = (rescaled_img/max_img)*peak_value*grav #array converted to 0-1, before multiplied by max height and gravity (geopotential)
        if debug_img:
            color_ocean(rescaled_img, img_rgb, img_width, img_height)
    else:
        range_value = peak_value-trench_value
        rescaled_img = ((grey_img*range_value)-trench_value)*grav #converts 0-1 to trench-peak times gravity (geopotential)
        color_land(rescaled_img, img_rgb, img_width, img_height)

    min = float(np.min(rescaled_img))           #finds the min height (should be near deepest depth)
    max = float(np.max(rescaled_img))           #finds the max height (should be near absolute max height)

    #Debug image 1 generation
    if debug_img:
        img = Image.new('RGB',(img_height,img_width))   #print original image
        img.putdata(img_rgb)
        img = img.transpose(Image.ROTATE_90)
        img = ImageOps.flip(img)
        img.save(sra_path+"LandMaskOriginal.png")
        print("Debug Image 1 printed...")

    #Image rescaling
    options = {"T21": 32,"T42": 64,"T63": 96,"T85": 128,"T106": 160,"T127": 192,"T170": 256}
    if resotext in options:
        height = options[resotext]
        width = 2*height

    scale_width = img_width/width               #finds the ratio between starting and final width
    scale_height = img_height/height            #finds the ratio between starting and final height

    print("Width ratio: "+str(scale_width))
    print("Height ratio: "+str(scale_height))

    #tests to see whether original image is a multiple of desired resolution, before splitting the array into chunks if it is
    if scale_width == round(scale_width):
        if scale_height == round(scale_height):

            width_ratio = int(scale_width)          #width ratio between original and resized image
            height_ratio = int(scale_height)        #height ratio between original and resized image
            chunked = chunk(rescaled_img, height_ratio, width_ratio) #splits the geopotential array into a 3d array
            length_ratio = len(chunked)             #finds the length of the 3d array
            print("All ratios are good!")
        else:
            print("Height ratio incompatible, please try to have the image resolution as a multiple of the output resolution.")
    else:
        print("Width ratio incompatible, please try to have the image resolution as a multiple of the output resolution.")

    img_rgb = []
    if not desert_planet:
        b_w = chunked.copy()[:,:,:]                 #new empty 3d array, avoids overriding original array!
        for x in range(length_ratio):
            for y in range(width_ratio):
                for z in range(height_ratio):
                    checker = chunked[x,y,z]
                    if checker > 0:                 #converts 3d geopotential array to 3d land mask array
                        b_w[x,y,z] = 1
                    else:
                        b_w[x,y,z] = 0

        b_w = b_w.mean(axis=(1,2))                  #averages land mask array into 1d list
        dechunked = chunked.mean(axis=(1,2))        #simpler approach, since there's no ocean there's no need to check for it, so just average all the land to 1d list
        dechunked = np.reshape(dechunked, (height, width)) #reshapes list to equirectangular 2d array
        b_w = np.reshape(b_w, (height, width))
        color_ocean(b_w, img_rgb, width, height)    #converts to land mask

    else:
        #simpler approach, since there's no ocean there's no need to check for it, so just average all the land to 1d list
        dechunked = chunked.mean(axis=(1,2))    
        dechunked = np.reshape(dechunked, (height, width)) #reshapes list to equirectangular 2d array
        b_w = dechunked + 1
        color_land(dechunked, img_rgb, width, height) #converts to land mask

    if debug_img:
        img = Image.new('RGB',(height,width))   #print resized image
        img.putdata(img_rgb)
        img = img.transpose(Image.ROTATE_90)
        img = ImageOps.flip(img)
        img.save(sra_path+"LandMaskSmall.png")
        print("Debug Image 2 printed...")

    list_image = dechunked.flatten()            #Flattens 2d array into list
    b_w = b_w.flatten()
    sra_129 = np.array(list_image).reshape(-1, 8) #Rearranges list into 2d array that matches sra format
    sra_172 = np.array(b_w).reshape(-1, 8)

    if desert_planet:
        sra_172[:,:] = 1                            #Everything becomes land

    fl_height = float(height)                       #Apparently it doesn't like integers
    fl_width = float(width)
    sra_final_path = sra_path+'SRA/'
    writeSRA(sra_final_path,sra_name,172,sra_172,fl_height,fl_width)
    writeSRA(sra_final_path,sra_name,129,sra_129,fl_height,fl_width)
    print("Conversion successful!") #Nice!
    print("Formatting...")
    landmaptext = 'landmap="SRA/'+sra_name+'_surf_0172.sra",'
    topomaptext = 'topomap="SRA/'+sra_name+'_surf_0129.sra",'
