

def calcOverscan(oScan=1.1,
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

    oXres = xRes * oScan
    oYres = yRes * oScan

    rX = round(oXres)
    rY = round(oYres)

    if rX % 2 == 1:
        rX += 1.0

    if rY % 2 == 1:
        rY += 1.0

    xScale = rX/xRes
    yScale = rY/yRes

    oXAper = xAper * xScale
    oYAper = yAper * yScale

    return [int(rX), int(rY)], [oXAper, oYAper]

if __name__ == '__main__':
    res, aper = calcOverscan(oScan=1.1,
                             xRes=2048,
                             yRes=1080,
                             xAper=0.9449244,
                             yAper=0.4982999)

    print(res, aper)
