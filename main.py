import pandas as pd
import exiv2
import os

# CONSTANTS
EXIFTAGS = ('make', 'model', 'dateTimeOriginal', 'exposureTime',
                 'apertureValue', 'exposureBiasValue', 'exposureIndex', 'flash',
                 'flashBias', 'flashEnergy', 'focalLength', 'subjectDistance',
                 'isoSpeed', 'exposureMode', 'meteringMode', 'macroMode',
                 'imageQuality', 'whiteBalance', 'orientation', 'sceneMode',
                 'sceneCaptureType', 'lensName', 'saturation', 'sharpness',
                 'contrast', 'fNumber', 'serialNumber', 'afPoint',
                 'shutterSpeedValue', 'brightnessValue', 'maxApertureValue',
                 'lightSource', 'subjectArea', 'sensingMethod')

# METHODS  
def readFileMetadata(fp, df, p=True): # reads exif data from image from a filepath, fp and appends to a dataframe, df; will print read exif data with flag p by default
     
    img = exiv2.ImageFactory.open(fp)
    img.readMetadata()
    exifData = img.exifData()
    
    data = {}
    strbuild = '*'*15 + '\n'
    
    for name in EXIFTAGS:
        if hasattr(exiv2, name): 
            datum = getattr(exiv2, name)(exifData)
            if datum:
                strbuild += '{:18s}: {:30s}: {:s}'.format(
                    name, datum.key(), datum.print(exifData)) + '\n'   
                data.update({name : datum.print(exifData)})
            
    strbuild += '*'*15 + '\n'
    df.loc[len(df)] = data
    if p: print(strbuild)

    return 0

def readFolder(folder):
    for file in os.listdir(folder):
        img = os.path.join(folder, file)
        if os.path.isfile(img):
            readFileMetadata(img, testdf, p=False)
    return 0


# # TEST FILES WITH FUJI AND NIKON RAWS
# fuji = r'C:\Users\Saber\OneDrive\Pictures\2024\2024-07-07\DSCF0429.RAF'
# nikon = r'C:\Users\Saber\OneDrive\Pictures\raws\2024\2024-04-08\DSC_9423.NEF'

# df = pd.DataFrame(columns=EXIFTAGS)
# readFileMetadata(fuji, df)
# readFileMetadata(nikon, df)
# print(df)


# PLACEHOLDER FOR FRONT END INTEGRATION
folder = r'C:\Users\Saber\OneDrive\Desktop\Night Market 2024 raws\nm\nm2'
testdf = pd.DataFrame(columns=EXIFTAGS)

readFolder(folder)
print(testdf)
