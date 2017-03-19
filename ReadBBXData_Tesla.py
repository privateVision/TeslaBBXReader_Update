#!/usr/bin/env python
# coding utf-8
import sys,os,calendar,datetime,time,linecache

#collect current directory
def cur_file_dir():
    path=os.path.split(os.path.realpath(__file__))[0]
    #path=sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def BBXPrint(i):
    file1=os.path.join(cur_file_dir(),'result.log')
    f1=open(file1,'a+')

    if i==0:
        f1.write('=============BBX Data=============')
        f1.write('\n')
        f1.write('=============gpu0=============')
        f1.write('\n')
    elif i==1:
        f1.write('\n')
        f1.write('=============gpu1=============')
        f1.write('\n')

    f1.close()
    return "Print BBX successfully"

# PN#
def PN():
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')

    #For PN#
    for Line0 in f1:
        if ': 900' in Line0:
            #the location of *032*
            loc=Line0.index(': 900')
            #print(loc)

            f2.write('PN:')
            f2.write(Line0[(loc+2):(loc+20)]) #collect the current PN location between 'loc+2' and 'loc+20'
            f2.write('\n')
            break
    
    f1.close()
    f2.close()
    return "Collect PN# successfully"            

# SN#
def SN():
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')

    #For SN
    for Line1 in f1:
        if ': 032' in Line1:
            #the location of *032*
            loc=Line1.index(': 032')
            #print(loc)

            f2.write('SN:')
            f2.write(Line1[(loc+2):(loc+15)]) #collect the current SN location between 'loc+2' and 'loc+15'
            f2.write('\n')
            break
    
    f1.close()
    f2.close()
    return "Collect SN# successfully"

#SKU
def SKU():
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')

    for Line1 in f1:
        if 'Project        :' in Line1:
            f2.write('SKU:')
            f2.write(Line1[16:27])
            f2.write('\n')
            break

    f1.close()
    f2.close()
    return "Collect SKU# successfully"

# ECC mode
def ECC(a):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    #1st GPU
    if a==0:
        for Line1 in f1:
            if 'ECC    ' in Line1:
                if Line1[17:25]=='Disabled':
                    f2.write('ECC Mode:')
                    f2.write(Line1[17:25])
                    f2.write('\n')
                    break
            else:
                pass
    elif a==1:
        for Line2 in f3:
            if 'ECC    ' in Line2:
                if Line2[45:53]=='Disabled':
                    f2.write('ECC Mode:')
                    f2.write(Line2[45:53])
                    f2.write('\n')
                    break
            else:
                pass
    
    f1.close()
    f2.close()
    return 'Collect ECC mode successfully'

#InfoRom BBX Data location:
def BBXDataLoc(b):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    f2 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    i=0
    j=0
    InfoRomBBXDataLoc=0
    #1st GPU
    if b==0:
        for Line1 in f1:
            i=i+1
            if 'InfoRom Data (GPU 0:0):'in Line1:
                InfoRomBBXDataLoc=i
                break

    elif b==1:
        for Line3 in f2:
            j=j+1
            if 'InfoRom Data (GPU 1:0):' in Line3:
                InfoRomBBXDataLoc=j
                break

    f1.close()
    f2.close()
    return InfoRomBBXDataLoc

#Mods Version
def Mods():
    for root, dirs, files in os.walk(cur_file_dir()):
        if files[1] == 'ReadBBXData_Tesla.py' and files[0]=='BBXDataBuffer.log' :
            # merge(join) path and file
            file1 = os.path.join(cur_file_dir(), files[3])
            f1 = open(file1, 'r', encoding='UTF-8', errors='ignore')
            file2 = os.path.join(cur_file_dir(), 'result.log')
            f2=open(file2,'a+')

        elif files[2] == 'ReadBBXData_Tesla.py' and files[0]=='BBXDataBuffer.log' :
            # merge(join) path and file
            file1 = os.path.join(cur_file_dir(), files[1])
            f1 = open(file1, 'r', encoding='UTF-8', errors='ignore')
            file2 = os.path.join(cur_file_dir(), 'result.log')
            f2=open(file2,'a+')
        else:
            file1 = os.path.join(cur_file_dir(), files[0])
            f1 = open(file1, 'r', encoding='UTF-8', errors='ignore')
            file2 = os.path.join(cur_file_dir(), 'result.log')
            f2=open(file2,'a+')

    for Line1 in f1:
        if 'MODS           :' in Line1:
            f2.write('Mods:')
            f2.write(Line1[-7:-1])
            f2.write('\n')
            break

    f1.close()
    f2.close()
    return "Collect Mods successfully"

#Vendor of Memory
def MemVendor(c):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f4 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    i=0
    for Line1 in f1:
        if 'Memory Man.' in Line1:
            f2.write('Memory Man. :')
            f2.write(Line1[20:-1])
            f2.write('\n')
            break
    #One GPU
    if c==3:
        for Line2 in f3:
            if 'HBM Info' in Line2:
                f2.write('HBM Info :')
                f2.write(Line2[17:-1])
                f2.write('\n')
                break
    #Two GPU
    elif c==1:
        for Line3 in f4:
            i=i+1
            if 'HBM Info' in Line3:
                HBMInfoLen=int(len(Line3)-(len(Line3)-16)/2)
                HBMInfo=linecache.getline(file1, i)[17:HBMInfoLen]
                f2.write('HBM Info :')
                f2.write(HBMInfo)
                f2.write('\n')
                break


    f1.close()
    f2.close()
    f3.close()
    f4.close()
    return "Collect MemVendor successfully"

#Memory Part ID
def MemPN():
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')

    for Line1 in f1:
        if 'Memory Part ID' in Line1:
            f2.write('Memory Part ID:')
            f2.write(Line1[21:-1])
            f2.write('\n')
            break

    f1.close()
    f2.close()
    return "Collect Memory Part ID# successfully"

#Show Field Time
def FieldTime(j):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3=open(file1, 'r', encoding='UTF-8', errors='ignore')
    f4=open(file1, 'r', encoding='UTF-8', errors='ignore')
    f5=open(file1, 'r', encoding='UTF-8', errors='ignore')

    a=0
    b=0
    c=0
    d=0
    # 1st GPU
    if j==0:
        for Line1 in f1:
            a=a+1
            if 'First Time' in Line1:
                FirstTimeLoc_1stG=a
                if BBXDataLoc(0)<FirstTimeLoc_1stG<BBXDataLoc(1):
                    loc1 = Line1.index('First Time')
                    f2.write('First Time BBX updated:')
                    f2.write(Line1[(loc1 + 36):(loc1 + 56)])
                    f2.write('\n')
                    break

        for Line2 in f3:
            d=d+1
            if 'Last Time' in Line2:
                LastTimeLoc_1stG=d
                if BBXDataLoc(0) < FirstTimeLoc_1stG < BBXDataLoc(1):
                    loc2 = Line2.index('Last Time')
                    f2.write('Last Time BBX updated:')
                    f2.write(Line2[(loc2 + 36):(loc2 + 56)])
                    f2.write('\n')
                    break

    # 2nd GPU
    if j==1:
        for Line3 in f4:
            b=b+1
            if 'First Time' in Line3:
                FirstTimeLoc_2ndG=b
                if FirstTimeLoc_2ndG>BBXDataLoc(1):
                    loc3 = Line3.index('First Time')
                    f2.write('First Time BBX updated:')
                    f2.write(Line3[(loc3 + 36):(loc3 + 56)])
                    f2.write('\n')
                    break

        for Line4 in f5:
            c=c+1
            if 'Last Time BBX was updated' in Line4:
                LastTimeLoc_2ndG=c
                if LastTimeLoc_2ndG>BBXDataLoc(1):
                    loc4 = Line4.index('Last Time')
                    f2.write('Last Time BBX updated:')
                    f2.write(Line4[(loc4 + 36):(loc4 + 56)])
                    f2.write('\n')
                    break
    #One GPU
    if j==3:
        for Line1 in f1:
            a=a+1
            if 'First Time' in Line1:
                FirstTimeLoc_1stG=a
                if BBXDataLoc(0)<FirstTimeLoc_1stG<BBXDataLoc(0)+1000:
                    loc1 = Line1.index('First Time')
                    f2.write('First Time BBX updated:')
                    f2.write(Line1[(loc1 + 36):(loc1 + 56)])
                    f2.write('\n')
                    break

        for Line2 in f3:
            d=d+1
            if 'Last Time' in Line2:
                LastTimeLoc_1stG=d
                if BBXDataLoc(0) < FirstTimeLoc_1stG < BBXDataLoc(0) + 1000:
                    loc2 = Line2.index('Last Time')
                    f2.write('Last Time BBX updated:')
                    f2.write(Line2[(loc2 + 36):(loc2 + 56)])
                    f2.write('\n')
                    break

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

    return 'Field Time Show'

