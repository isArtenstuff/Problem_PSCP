"""Rectangle Area"""

fir_rect = input()
fir_width = int(fir_rect.split()[2])
fir_height = int(fir_rect.split()[3])
fir_Ll = (int(fir_rect.split()[0]),int(fir_rect.split()[1]))
fir_Ur = (int(fir_rect.split()[0])+fir_width,int(fir_rect.split()[1])+fir_height)

sec_rect = input()
sec_width = int(sec_rect.split()[2])
sec_height = int(sec_rect.split()[3])
sec_Ll = (int(sec_rect.split()[0]),int(sec_rect.split()[1]))
sec_Ur = (int(sec_rect.split()[0])+sec_width,int(sec_rect.split()[1])+sec_height)

OVERLAP_L = max(fir_Ll[0], sec_Ll[0])
OVERLAP_R = min(fir_Ur[0], sec_Ur[0])
OVERLAP_BOT = max(fir_Ll[1], sec_Ll[1])
OVERLAP_TOP = min(fir_Ur[1], sec_Ur[1])

if fir_Ll[0]<sec_Ur[0] and sec_Ll[0]<fir_Ur[0] and fir_Ll[1]<sec_Ur[1] and sec_Ll[1]<fir_Ur[1]:
    overlap_area = (OVERLAP_R - OVERLAP_L) * (OVERLAP_TOP - OVERLAP_BOT)
    print(overlap_area)
else:
    print("no overlapping")
