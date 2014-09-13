from decimal import Decimal

def calculateOverscan(oScan=1.1,
                 xRes=2048,
                 yRes=1080,
                 xAper=0.9449244,
                 yAper=0.4982999):
    '''
    Calculates a proper overscan resolution
    and aperture for an overscan amount.

    @param xRes - The value of the resolution width.
    @param yRes - The value of the resolution height.
    @param xAper - The Horizontal Aperture of the camera.
    @param yAper - The Vertical Aperture of the camera.
    @param oScan - The scalar overscan amount. (ex. 1.1 = 10%)

    Returns:
        (list of ints): Overscan Resolution X and Y
        (list of floats): Horizontal and Vertical Aperture

    Example:
        res, aper = calcOverscan(oScan=1.1,
                                 xRes=2048,
                                 yRes=1080,
                                 xAper=0.9449244,
                                 yAper=0.4982999)

    Raises:
        ValueError: If the oScan is equal to or less than 1.0.
    '''
    if oScan <= 1.000:
        raise ValueError("Overscan value is equal to or less than 1.0")

    #Coverting values for decimal.
    dec_OScan = Decimal(str(oScan))
    dec_xRes = Decimal(str(xRes))
    dec_yRes = Decimal(str(yRes))

    #Calculate overscan res.
    oXres = dec_xRes * dec_OScan
    oYres = dec_yRes * dec_OScan

    #Round to int.
    resX = round(oXres)
    resY = round(oYres)

    #Make sure it's even on X.
    if resX % 2 == 1:
        resX += 1.0

    #Make sure it's even on Y.
    if resY % 2 == 1:
        resY += 1.0

    #Find x and y scale values.
    xScale = Decimal(str(resX))/dec_xRes
    yScale = Decimal(str(resY))/dec_yRes

    #Calculate aperture.
    oXAper = Decimal(str(xAper)) * Decimal(str(xScale))
    oYAper = Decimal(str(yAper)) * Decimal(str(yScale))

    return [int(resX), int(resY)], [float(oXAper), float(oYAper)]

if __name__ == '__main__':
    res, aper = calculateOverscan(oScan=1.1,
                                  xRes=2048,
                                  yRes=1080,
                                  xAper=0.9449244,
                                  yAper=0.4982999)

    print(res, aper)