#Calculate Field Time
def CalculateFieldTime(m):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3=open(file1, 'r', encoding='UTF-8', errors='ignore')
    f4=open(file1, 'r', encoding='UTF-8', errors='ignore')
    f5=open(file1, 'r', encoding='UTF-8', errors='ignore')
    f6 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f7 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    a=0#1st GPU First time Location
    b=0#2nd GPU First time location
    k=0

    #1st GPU Field Time calculate
    if m==0:
        #Calculate BBX Time
        for Line1 in f1:
            a=a+1
            if 'First Time' in Line1:
                FirstTimeLoc_1stG=a
                loc1=Line1.index('First Time')
                date1=datetime.datetime.strptime(Line1[(loc1 + 36):(loc1 + 56)], '%Y-%m-%d, %H:%M:%S')
                break
        for Line2 in f3:
            if 'Last Time' in Line2:
                loc2 = Line2.index('Last Time')
                date2 = datetime.datetime.strptime(Line2[(loc2 + 36):(loc2 + 56)], '%Y-%m-%d, %H:%M:%S')
                break
        for Line3 in f4:
            if 'Total time GPU was running' in Line3:
                loc3 = Line3.index('Total time GPU was running')
                date3 = Line3[(loc3 + 36):-1]  # 1st GPU Total time
                break

        delta1=date2-date1 #field time delta
        if date1==date2 :
            pass
        elif BBXDataLoc(0)<FirstTimeLoc_1stG<BBXDataLoc(1):
            now_date = datetime.datetime.now() # the Days' number of February
            now_year = now_date.year
            num_feb = calendar.monthrange(now_year, 2)[1]

            # Field time
            time1stG_1 = delta1.days  # 1st GPU total field days
            time1stG_2 = delta1.seconds
            time1stG_3 = time1stG_2 / 86400  # translate seconds to days
            time1stG_4 = time1stG_1 * 86400 + time1stG_2  # 1st GPU All time translate to seconds

            #All field days
            time1stG_5=time1stG_1+time1stG_3

            # field year
            if num_feb == 28:
                year1stG = int(time1stG_1 / 365)
            if num_feb == 29:
                year1stG = int(time1stG_1 / 366)

            # field days
            if num_feb == 28:
                days1stG = time1stG_1 - 365 * year1stG + time1stG_3
            elif num_feb == 29:
                days1stG = time1stG_1 - 366 * year1stG + time1stG_3

            # field Hour Min Seconds
            HMS1stG = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(time1stG_2))  # hour/min/second

            # GPU All running time
            ART1 = int(date3)

            # GPU All running year/days/hour min seconds
            if num_feb == 28:
                # year
                ARY1 = int(ART1 / (365 * 24 * 3600))

                # days
                ARD1 = int((ART1 - 365 * 24 * 3600 * ARY1) / (24 * 3600))

                # Hour Min Second
                ARHMS1 = int(ART1 - 365 * 24 * 3600 * ARY1 - 24 * 3600 * ARD1)
                ARHMS11 = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(ARHMS1))

            if num_feb == 29:
                ARY1 = int(ART1 / (366 * 24 * 3600))

                # days
                ARD1 = int((ART1 - 366 * 24 * 3600 * ARY1) / (24 * 3600))

                # Hour Min Second
                ARHMS1 = int(ART1 - 366 * 24 * 3600 * ARY1 - 24 * 3600 * ARD1)
                ARHMS11 = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(ARHMS1))

            # GPU All Running operation days
            ODays1 = (ART1 / (24 * 3600))
            # dutyCycle
            dutyCycle1 = (ART1 / time1stG_4) * 100

            # write field time
            f2.write('Field Time: %.3f days' % time1stG_5)
            f2.write('(%dyear, %ddays %s)\n' % (year1stG, days1stG, HMS1stG))
            f2.write('Total Time: %d seconds' % (ART1))
            f2.write('(%dyear, %ddays %s)\n' % (ARY1, ARD1, ARHMS11))
            f2.write('Operation Day=%.3f Days\n' % ODays1)
            f2.write('DutyCycle=%.1f%%\n' % dutyCycle1)

    #2nd GPU Field Time calculate
    elif m==1:
        for Line4 in f5:
            b=b+1
            if 'First Time' in Line4:
                FirstTimeLoc_2ndG=b
                if k==0:
                    k=1
                else:
                    loc4 = Line4.index('First Time')
                    date3 = datetime.datetime.strptime(Line4[(loc4 + 36):(loc4 + 56)], '%Y-%m-%d, %H:%M:%S')
                    break

        for Line5 in f6:
            if 'Last Time' in Line5:
                if k==1:
                    k=2
                else:
                    loc5 = Line5.index('Last Time')
                    date4 = datetime.datetime.strptime(Line5[(loc5 + 36):(loc5 + 56)], '%Y-%m-%d, %H:%M:%S')
                    break

        for Line6 in f7:
            if 'Total time GPU was running' in Line6:
                if k==2:
                    k=3
                else:
                    loc6 = Line6.index('Total time GPU was running')
                    date5 = Line6[(loc6 + 36):-1]  # 2nd GPU Total time
                    break

        delta2=date4-date3 #field time delta
        if date3==date4 :
            pass
        elif FirstTimeLoc_2ndG>BBXDataLoc(1):
            now_date = datetime.datetime.now() # the Days' number of February
            now_year = now_date.year
            num_feb = calendar.monthrange(now_year, 2)[1]

            # Field time
            time2ndG_1 = delta2.days  # 1st GPU total field days
            time2ndG_2 = delta2.seconds
            time2ndG_3 = time2ndG_2 / 86400  # translate seconds to days
            time2ndG_4 = time2ndG_1 * 86400 + time2ndG_2  # 1st GPU All time translate to seconds

            #All field days
            time2ndG_5=time2ndG_1+time2ndG_3

            # field year
            if num_feb == 28:
                year2ndG = int(time2ndG_1 / 365)
            if num_feb == 29:
                year2ndG = int(time2ndG_1 / 366)

            # field days
            if num_feb == 28:
                days2ndG = time2ndG_1 - 365 * year2ndG + time2ndG_3
            elif num_feb == 29:
                days2ndG = time2ndG_1 - 366 * year2ndG + time2ndG_3

            # field Hour Min Seconds
            HMS2ndG = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(time2ndG_2))  # hour/min/second

            # GPU All running time
            ART2 = int(date5)

            # GPU All running year/days/hour min seconds
            if num_feb == 28:
                # year
                ARY2 = int(ART2 / (365 * 24 * 3600))

                # days
                ARD2 = int((ART2 - 365 * 24 * 3600 * ARY2) / (24 * 3600))

                # Hour Min Second
                ARHMS2 = int(ART2 - 365 * 24 * 3600 * ARY2 - 24 * 3600 * ARD2)
                ARHMS22 = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(ARHMS2))

            if num_feb == 29:
                ARY2 = int(ART2 / (366 * 24 * 3600))

                # days
                ARD2 = int((ART2 - 366 * 24 * 3600 * ARY2) / (24 * 3600))

                # Hour Min Second
                ARHMS2 = int(ART2 - 366 * 24 * 3600 * ARY2 - 24 * 3600 * ARD2)
                ARHMS22 = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(ARHMS2))

            # GPU All Running operation days
            ODays2 = (ART2 / (24 * 3600))
            # dutyCycle
            dutyCycle2 = (ART2 / time2ndG_4) * 100

            # write field time
            f2.write('Field Time: %.3f days' % time2ndG_5)
            f2.write('(%dyear, %ddays %s)\n' % (year2ndG, days2ndG, HMS2ndG))
            f2.write('Total Time: %d seconds' % (ART2))
            f2.write('(%dyear, %ddays %s)\n' % (ARY2, ARD2, ARHMS22))
            f2.write('Operation Day=%.3f Days\n' % ODays2)
            f2.write('DutyCycle=%.1f%%\n' % dutyCycle2)

    #One GPU Field Time calculate
    if m==3:
        #Calculate BBX Time
        for Line1 in f1:
            a=a+1
            if 'First Time' in Line1:
                FirstTimeLoc_1stG=a
                loc1=Line1.index('First Time')
                date1=datetime.datetime.strptime(Line1[(loc1 + 36):(loc1 + 56)], '%Y-%m-%d, %H:%M:%S')
                break
        for Line2 in f3:
            if 'Last Time' in Line2:
                loc2 = Line2.index('Last Time')
                date2 = datetime.datetime.strptime(Line2[(loc2 + 36):(loc2 + 56)], '%Y-%m-%d, %H:%M:%S')
                break
        for Line3 in f4:
            if 'Total time GPU was running' in Line3:
                loc3 = Line3.index('Total time GPU was running')
                date3 = Line3[(loc3 + 36):-1]  # 1st GPU Total time
                break

        delta1=date2-date1 #field time delta
        if date1==date2 :
            pass
        elif BBXDataLoc(0)<FirstTimeLoc_1stG<BBXDataLoc(0)+1000:
            now_date = datetime.datetime.now() # the Days' number of February
            now_year = now_date.year
            num_feb = calendar.monthrange(now_year, 2)[1]

            # Field time
            time1stG_1 = delta1.days  # 1st GPU total field days
            time1stG_2 = delta1.seconds
            time1stG_3 = time1stG_2 / 86400  # translate seconds to days
            time1stG_4 = time1stG_1 * 86400 + time1stG_2  # 1st GPU All time translate to seconds

            #All field days
            time1stG_5=time1stG_1+time1stG_3

            # field year
            if num_feb == 28:
                year1stG = int(time1stG_1 / 365)
            if num_feb == 29:
                year1stG = int(time1stG_1 / 366)

            # field days
            if num_feb == 28:
                days1stG = time1stG_1 - 365 * year1stG + time1stG_3
            elif num_feb == 29:
                days1stG = time1stG_1 - 366 * year1stG + time1stG_3

            # field Hour Min Seconds
            HMS1stG = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(time1stG_2))  # hour/min/second

            # GPU All running time
            ART1 = int(date3)

            # GPU All running year/days/hour min seconds
            if num_feb == 28:
                # year
                ARY1 = int(ART1 / (365 * 24 * 3600))

                # days
                ARD1 = int((ART1 - 365 * 24 * 3600 * ARY1) / (24 * 3600))

                # Hour Min Second
                ARHMS1 = int(ART1 - 365 * 24 * 3600 * ARY1 - 24 * 3600 * ARD1)
                ARHMS11 = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(ARHMS1))

            if num_feb == 29:
                ARY1 = int(ART1 / (366 * 24 * 3600))

                # days
                ARD1 = int((ART1 - 366 * 24 * 3600 * ARY1) / (24 * 3600))

                # Hour Min Second
                ARHMS1 = int(ART1 - 366 * 24 * 3600 * ARY1 - 24 * 3600 * ARD1)
                ARHMS11 = time.strftime('%Hhour:%Mmin:%Ssecond', time.gmtime(ARHMS1))

            # GPU All Running operation days
            ODays1 = (ART1 / (24 * 3600))
            # dutyCycle
            dutyCycle1 = (ART1 / time1stG_4) * 100

            # write field time
            f2.write('Field Time: %.3f days' % time1stG_5)
            f2.write('(%dyear, %ddays %s)\n' % (year1stG, days1stG, HMS1stG))
            f2.write('Total Time: %d seconds' % (ART1))
            f2.write('(%dyear, %ddays %s)\n' % (ARY1, ARD1, ARHMS11))
            f2.write('Operation Day=%.3f Days\n' % ODays1)
            f2.write('DutyCycle=%.1f%%\n' % dutyCycle1)


    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()

    return 'Calculate Time'

