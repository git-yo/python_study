pro = {'guizhou':'guizhou','guangdong':'guangdong'}
city = {'guizhou':['guiyang','qainnan'],'guangdong':['guangzhou','shengzhen']}
area = {'guiyang':['huaxi','nanming','xiaohe'],'shengzhen':['nanshan','futian','longhua']}

print(pro.keys())
_pro = input('Please enter your pro or enter back to go meau: ')
while _pro == 'back':
    print(pro.keys())
    _pro = input('Please enter your pro: ')
    if _pro == pro[_pro]:
        print(city[_pro])
        _city = in
        put('Please enter your city or enter back to go meau: ')

else:
     print(city[_pro])
     _city = input('Please enter your city or enter back to go meau: ')
     while _city == 'back':
         print(pro.keys())
         _pro = input('Please enter your pro  or enter back to go meau: ')
         if _pro == pro[_pro]:
            print (city[_pro])
            _city = input('Please enter your city : ')
            if _city == city[_city]:
               print(area[_city])
               _area = input('Please enter your area')
        
     else:
         print (area[_city])
         _area = input('Please enter your area : ')
         while _area == 'back':
            print(city[_pro])
            _city = input('Please enter your city or enter back to go meau: ')
    #    else:
    #        print ('Your address is: ',_pro,'省',_city,'市/县',_area,'区')


