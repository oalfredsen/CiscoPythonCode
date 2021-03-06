#Python versjon 3
#Cisco AP bulk config generator versjon 1.0

import itertools

print (" ")
print ("Hello and welcome to Cisco AP bulk config generator!!")
print (" ")
ap_usr_input = input("Please paste in ap names seperated by comma e.g APNAME001,APNAME002,APNAME003: ")
mac_usr_input = input("Please paste in mac addresses seperated by comma e.g 000000000000,aaaaaaaaaaaa,dddddddddddd:")
print (" ")
print ("Step.1 set AP name to mac: ")
print (" ")
ap_list = ap_usr_input.split(",")
mac_list = mac_usr_input.split(",")
wlc_ap_name_list = ['config ap name']
ap2mac_list = [None] * (len(ap_list)+len(ap_list))
ap2mac_list[::2] = ap_list
ap2mac_list[1::2] = mac_list
number=1
size=2
wlc_conf_ap_mac_list=len(ap2mac_list)+(len(ap2mac_list)/size)*number*len(wlc_ap_name_list)
i=0
while i<wlc_conf_ap_mac_list:
    i+=size
    for times in range(number):
        for elem in wlc_ap_name_list:
            ap2mac_list.insert(i,elem)
        i+=len(wlc_ap_name_list)
ap2mac_list.insert(0, 'config ap name')
ap2mac_list.pop()

from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

for i in grouper(ap2mac_list,3):
    print (str(" ".join(i)))

print (" ")
input("Press enter to continue")
print (" ")
print ("Step.2 Config for AP mode and group. This will require AP reboot so check that ap is up before running config from step.3: ")
print (" ")

conf_ap_mode_list = ['config ap mode flexconnect submode none ']
conf_ap_group_list = ['config ap group-name XXX']#replace XXX with group name
enter_yes_list = ['y']

for ap_mode in (conf_ap_mode_list):
    for ap in (ap_list):
        for ap_group in (conf_ap_group_list):
            for yes in (enter_yes_list):
              print (((ap_mode) + (ap)) + '\n' + ((ap_group) + (ap)) + '\n' + (yes))

print (" ")
input("Press enter to continue")
print (" ")
print ("Step.3 Config for AP connection and vlan: ")
print (" ")
print (" ")
conf_ap_disable = ['config ap disable ']
conf_ap_flex_vlan_en = ['config ap flexconnect vlan enable ']
conf_ap_flex_vlan_native = ['config ap flexconnect vlan native XX '] #replace XX with native vlan
conf_ap_flex_vlan_wlan = ['config ap flexconnect vlan wlan XX ']#replace XX with vlan
conf_ap_enable = ['config ap enable ']

for ap_disable in (conf_ap_disable):
    for ap3 in (ap_list):
        for c_ap_flex_v_en in (conf_ap_flex_vlan_en):
            for c_ap_flex_vlan_n in (conf_ap_flex_vlan_native):
                for c_ap_flex_v_w in (conf_ap_flex_vlan_wlan):
                    for c_ap_en in (conf_ap_enable):
                        print (((ap_disable) + (ap3)) + '\n' + ((c_ap_flex_v_en) + (ap3)) + '\n' + ((c_ap_flex_vlan_n) + (ap3)) + '\n' + ((c_ap_flex_v_w) + (ap3)) + '\n' + ((c_ap_en) + (ap3)))




print('')
print('')
input("Press enter to continue")
print('')
primary_wlc = input ("Step.4 Please type short name of primary controller, e.g wlc01 : ")
print('')
secondary_wlc = input ("Step.5 Please type short name of secondary controller, e.g wlc02 : ")

conf_ap_primary_list = ['config ap primary-base']
conf_ap_secondary_list = ['config ap secondary-base']







#-------------Primary controllers-------------------------
wlc01_list = [' wlc01 '] #name of controller
wlc01_ip_lst = [' X.X.X.X'] #replace X with IP adr
wlc02_list = [' wlc02 ']#name of controller
wlc02_ip_lst = [' X.X.X.X']#replace X with IP adr
wlc03_list = [' wlc03 ']#name of controller
wlc03_ip_lst = [' X.X.X.X']#replace X with IP adr
wlc04_list = [' wlc04 ']#name of controller
wlc04_ip_lst = [' X.X.X.X']#replace X with IP adr
wlc05_list = [' wlc05 ']#name of controller
wlc05_ip_lst = [' X.X.X.X']#replace X with IP adr


#----------------Secondary controllers-------------
wlc11_HA_list = [' wlc11-HA ']#name of controller
wlc11_HA_ip_lst = [' X.X.X.X']#replace X with IP adr
wlc12_HA_list = [' wlc12-HA ']#name of controller
wlc12_HA_ip_lst = [' X.X.X.X']#replace X with IP adr



print('')
print('Step.6 Final config:')
print('')
if primary_wlc == ('wlc01'):
   for ap_primary in (conf_ap_primary_list):
       for wlc01_name in (wlc01_list):
           for ip_adr in (wlc01_ip_lst):
             for ap in (ap_list):
                print ((ap_primary) + (wlc01_name) + (ap) + (ip_adr))

if primary_wlc == ('wlc02'):
   for ap_primary in (conf_ap_primary_list):
       for wlc02_name in (wlc02_list):
           for ip_adr in (wlc02_ip_lst):
             for ap in (ap_list):
                print ((ap_primary) + (wlc02_name) + (ap) + (ip_adr))

if primary_wlc == ('wlc03'):
   for ap_primary in (conf_ap_primary_list):
       for wlc03_name in (wlc03_list):
           for ip_adr in (wlc03_ip_lst):
             for ap in (ap_list):
                print ((ap_primary) + (wlc03_name) + (ap) + (ip_adr))

if primary_wlc == ('wlc04'):
   for ap_primary in (conf_ap_primary_list):
       for wlc04_name in (wlc04_list):
           for ip_adr in (wlc04_ip_lst):
             for ap in (ap_list):
                print ((ap_primary) + (wlc04_name) + (ap) + (ip_adr))

if primary_wlc == ('wlc05'):
   for ap_primary in (conf_ap_primary_list):
       for wlc05_name in (wlc05_list):
           for ip_adr in (wlc05_ip_lst):
             for ap in (ap_list):
                print ((ap_primary) + (wlc05_name) + (ap) + (ip_adr))

i
#----------------Secondary WLC-----------------

if secondary_wlc == ('wlc11-HA'):
   for ap_secondary in (conf_ap_secondary_list):
       for wlc11_HA_name in (wlc11_HA_list):
           for ip_adr in (wlc11_HA_ip_lst):
             for ap in (ap_list):
                print ((ap_secondary) + (wlc11_HA_name) + (ap) + (ip_adr))

if secondary_wlc == ('wlc12-HA'):
   for ap_secondary in (conf_ap_secondary_list):
       for wlc12_HA_name in (wlc12_HA_list):
           for ip_adr in (wlc12_HA_ip_lst):
             for ap in (ap_list):
                print ((ap_secondary) + (wlc12_HA_name) + (ap) + (ip_adr))




print('')
print('')
print('')