#GPU Max Power
def Power(n):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f4 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f5 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    l=0
    m=0

    #1st GPU Power
    if n==0:
        for Line1 in f1:
            l = l + 1
            if BBXDataLoc(0) < l < BBXDataLoc(0)+500:
                if 'Maximum power drawn per day' in Line1:
                    PowerArray=[]
                    PowerNum=int(linecache.getline(file1, l)[-9:-7])
                    for k in range(0,PowerNum):
                        Power=int(linecache.getline(file1, l + 4+k)[12:18])
                        PowerArray.append(Power)

                    PowerMax = str(max(PowerArray))
                    if int(PowerMax) > 0:
                        f2.write('MaxPwr%ddays:' % PowerNum)
                        f2.write(PowerMax)
                        f2.write('\n')
                        break

        l = 0
        for Line2 in f3:
            l = l + 1
            if BBXDataLoc(0) < l < BBXDataLoc(0)+500:
                if 'Maximum power drawn per month' in Line2:
                    PowerArray = []
                    PowerNum = int(linecache.getline(file1, l)[-11:-9])
                    for k in range(0, PowerNum):
                        Power = int(linecache.getline(file1, l + 4 + k)[12:18])
                        PowerArray.append(Power)

                    PowerMax = str(max(PowerArray))
                    if int(PowerMax)>0:
                        f2.write('MaxPwr%dmonths:' % PowerNum)
                        f2.write(PowerMax)
                        f2.write('\n')
                        break

    #2nd GPU Power
    if n==1:
        for Line3 in f4:
            m = m + 1
            if BBXDataLoc(1)<m < BBXDataLoc(1)+500 :
                if 'Maximum power drawn per day' in Line3:
                    PowerArray=[]
                    PowerNum=int(linecache.getline(file1, m)[-9:-7])
                    for k in range(0,PowerNum):
                        Power=int(linecache.getline(file1, m + 4+k)[12:18])
                        PowerArray.append(Power)

                    PowerMax = str(max(PowerArray))
                    if int(PowerMax) > 0:
                        f2.write('MaxPwr%ddays:' % PowerNum)
                        f2.write(PowerMax)
                        f2.write('\n')
                        break

        m=0
        for Line4 in f5:
            m=m+1
            if BBXDataLoc(1)<m < BBXDataLoc(1)+500 :
                if 'Maximum power drawn per month' in Line4:
                    PowerArray = []
                    PowerNum = int(linecache.getline(file1, m)[-11:-9])
                    for k in range(0, PowerNum):
                        Power = int(linecache.getline(file1, m + 4 + k)[12:18])
                        PowerArray.append(Power)

                    PowerMax = str(max(PowerArray))
                    if int(PowerMax)>0:
                        f2.write('MaxPwr%dmonths:' % PowerNum)
                        f2.write(PowerMax)
                        f2.write('\n')
                        break

    #One GPU
    if n==3:
        for Line1 in f1:
            l = l + 1
            if BBXDataLoc(0) < l < BBXDataLoc(0) + 600:
                if 'Maximum power drawn per day' in Line1:
                    PowerArray=[]
                    PowerNum=int(linecache.getline(file1, l)[-9:-7])
                    for k in range(0,PowerNum):
                        Power=int(linecache.getline(file1, l + 4+k)[12:18])
                        PowerArray.append(Power)

                    PowerMax = str(max(PowerArray))
                    if int(PowerMax) > 0:
                        f2.write('MaxPwr%ddays:' % PowerNum)
                        f2.write(PowerMax)
                        f2.write('\n')
                        break
        l = 0
        for Line2 in f3:
            l = l + 1
            if BBXDataLoc(0) < l < BBXDataLoc(0) + 600:
                if 'Maximum power drawn per month' in Line2:
                    PowerArray = []
                    PowerNum = int(linecache.getline(file1, l)[-11:-9])
                    for k in range(0, PowerNum):
                        Power = int(linecache.getline(file1, l + 4 + k)[12:18])
                        PowerArray.append(Power)

                    PowerMax = str(max(PowerArray))
                    if int(PowerMax)>0:
                        f2.write('MaxPwr%dmonths:' % PowerNum)
                        f2.write(PowerMax)
                        f2.write('\n')
                        break

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

    return 'Max Power Show'

