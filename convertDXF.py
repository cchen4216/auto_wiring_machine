##  GridDXF.py Version 1.02
##  Copyright (c) 2006 Bruce Vaughan, BV Detailing & Design, Inc.
##  All rights reserved.
##  NOT FOR SALE. The software is provided "as is" without any warranty.
########################################################################
'''
parseDXFpts(file_name) - 'file_name' is the name of the DXF file to parse.
                         The function returns a list of lines and a list of circles.
                         All other entities are ignored.
                         Each element of the line list (ptList) is a list of the x, y, z values of the two end points.
                         Each element of the circle list (cirList) is a list of the x, y, z value of the end point and the radius.
 
formatDXFpts(ptList, cirList) - Returns a formatted string suitable for file method 'write()'.
                                The strings are formatted to be compatible with parametric GridLayout version 1.03 and greater.
 
Example usage:
    file_name = r'C:\SDS2_7.0\macro\New Versions\Ref\grids.dxf'
    gridFile = r'C:\SDS2_7.0\macro\New Versions\Ref\grid_test.txt'
    f = open(gridFile, 'w')
    f.write(formatDXFpts(*(parseDXFpts(file_name))))
    f.close()
 
Version 1.00 (5/8/07)
Version 1.01 (5/9/07) -     Skip until ENTITIES section using f.next()
                            Remove unnecessary variable assignments
Version 1.02 (5/10/07) -    Use dict.fromkeys() and f.next() to compile entity data
'''
def parseDXFpts(fn):
    f = open(fn)
 
    # skip to entities section
    s = f.next()
    while s.strip() != 'ENTITIES':
        s = f.next()
 
    inLine = False
    inCircle = False
 
    ptList = []
    cirList = []
 
    for line in f:
        line = line.strip()
        # In ENTITIES section, iteration can cease when ENDSEC is reached
        if line == 'ENDSEC':
            break
 
        elif inLine == True:
            dd = dict.fromkeys(['10','20','30','11','21','31'], 0.0)
            while line != '0':
                if line in dd:
                    dd[line] = f.next().strip()
                line = f.next().strip()
            ptList.append([[dd['10'], dd['20'], dd['30']], [dd['11'], dd['21'], dd['31']]])
            inLine = False
 
        elif inCircle == True:
            dd = dict.fromkeys(['10','20','30','40'], 0.0)
            while line != '0':
                if line in dd:
                    dd[line] = f.next().strip()
                line = f.next().strip()
            cirList.append([[dd['10'], dd['20'], dd['30']], dd['40']])
            inCircle = False
 
        else:
            if line == 'LINE':
                inLine = True
            elif line == 'CIRCLE' or line == 'ARC':
                inCircle = True
 
    f.close()
 
    return ptList, cirList
 
# base must be a tuple or list, not a Point object
def formatDXFpts(ptList, cirList, base=False):
    outList = []
    for pt1, pt2 in ptList:
        if base:
            pt1 = map(str, [i+j for i,j in zip(map(float, pt1), base)])
            pt2 = map(str, [i+j for i,j in zip(map(float, pt2), base)])
        # ExplicitL: 20-0, 20-0, 20-0 : 40-0, 40-0, 40-0
        outList.append('ExplicitL: %s : %s' % (', '.join(pt1), ', '.join(pt2)))
    for pt1, rad in cirList:
        if base:
            pt1 = map(str, [i+j for i,j in zip(map(float, pt1), base)])
        # ExplicitR: 20-0, 20-0, 20-0 : 15-0    
        outList.append('ExplicitR: %s : %s' % (', '.join(pt1), rad))
    return '\n'.join(outList)
 
if __name__ == '__main__':
 
    fn = r'C:\SDS2_7.0\macro\New Versions\Ref\grids2.dxf'
    gridStr = formatDXFpts(base=(0.0, -2000.0, -2000.0),*(parseDXFpts(fn)))
    print gridStr
    '''
    file_name = r'C:\SDS2_7.0\macro\New Versions\Ref\grids.dxf'
    gridFile = r'C:\SDS2_7.0\macro\New Versions\Ref\grid_test.txt'
    f = open(gridFile, 'w')
    f.write(formatDXFpts(*(parseDXFpts(file_name))))
    f.close()
    '''
 
'''
ExplicitL: 9816.68821752379, 9342.150641757189, 0.0 : 5891.694641987371, 7589.498197195453, 0.0
ExplicitL: 13837.65104243732, 8933.988514331103, 0.0 : 14456.10878705126, 5947.569025541323, 0.0
ExplicitL: 13863.97763099647, 8944.937937731237, 0.0 : 14483.88419985993, 5951.522341265071, 0.0
ExplicitL: 15455.83326287129, 6340.472643957712, 0.0 : 14921.10765265826, 6149.932906111864, 0.0
ExplicitL: 16488.77763008338, 6904.236993653539, 0.0 : 15978.35671679392, 6590.049547387251, 0.0
ExplicitL: 3966.563802256045, 10246.06975532415, 0.0 : 18100.41385149004, 10246.06975532415, 0.0
ExplicitR: 16534.87751064366, 4916.545768317483, 0.0 : 380.8099725875799
ExplicitR: 17010.88992108956, 14650.96205330669, 0.0 : 299.1021903913424
>>>
'''