#GPU Day Temp
def DayTemp(p):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f4 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f5 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    i=0 #'i' and 'j' is the line number
    j=0
    #1st GPU Temp
    if p==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1)-150:
                if 'Maximum GPU temp per day' in Line1:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-9:-7])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[21:32]
                        TempArray.append(Temp)

                    TempMax = max(TempArray)
                    if float(TempMax) > 0:
                        f2.write('MaxTemp%ddays:' % TempNum)
                        f2.write(TempMax)
                        f2.write('\n')
                        break

        i=0
        for Line2 in f3:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1)-150:
                if 'Minimum GPU temp per day' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-9:-7])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[21:32]
                        TempArray.append(Temp)

                    TempMin =min(TempArray)
                    if float(TempMin) > 0:
                        f2.write('MinTemp%ddays:' % TempNum)
                        f2.write(TempMin)
                        f2.write('\n')
                        break

    #2nd GPU Power
    elif p==1:
        for Line2 in f4:
            j=j+1
            if BBXDataLoc(1)<j < BBXDataLoc(1)+800:
                if 'Maximum GPU temp per day' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1,j)[-9:-7])
                    for k in range(0, TempNum):
                        Temp = linecache.getline(file1, j + 4 + k)[21:32]
                        TempArray.append(Temp)

                    TempMax = max(TempArray)
                    if float(TempMax) > 0:
                        f2.write('MaxTemp%ddays:' % TempNum)
                        f2.write(TempMax)
                        f2.write('\n')
                        break
        j=0
        for Line2 in f5:
            j=j+1
            if BBXDataLoc(1) < j < BBXDataLoc(1) + 800:
                if 'Minimum GPU temp per day' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, j)[-9:-7])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, j + 4+k)[21:32]
                        TempArray.append(Temp)

                    TempMin = min(TempArray)
                    if float(TempMin) > 0:
                        f2.write('MinTemp%ddays:' % TempNum)
                        f2.write(TempMin)
                        f2.write('\n')
                        break

    #One GPU
    if p==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+800:
                if 'Maximum GPU temp per day' in Line1:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-9:-7])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[21:32]
                        TempArray.append(Temp)

                    TempMax = max(TempArray)
                    if float(TempMax) > 0:
                        f2.write('MaxTemp%ddays:' % TempNum)
                        f2.write(TempMax)
                        f2.write('\n')
                        break

        i=0
        for Line2 in f3:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+800:
                if 'Minimum GPU temp per day' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-9:-7])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[21:32]
                        TempArray.append(Temp)

                    TempMin =min(TempArray)
                    if float(TempMin) > 0:
                        f2.write('MinTemp%ddays:' % TempNum)
                        f2.write(TempMin)
                        f2.write('\n')
                        break


    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

    return 'GPU Day Temp Show'

#GPU Month Temp
def MonTemp(q):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f4 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f5 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    i=0 #'i' and 'j' is the line number
    j=0
    #1st GPU Temp
    if q==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1)-150:
                if 'Maximum GPU temp per month' in Line1:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-11:-9])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[23:32]
                        TempArray.append(Temp)

                    TempMax = max(TempArray)
                    if float(TempMax) > 0:
                        f2.write('MaxTemp%dmonths:' % TempNum)
                        f2.write(TempMax)
                        f2.write('\n')
                        break

        i=0
        for Line2 in f3:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1)-150:
                if 'Minimum GPU temp per month' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-11:-9])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[23:32]
                        TempArray.append(Temp)

                    TempMin =min(TempArray)
                    if float(TempMin) > 0:
                        f2.write('MinTemp%dmonths:' % TempNum)
                        f2.write(TempMin)
                        f2.write('\n')
                        break

    #2nd GPU Power
    elif q==1:
        for Line2 in f4:
            j=j+1
            if BBXDataLoc(1) < j < BBXDataLoc(1) + 800:
                if 'Maximum GPU temp per month' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1,j)[-11:-9])
                    for k in range(0, TempNum):
                        Temp = linecache.getline(file1, j + 4 + k)[23:32]
                        TempArray.append(Temp)

                    TempMax = max(TempArray)
                    if float(TempMax) > 0:
                        f2.write('MaxTemp%dmonths:' % TempNum)
                        f2.write(TempMax)
                        f2.write('\n')
                        break
        j=0
        for Line2 in f5:
            j=j+1
            if BBXDataLoc(1) < j < BBXDataLoc(1) + 800:
                if 'Minimum GPU temp per month' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, j)[-11:-9])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, j + 4+k)[23:32]
                        TempArray.append(Temp)

                    TempMin = min(TempArray)
                    if float(TempMin) > 0:
                        f2.write('MinTemp%dmonths:' % TempNum)
                        f2.write(TempMin)
                        f2.write('\n')
                        break

    #One GPU
    if q==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+800:
                if 'Maximum GPU temp per month' in Line1:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-11:-9])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[23:32]
                        TempArray.append(Temp)

                    TempMax = max(TempArray)
                    if float(TempMax) > 0:
                        f2.write('MaxTemp%dmonths:' % TempNum)
                        f2.write(TempMax)
                        f2.write('\n')
                        break

        i=0
        for Line2 in f3:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+800:
                if 'Minimum GPU temp per month' in Line2:
                    TempArray = []
                    TempNum = int(linecache.getline(file1, i)[-11:-9])
                    for k in range(0,TempNum):
                        Temp=linecache.getline(file1, i + 4+k)[23:32]
                        TempArray.append(Temp)

                    TempMin =min(TempArray)
                    if float(TempMin) > 0:
                        f2.write('MinTemp%dmonths:' % TempNum)
                        f2.write(TempMin)
                        f2.write('\n')
                        break

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

    return 'GPU Month Temp Show'

#Blacklisted Pages
def BlacklistedPages(r):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')
    f4 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    i=0
    j=0
    k=0
    BlackPagesAllNumber=0
    BlacklistCountDSbe=0
    BlacklistCountDDbe=0

    BlacklistCountDSbe_2ndG=0
    BlacklistCountDDbe_2ndG=0

    #1st GPU
    if r==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1):
                if 'Blacklisted Pages:' in Line1:
                        BlackPagesAllNumber=int(Line1[21:-1])

                if BlackPagesAllNumber>0:
                    if 'DprSbe ' in Line1:
                        BlacklistCountDSbe=BlacklistCountDSbe+1
                    if 'DprDbe 'in Line1:
                        BlacklistCountDDbe=BlacklistCountDDbe+1


        f2.write('RetirePages=%s ' %BlackPagesAllNumber)
        f2.write('\n')
        if BlacklistCountDSbe>0:
            f2.write('DprSbe=%s ' % BlacklistCountDSbe)
            f2.write('\n')
        if BlacklistCountDDbe>0:
            f2.write('DprDbe=%s ' % BlacklistCountDDbe)
            f2.write('\n')

    #2nd GPU
    if r==1:
        for Line2 in f3:
            j=j+1
            if j > BBXDataLoc(1):
                if 'Blacklisted Pages:' in Line2:
                    BlackPagesAllNumber=int(Line2[21:-1])

                if BlackPagesAllNumber > 0:
                    if 'DprSbe ' in Line2:
                        BlacklistCountDSbe_2ndG = BlacklistCountDSbe_2ndG + 1
                    if 'DprDbe ' in Line2:
                        BlacklistCountDDbe_2ndG = BlacklistCountDDbe_2ndG + 1

        f2.write('RetirePages=%s ' % BlackPagesAllNumber)
        f2.write('\n')
        if BlacklistCountDSbe_2ndG > 0:
            f2.write('DprSbe=%s ' % BlacklistCountDSbe_2ndG)
            f2.write('\n')
        if BlacklistCountDDbe_2ndG > 0:
            f2.write('DprDbe=%s ' % BlacklistCountDDbe_2ndG)
            f2.write('\n')

    #One GPU
    if r==3:
        for Line3 in f4:
            k=k+1
            if BBXDataLoc(0) < k < BBXDataLoc(0) + 1000:
                if 'Blacklisted Pages:' in Line3:
                    BlackPagesAllNumber=int(Line3[21:-1])

                if BlackPagesAllNumber > 0:
                    if 'DprSbe ' in Line3:
                        BlacklistCountDSbe = BlacklistCountDSbe + 1
                    if 'DprDbe ' in Line3:
                        BlacklistCountDDbe = BlacklistCountDDbe + 1

        f2.write('RetirePages=%s ' % BlackPagesAllNumber)
        f2.write('\n')
        if BlacklistCountDSbe > 0:
            f2.write('DprSbe=%s ' % BlacklistCountDSbe)
            f2.write('\n')
        if BlacklistCountDDbe > 0:
            f2.write('DprDbe=%s ' % BlacklistCountDDbe)
            f2.write('\n')

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    return "Blacklisted Pages Count"

#FB Error Counts
def FBErrorCount(s):
    file1=os.path.join(cur_file_dir(),'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    k=0
    i=0
    l=0
    FBErrorLoc=0
    L2CacheErrorLoc=0
    #1st GPU
    if s==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1):
                if 'FB Error Counts' in Line1:
                    FBErrorLoc=i
                elif 'L2 Cache Error Counts' in Line1:
                    L2CacheErrorLoc=i
                    break

        SubpNum=L2CacheErrorLoc-FBErrorLoc-3
        if SubpNum>0:
            for j in range (0,SubpNum):
                FB_SBENum=int(linecache.getline(file1,FBErrorLoc+j+3 )[31:43])
                FB_DBENum=int(linecache.getline(file1,FBErrorLoc+j+3)[-11:-1])
                PartitionLoc =int(j/2)
                SubpLoc=j%2

                if FB_SBENum >0:
                    if k==0:
                        f2.write('FBError:P%dS%d_SBE:%d; '%(PartitionLoc,SubpLoc,FB_SBENum))
                        k=1
                    else:
                        f2.write('P%dS%d_SBE:%d; '%(PartitionLoc,SubpLoc,FB_SBENum))
                if FB_DBENum >0:
                    if k==0:
                        f2.write('FBError:P%dS%d_DBE:%d; '%(PartitionLoc,SubpLoc,FB_DBENum))
                        k=1
                    else:
                        f2.write('P%dS%d_DBE:%d; '%(PartitionLoc,SubpLoc,FB_DBENum))

            if k==1:
                k=0
                f2.write('\n')

    #2nd GPU
    elif s==1:
        for Line2 in f3:
            l=l+1
            if l > BBXDataLoc(1):
                if 'FB Error Counts' in Line2:
                    FBErrorLoc=l
                elif 'L2 Cache Error Counts' in Line2:
                    L2CacheErrorLoc=l
                    break

        SubpNum=L2CacheErrorLoc-FBErrorLoc-3
        if SubpNum>0:
            for j in range (0,SubpNum):
                FB_SBENum=int(linecache.getline(file1,FBErrorLoc+j+3 )[31:43])
                FB_DBENum=int(linecache.getline(file1,FBErrorLoc+j+3)[-11:-1])
                PartitionLoc =int(j/2)
                SubpLoc=j%2

                if FB_SBENum >0:
                    if k==0:
                        f2.write('FBError:P%dS%d_SBE:%d; '%(PartitionLoc,SubpLoc,FB_SBENum))
                        k=1
                    else:
                        f2.write('P%dS%d_SBE:%d; '%(PartitionLoc,SubpLoc,FB_SBENum))
                if FB_DBENum >0:
                    if k==0:
                        f2.write('FBError:P%dS%d_DBE:%d; '%(PartitionLoc,SubpLoc,FB_DBENum))
                        k=1
                    else:
                        f2.write('P%dS%d_DBE:%d; '%(PartitionLoc,SubpLoc,FB_DBENum))

            if k==1:
                k=0
                f2.write('\n')

    #One GPU
    if s==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+1000:
                if 'FB Error Counts' in Line1:
                    FBErrorLoc=i
                elif 'L2 Cache Error Counts' in Line1:
                    L2CacheErrorLoc=i
                    break

        SubpNum=L2CacheErrorLoc-FBErrorLoc-3
        if SubpNum>0:
            for j in range (0,SubpNum):
                FB_SBENum=int(linecache.getline(file1,FBErrorLoc+j+3 )[31:43])
                FB_DBENum=int(linecache.getline(file1,FBErrorLoc+j+3)[-11:-1])
                PartitionLoc =int(j/2)
                SubpLoc=j%2

                if FB_SBENum >0:
                    if k==0:
                        f2.write('FBError:P%dS%d_SBE:%d; '%(PartitionLoc,SubpLoc,FB_SBENum))
                        k=1
                    else:
                        f2.write('P%dS%d_SBE:%d; '%(PartitionLoc,SubpLoc,FB_SBENum))
                if FB_DBENum >0:
                    if k==0:
                        f2.write('FBError:P%dS%d_DBE:%d; '%(PartitionLoc,SubpLoc,FB_DBENum))
                        k=1
                    else:
                        f2.write('P%dS%d_DBE:%d; '%(PartitionLoc,SubpLoc,FB_DBENum))

            if k==1:
                k=0
                f2.write('\n')

    f1.close()
    f2.close()
    f3.close()

    return 'FB Error Counts'

#Texture Cache Retry Counts
def TextureCacheErrors(t):
    file1=os.path.join(cur_file_dir(),'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    k=0
    i=0
    l=0
    FBErrorLoc=0
    TextureLoc=0
    TPCNum_PerGPC=0
    #1st GPU
    if t==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1):
                if 'Texture Cache Retry Counts' in Line1:
                    TextureLoc=i
                elif 'FB Error Counts' in Line1:
                    FBErrorLoc = i
                    break

        TPCAllNum=FBErrorLoc-TextureLoc-3
        if TPCAllNum>0 :

            for m in range(0, 6):
                TPC_Count = int(linecache.getline(file1, TextureLoc + 3 + m)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                TextureCorrect = int(linecache.getline(file1, TextureLoc + j + 3)[31:41])
                TextureUncorrect = int(linecache.getline(file1, TextureLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if TextureCorrect>0:
                    if k==0:
                        f2.write('Texture:GPC%dTPC%d_Correctable:%d; '%(GPCLoc,TPCLoc,TextureCorrect))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_Correctable:%d; '%(GPCLoc,TPCLoc,TextureCorrect))
                if TextureUncorrect>0:
                    if k==0:
                        f2.write('Texture:GPC%dTPC%d_Uncorrectable:%d; '%(GPCLoc,TPCLoc,TextureUncorrect))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_Uncorrectable:%d; '%(GPCLoc,TPCLoc,TextureUncorrect))

            if k == 1:
                k = 0
                f2.write('\n')
    #2nd GPU
    if t==1:
        for Line1 in f3:
            l=l+1
            if l > BBXDataLoc(1):
                if 'Texture Cache Retry Counts' in Line1:
                    TextureLoc=l
                elif 'FB Error Counts' in Line1:
                    FBErrorLoc = l
                    break

        TPCAllNum=FBErrorLoc-TextureLoc-3
        if TPCAllNum>0:

            for n in range(0, 6):
                TPC_Count = int(linecache.getline(file1, TextureLoc + 3 + n)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                TextureCorrect = int(linecache.getline(file1, TextureLoc + j + 3)[31:41])
                TextureUncorrect = int(linecache.getline(file1, TextureLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if TextureCorrect>0:
                    if k==0:
                        f2.write('Texture:GPC%dTPC%d_Correctable:%d; '%(GPCLoc,TPCLoc,TextureCorrect))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_Correctable:%d; '%(GPCLoc,TPCLoc,TextureCorrect))
                if TextureUncorrect>0:
                    if k==0:
                        f2.write('Texture:GPC%dTPC%d_Uncorrcetable:%d; '%(GPCLoc,TPCLoc,TextureUncorrect))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_Uncorrectable:%d; '%(GPCLoc,TPCLoc,TextureUncorrect))

            if k==1:
                k=0
                f2.write('\n')

    #One GPU
    if t==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+900:
                if 'Texture Cache Retry Counts' in Line1:
                    TextureLoc=i
                elif 'FB Error Counts' in Line1:
                    FBErrorLoc = i
                    break

        TPCAllNum=FBErrorLoc-TextureLoc-3
        if TPCAllNum>0 :

            for n in range(0, 6):
                TPC_Count = int(linecache.getline(file1, TextureLoc + 3 + n)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                TextureCorrect = int(linecache.getline(file1, TextureLoc + j + 3)[31:41])
                TextureUncorrect = int(linecache.getline(file1, TextureLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if TextureCorrect>0:
                    if k==0:
                        f2.write('Texture:GPC%dTPC%d_Correctable:%d; '%(GPCLoc,TPCLoc,TextureCorrect))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_Correctable:%d; '%(GPCLoc,TPCLoc,TextureCorrect))
                if TextureUncorrect>0:
                    if k==0:
                        f2.write('Texture:GPC%dTPC%d_Uncorrectable:%d; '%(GPCLoc,TPCLoc,TextureUncorrect))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_Uncorrectable:%d; '%(GPCLoc,TPCLoc,TextureUncorrect))

            if k == 1:
                k = 0
                f2.write('\n')

    f1.close()
    f2.close()
    f3.close()

    return 'Texture Cache Retry Counts'

#Register File Error Counts
def RegisterErrorCounts(u):
    file1=os.path.join(cur_file_dir(),'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    k=0
    i=0
    l=0
    RegisterLoc=0
    TextureLoc=0
    TPCNum_PerGPC=0
    #1st GPU
    if u==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1):
                if 'Register File Error Counts' in Line1:
                    RegisterLoc=i
                elif 'Texture Cache Retry Counts' in Line1:
                    TextureLoc = i
                    break

        TPCAllNum=TextureLoc-RegisterLoc-3
        if TPCAllNum>0:

            for m in range(0, 6):
                TPC_Count = int(linecache.getline(file1, RegisterLoc + 3 + m)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                RegisterSBE = int(linecache.getline(file1, RegisterLoc + j + 3)[29:44])
                RegisterDBE = int(linecache.getline(file1, RegisterLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if RegisterSBE>0:
                    if k==0:
                        f2.write('Register:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,RegisterSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,RegisterSBE))
                if RegisterDBE>0:
                    if k==0:
                        f2.write('Register:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,RegisterDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,RegisterDBE))

            if k == 1:
                k = 0
                f2.write('\n')
    #2nd GPU
    if u==1:
        for Line1 in f3:
            l=l+1
            if l > BBXDataLoc(1):
                if 'Register File Error Counts' in Line1:
                    RegisterLoc=l
                elif 'Texture Cache Retry Counts' in Line1:
                    TextureLoc = l
                    break

        TPCAllNum=TextureLoc-RegisterLoc-3
        if TPCAllNum>0:

            for n in range(0, 6):
                TPC_Count = int(linecache.getline(file1, RegisterLoc + 3 + n)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                RegisterSBE = int(linecache.getline(file1, RegisterLoc + j + 3)[29:44])
                RegisterDBE = int(linecache.getline(file1, RegisterLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if RegisterSBE>0:
                    if k==0:
                        f2.write('Register:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,RegisterSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,RegisterSBE))
                if RegisterDBE>0:
                    if k==0:
                        f2.write('Register:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,RegisterDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,RegisterDBE))

            if k==1:
                k=0
                f2.write('\n')

    #One GPU
    if u==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+900:
                if 'Register File Error Counts' in Line1:
                    RegisterLoc=i
                elif 'Texture Cache Retry Counts' in Line1:
                    TextureLoc = i
                    break

        TPCAllNum=TextureLoc-RegisterLoc-3
        if TPCAllNum>0:

            for m in range(0, 6):
                TPC_Count = int(linecache.getline(file1, RegisterLoc + 3 + m)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                RegisterSBE = int(linecache.getline(file1, RegisterLoc + j + 3)[29:44])
                RegisterDBE = int(linecache.getline(file1, RegisterLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if RegisterSBE>0:
                    if k==0:
                        f2.write('Register:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,RegisterSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,RegisterSBE))
                if RegisterDBE>0:
                    if k==0:
                        f2.write('Register:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,RegisterDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,RegisterDBE))

            if k == 1:
                k = 0
                f2.write('\n')

    f1.close()
    f2.close()
    f3.close()

    return 'Register File Error Counts'

#L1 Cache Error Counts
def L1CacheErrorCount(v):
    file1=os.path.join(cur_file_dir(),'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    k=0
    i=0
    l=0
    L1CacheLoc=0
    TPCNum_PerGPC=0
    #1st GPU
    if v==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1):
                if 'L1 Cache Error Counts' in Line1:
                    L1CacheLoc=i
                elif 'Register File Error Counts' in Line1:
                    RegisterLoc = i
                    break

        TPCAllNum=RegisterLoc-L1CacheLoc-3
        if TPCAllNum>0 :
            for m in range(0, 6):
                TPC_Count = int(linecache.getline(file1, L1CacheLoc + 3 + m)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                L1CacheSBE = int(linecache.getline(file1, L1CacheLoc + j + 3)[29:44])
                L1CacheDBE = int(linecache.getline(file1, L1CacheLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if L1CacheSBE>0:
                    if k==0:
                        f2.write('L1Cache:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,L1CacheSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,L1CacheSBE))
                if L1CacheDBE>0:
                    if k==0:
                        f2.write('L1Cache:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,L1CacheDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,L1CacheDBE))

            if k == 1:
                k = 0
                f2.write('\n')
    #2nd GPU
    if v==1:
        for Line1 in f3:
            l=l+1
            if l > BBXDataLoc(1):
                if 'L1 Cache Error Counts' in Line1:
                    L1CacheLoc=l
                elif 'Register File Error Counts' in Line1:
                    RegisterLoc = l
                    break

        TPCAllNum=RegisterLoc-L1CacheLoc-3
        if TPCAllNum>0:

            for n in range(0, 6):
                TPC_Count = int(linecache.getline(file1, L1CacheLoc + 3 + n)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                L1CacheSBE = int(linecache.getline(file1, L1CacheLoc + j + 3)[29:44])
                L1CacheDBE = int(linecache.getline(file1, L1CacheLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if L1CacheSBE>0:
                    if k==0:
                        f2.write('L1Cache:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,L1CacheSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,L1CacheSBE))
                if L1CacheDBE>0:
                    if k==0:
                        f2.write('L1Cache:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,L1CacheDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,L1CacheDBE))

            if k==1:
                k=0
                f2.write('\n')

    #One GPU
    if v==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+900:
                if 'L1 Cache Error Counts' in Line1:
                    L1CacheLoc=i
                elif 'Register File Error Counts' in Line1:
                    RegisterLoc = i
                    break

        TPCAllNum=RegisterLoc-L1CacheLoc-3
        if TPCAllNum>0 :

            for m in range(0, 6):
                TPC_Count = int(linecache.getline(file1, L1CacheLoc + 3 + m)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                L1CacheSBE = int(linecache.getline(file1, L1CacheLoc + j + 3)[29:44])
                L1CacheDBE = int(linecache.getline(file1, L1CacheLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if L1CacheSBE>0:
                    if k==0:
                        f2.write('L1Cache:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,L1CacheSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,L1CacheSBE))
                if L1CacheDBE>0:
                    if k==0:
                        f2.write('L1Cache:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,L1CacheDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,L1CacheDBE))

            if k == 1:
                k = 0
                f2.write('\n')

    f1.close()
    f2.close()
    f3.close()

    return 'L1 Cache Error Counts'

#L2 Cache Error Counts:
def L2CacheErrorCount(x):
    file1=os.path.join(cur_file_dir(),'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    k=0
    i=0
    l=0
    L2CacheLoc=0
    SliceNum_PerPar=0
    FBErrorLoc=0
    SliceAllNum=0
    #1st GPU
    if x==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1):
                if 'L2 Cache Error Counts' in Line1:
                    L2CacheLoc=i
                    break
                elif 'FB Error Counts' in Line1:
                    FBErrorLoc = i

        PartitionNum=(L2CacheLoc-FBErrorLoc-3)/2
        if PartitionNum>0 :
            for m in range(0, 6):
                Slice_Count = int(linecache.getline(file1, L2CacheLoc + 3 + m)[7:8])
                if Slice_Count == 0:
                    SliceNum_PerPar = SliceNum_PerPar + 1

            SliceAllNum=int(PartitionNum*SliceNum_PerPar)

            for j in range (0,SliceAllNum):
                L2CacheSBE = int(linecache.getline(file1, L2CacheLoc + j + 3)[29:44])
                L2CacheDBE = int(linecache.getline(file1, L2CacheLoc + j + 3)[-11:-1])
                ParLoc=int(j/SliceNum_PerPar)
                SliceLoc=j%SliceNum_PerPar

                if L2CacheSBE>0:
                    if k==0:
                        f2.write('L2Cache:P%dS%d_SBE:%d; '%(ParLoc,SliceLoc,L2CacheSBE))
                        k=1
                    else:
                        f2.write('P%dS%d_SBE:%d; '%(ParLoc,SliceLoc,L2CacheSBE))
                if L2CacheDBE>0:
                    if k==0:
                        f2.write('L2Cache:P%dS%d_DBE:%d; '%(ParLoc,SliceLoc,L2CacheDBE))
                        k=1
                    else:
                        f2.write('P%dS%d_DBE:%d; '%(ParLoc,SliceLoc,L2CacheDBE))

            if k == 1:
                k = 0
                f2.write('\n')
    #2nd GPU
    if x==1:
        for Line2 in f3:
            l=l+1
            if l > BBXDataLoc(1):
                if 'L2 Cache Error Counts' in Line2:
                    L2CacheLoc = l
                    break
                elif 'FB Error Counts' in Line2:
                    FBErrorLoc = l

        PartitionNum = (L2CacheLoc - FBErrorLoc - 3) / 2
        if PartitionNum > 0:
            for m in range(0, 6):
                Slice_Count = int(linecache.getline(file1, L2CacheLoc + 3 + m)[7:8])
                if Slice_Count == 0:
                    SliceNum_PerPar = SliceNum_PerPar + 1

            SliceAllNum = int(PartitionNum * SliceNum_PerPar)
            for j in range (0,SliceAllNum):
                L2CacheSBE = int(linecache.getline(file1, L2CacheLoc + j + 3)[29:44])
                L2CacheDBE = int(linecache.getline(file1, L2CacheLoc + j + 3)[-11:-1])
                ParLoc=int(j/SliceNum_PerPar)
                SliceLoc=j%SliceNum_PerPar

                if L2CacheSBE>0:
                    if k==0:
                        f2.write('L2Cache:P%dS%d_SBE:%d; '%(ParLoc,SliceLoc,L2CacheSBE))
                        k=1
                    else:
                        f2.write('P%dS%d_SBE:%d; '%(ParLoc,SliceLoc,L2CacheSBE))
                if L2CacheDBE>0:
                    if k==0:
                        f2.write('L2Cache:P%dS%d_DBE:%d; '%(ParLoc,SliceLoc,L2CacheDBE))
                        k=1
                    else:
                        f2.write('P%dS%d_DBE:%d; '%(ParLoc,SliceLoc,L2CacheDBE))

            if k==1:
                k=0
                f2.write('\n')

    #One GPU
    if x==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+900:
                if 'L2 Cache Error Counts' in Line1:
                    L2CacheLoc = i
                    break
                elif 'FB Error Counts' in Line1:
                    FBErrorLoc = i

        PartitionNum = (L2CacheLoc - FBErrorLoc - 3) / 2
        if PartitionNum > 0:
            for m in range(0, 6):
                Slice_Count = int(linecache.getline(file1, L2CacheLoc + 3 + m)[7:8])
                if Slice_Count == 0:
                    SliceNum_PerPar = SliceNum_PerPar + 1

            SliceAllNum = int(PartitionNum * SliceNum_PerPar)

        for j in range (0,SliceAllNum):
            L2CacheSBE = int(linecache.getline(file1, L2CacheLoc + j + 3)[29:44])
            L2CacheDBE = int(linecache.getline(file1, L2CacheLoc + j + 3)[-11:-1])
            ParLoc=int(j/SliceNum_PerPar)
            SliceLoc=j%SliceNum_PerPar

            if L2CacheSBE>0:
                if k==0:
                    f2.write('L2Cache:P%dS%d_SBE:%d; '%(ParLoc,SliceLoc,L2CacheSBE))
                    k=1
                else:
                    f2.write('P%dS%d_SBE:%d; '%(ParLoc,SliceLoc,L2CacheSBE))
            if L2CacheDBE>0:
                if k==0:
                    f2.write('L2Cache:P%dS%d_DBE:%d; '%(ParLoc,SliceLoc,L2CacheDBE))
                    k=1
                else:
                    f2.write('P%dS%d_DBE:%d; '%(ParLoc,SliceLoc,L2CacheDBE))
        if k == 1:
            k = 0
            f2.write('\n')

    f1.close()
    f2.close()
    f3.close()

    return 'L2 Cache Error Counts'

#SHM Cache Error Counts
def SHMCacheErrorCount(y):
    file1=os.path.join(cur_file_dir(),'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    k=0
    i=0
    l=0
    TPCNum_PerGPC=0
    SHMCacheLoc=0
    #1st GPU
    if y==0:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(1):
                if 'Texture Cache Retry Counts' in Line1:
                    TextureLoc=i
                elif 'Register File Error Counts' in Line1:
                    RegisterLoc = i
                elif 'SHM Cache Error Counts' in Line1:
                    SHMCacheLoc=i
                    break

        TPCAllNum=TextureLoc-RegisterLoc-3
        if SHMCacheLoc>0 :
            for m in range(0, 6):
                TPC_Count = int(linecache.getline(file1, SHMCacheLoc + 3 + m)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                SHMCacheSBE = int(linecache.getline(file1, SHMCacheLoc + j + 3)[29:44])
                SHMCacheDBE = int(linecache.getline(file1, SHMCacheLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if SHMCacheSBE>0:
                    if k==0:
                        f2.write('SHMCache:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,SHMCacheSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,SHMCacheSBE))
                if SHMCacheDBE>0:
                    if k==0:
                        f2.write('SHMCache:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,SHMCacheDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,SHMCacheDBE))

            if k == 1:
                k = 0
                f2.write('\n')
    #2nd GPU
    if y==1:
        for Line1 in f3:
            l=l+1
            if l > BBXDataLoc(1):
                if 'Texture Cache Retry Counts' in Line1:
                    TextureLoc=l
                elif 'Register File Error Counts' in Line1:
                    RegisterLoc = l
                elif 'SHM Cache Error Counts' in Line1:
                    SHMCacheLoc=l
                    break

        TPCAllNum=TextureLoc-RegisterLoc-3
        if SHMCacheLoc>0:

            for n in range(0, 6):
                TPC_Count = int(linecache.getline(file1, SHMCacheLoc + 3 + n)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                SHMCacheSBE = int(linecache.getline(file1, SHMCacheLoc + j + 3)[29:44])
                SHMCacheDBE = int(linecache.getline(file1, SHMCacheLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if SHMCacheSBE>0:
                    if k==0:
                        f2.write('SHMCache:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,SHMCacheSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,SHMCacheSBE))
                if SHMCacheDBE>0:
                    if k==0:
                        f2.write('SHMCache:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,SHMCacheDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,SHMCacheDBE))

            if k==1:
                k=0
                f2.write('\n')

    #One GPU
    if y==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0) < i < BBXDataLoc(0)+900:
                if 'Texture Cache Retry Counts' in Line1:
                    TextureLoc=i
                elif 'Register File Error Counts' in Line1:
                    RegisterLoc = i
                elif 'SHM Cache Error Counts' in Line1:
                    SHMCacheLoc=i
                    break

        TPCAllNum=TextureLoc-RegisterLoc-3
        if SHMCacheLoc>0 :
            for m in range(0, 6):
                TPC_Count = int(linecache.getline(file1, SHMCacheLoc + 3 + m)[6:7])
                if TPC_Count == 0:
                    TPCNum_PerGPC = TPCNum_PerGPC + 1

            for j in range (0,TPCAllNum):
                SHMCacheSBE = int(linecache.getline(file1, SHMCacheLoc + j + 3)[29:44])
                SHMCacheDBE = int(linecache.getline(file1, SHMCacheLoc + j + 3)[-11:-1])
                GPCLoc=int(j/TPCNum_PerGPC)
                TPCLoc=j%TPCNum_PerGPC

                if SHMCacheSBE>0:
                    if k==0:
                        f2.write('SHMCache:GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,SHMCacheSBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_SBE:%d; '%(GPCLoc,TPCLoc,SHMCacheSBE))
                if SHMCacheDBE>0:
                    if k==0:
                        f2.write('SHMCache:GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,SHMCacheDBE))
                        k=1
                    else:
                        f2.write('GPC%dTPC%d_DBE:%d; '%(GPCLoc,TPCLoc,SHMCacheDBE))

            if k == 1:
                k = 0
                f2.write('\n')

    f1.close()
    f2.close()
    f3.close()

    return 'SHM Cache Error Counts'

#XID
def XID(z):
    file1 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
    f1=open(file1,'r',encoding='UTF-8',errors='ignore')
    file2=os.path.join(cur_file_dir(),'result.log')
    f2=open(file2,'a+')
    f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    i=0
    Mark=0
    XidNumber = []
    XidNumberLoc=[]

    #One GPU
    if z==3:
        for Line1 in f1:
            i=i+1
            if BBXDataLoc(0)<i<BBXDataLoc(0)+1300:
                if 'Xid number:' in Line1:
                    Xid=int(linecache.getline(file1, i)[-3:-1])
                    XidLoc=i
                    XidNumber.append(Xid)
                    XidNumberLoc.append(XidLoc)

        XidNumberSet=set(XidNumber)
        XidNumberList=[k for k in XidNumberSet]#'Set' change to 'List'
        if len(XidNumberList)>0:
            for j in range(0, len(XidNumberList)):
                for l in range(0,len(XidNumber)):
                    if XidNumberList[j]==XidNumber[l]:
                        NvidiaRMDriver=int(linecache.getline(file1,XidNumberLoc[l]+6 )[-7:-1])
                        #print('NvidiaRMDriver=',NvidiaRMDriver)
                        if Mark==0:
                            f2.write('XidNumber(rmDriverVersion):' )
                            f2.write(str(XidNumberList[j]))
                            f2.write('(%s)'%(str(NvidiaRMDriver)))
                            Mark=1
                            break
                        elif Mark==1:
                            f2.write(',')
                            f2.write(str(XidNumberList[j]))
                            f2.write('(%s)'%(str(NvidiaRMDriver)))
                            break

        f2.write('\n')
        if Mark==1:
            Mark=0

    #Two GPU
    i=0
    if z==0:#1st GPU
        for Line2 in f3:
            i=i+1
            if BBXDataLoc(0)<i<BBXDataLoc(1):
                if 'Xid number:' in Line2:
                    Xid=int(linecache.getline(file1, i)[-3:-1])
                    XidLoc=i
                    XidNumber.append(Xid)
                    XidNumberLoc.append(XidLoc)

        XidNumberSet=set(XidNumber)
        XidNumberList=[k for k in XidNumberSet]#'Set' change to 'List'
        if len(XidNumberList)>0:
            for j in range(0, len(XidNumberList)):
                for l in range(0,len(XidNumber)):
                    if XidNumberList[j]==XidNumber[l]:
                        NvidiaRMDriver=int(linecache.getline(file1,XidNumberLoc[l]+6 )[-7:-1])
                        #print('NvidiaRMDriver=',NvidiaRMDriver)
                        if Mark==0:
                            f2.write('XidNumber(rmDriverVersion):' )
                            f2.write(str(XidNumberList[j]))
                            f2.write('(%s)'%(str(NvidiaRMDriver)))
                            Mark=1
                            break
                        elif Mark==1:
                            f2.write(',')
                            f2.write(str(XidNumberList[j]))
                            f2.write('(%s)'%(str(NvidiaRMDriver)))
                            break

        f2.write('\n')
        if Mark==1:
            Mark=0

    i=0
    if z==1:#2nd GPU
        for Line3 in f3:
            i=i+1
            if i>BBXDataLoc(1):
                if 'Xid number:' in Line3:
                    Xid=int(linecache.getline(file1, i)[-3:-1])
                    XidLoc=i
                    XidNumber.append(Xid)
                    XidNumberLoc.append(XidLoc)

        XidNumberSet=set(XidNumber)
        XidNumberList=[k for k in XidNumberSet]#'Set' change to 'List'
        if len(XidNumberList)>0:
            for j in range(0, len(XidNumberList)):
                for l in range(0,len(XidNumber)):
                    if XidNumberList[j]==XidNumber[l]:
                        NvidiaRMDriver=int(linecache.getline(file1,XidNumberLoc[l]+6 )[-7:-1])
                        #print('NvidiaRMDriver=',NvidiaRMDriver)
                        if Mark==0:
                            f2.write('XidNumber(rmDriverVersion):' )
                            f2.write(str(XidNumberList[j]))
                            f2.write('(%s)'%(str(NvidiaRMDriver)))
                            Mark=1
                            break
                        elif Mark==1:
                            f2.write(',')
                            f2.write(str(XidNumberList[j]))
                            f2.write('(%s)'%(str(NvidiaRMDriver)))
                            break

        f2.write('\n')
        if Mark==1:
            Mark=0

    f1.close()
    f2.close()
    f3.close()
    return 'Xid Number Collect'

if __name__=="__main__":
    #Remove original result.log
    fileResult = os.path.join(cur_file_dir(), 'result.log')
    fileBBXBuffer = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')

    fileResultRemove=open(fileResult,'a+')
    fileBBXBufferRemove=open(fileBBXBuffer,'a+')
    fileResultRemove.close()
    fileBBXBufferRemove.close()
    os.remove(fileResult)
    os.remove(fileBBXBuffer)

    Result = os.path.join(cur_file_dir(), 'result.log')
    OpenResult=open(Result,'a+')
    OpenResult.close()

    for root, dirs, files in os.walk(cur_file_dir()):
        if files[0] == 'ReadBBXData_Tesla.py' :
            # merge(join) path and file
            file1 = os.path.join(cur_file_dir(), files[2])  # sys.argv[1] collect file
            f1 = open(file1, 'r', encoding='UTF-8', errors='ignore')
            file2 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
            f2=open(file2,'a+')
            f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

        else:
            file1 = os.path.join(cur_file_dir(), files[0])  # sys.argv[1] collect file
            f1 = open(file1, 'r', encoding='UTF-8', errors='ignore')
            file2 = os.path.join(cur_file_dir(), 'BBXDataBuffer.log')
            f2=open(file2,'a+')
            f3 = open(file1, 'r', encoding='UTF-8', errors='ignore')

    i=0
    j=0
    k=0
    FirstGPUBBXLoc=0
    SecondGPUBBXLoc=0
    for Line1 in f1:
        j=j+1
        if 'InfoRom Data' in Line1:
            i=i+1
        if 'Subsystem VID  :' in Line1:
            SubsLoc=j
        if 'InfoRom Data (GPU 0:0)' in Line1:
            FirstGPUBBXLoc=j
        if 'InfoRom Data (GPU 1:0):' in Line1:
            SecondGPUBBXLoc=j

    #For the size of BBXDataBuffer.log
    if i==1:
        for k in range (SubsLoc,FirstGPUBBXLoc + 1200):
            f2.write(str(linecache.getline(file1, k)))
    elif i==2:
        for k in range (SubsLoc,SecondGPUBBXLoc + 1200):
            f2.write(str(linecache.getline(file1, k)))

    #print(L2CacheErrorCount(1))


    #One GPU
    if i==1:
            print(BBXPrint(0))
            print(SN())
            print(PN())
            print(SKU())
            print(ECC(0))
            print(MemVendor(3))
            print(MemPN())
            if BBXDataLoc(0)>1:#If there are BBX data
                print(FieldTime(3))
                print(CalculateFieldTime(3))
                print(XID(3))
                print(Mods())
                print(Power(3))
                print(DayTemp(3))
                print(MonTemp(3))
                print(BlacklistedPages(3))
                print(FBErrorCount(3))
                print(TextureCacheErrors(3))
                print(RegisterErrorCounts(3))
                print(L1CacheErrorCount(3))
                print(L2CacheErrorCount(3))
                print(SHMCacheErrorCount(3))
            else:
                pass


    #Two GPUs
    if i==2:
        #1st GPU
        print(BBXPrint(0))
        print(SN())
        print(PN())
        print(SKU())
        print(ECC(0))
        print(MemVendor(1))
        print(MemPN())
        if BBXDataLoc(0) > 1:
            print(FieldTime(0))
            print(CalculateFieldTime(0))
            print(XID(0))
            print(Mods())
            print(Power(0))
            print(DayTemp(0))
            print(MonTemp(0))
            print(BlacklistedPages(0))
            print(FBErrorCount(0))
            print(TextureCacheErrors(0))
            print(RegisterErrorCounts(0))
            print(L1CacheErrorCount(0))
            print(L2CacheErrorCount(0))
            print(SHMCacheErrorCount(0))
        else:
            pass

        #2nd GPU
        print(BBXPrint(1))
        print(SN())
        print(PN())
        print(SKU())
        print(ECC(1))
        print(MemVendor(1))
        print(MemPN())
        if BBXDataLoc(1) > 1:
            print(FieldTime(1))
            print(CalculateFieldTime(1))
            print(XID(1))
            print(Mods())
            print(Power(1))
            print(DayTemp(1))
            print(MonTemp(1))
            print(BlacklistedPages(1))
            print(FBErrorCount(1))
            print(TextureCacheErrors(1))
            print(RegisterErrorCounts(1))
            print(L1CacheErrorCount(1))
            print(L2CacheErrorCount(1))
            print(SHMCacheErrorCount(1))
        else:
            pass


    f1.close()
    f2.close()
    os.remove(file2)

