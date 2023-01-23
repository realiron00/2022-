import sys
import os.path

def Invsie(file_hex, time):
    
    if time%3==0:
        if file_hex==0:
            result=255
        else:
            result=file_hex-1
            
    if time%3==1:
        if file_hex==0:
            result=254
        elif file_hex==1:
            result=255
        else:
            result=file_hex-2
            
    if time%3==2:
        if file_hex==0:
            result=253
        elif file_hex==1:
            result=254
        elif file_hex==2:
            result=255
        else:
            result=file_hex-3
            
    return result

def Invcet(f, h):
    f_name=os.path.splitext(f)
    
    if h[0:4]==[37, 80, 68, 70]:
        os.rename(f, f_name[0]+'.pdf')
        
    elif h[0:8]==[137, 80, 78, 71, 13, 10, 26, 10]:
        os.rename(f, f_name[0]+'.png')
        
    elif h[0:8]==[208, 207, 17, 224, 161, 177, 26, 225]:
        os.rename(f, f_name[0]+'.hwp')
        
    elif h[0:3]== [255, 216, 255]:
        os.rename(f, f_name[0]+'.jpg')
        
    elif h[0:3]==[73, 68, 51]:
        os.rename(f, f_name[0]+'.mp3')
        
    elif h[0:8]==[0, 0, 0, 24, 102, 116, 121, 112]:
        os.rename(f, f_name[0]+'.mp4')
        
    elif h[0:4]==[80, 75, 3, 4]:
        if h[4:8]==[20, 0, 6, 0]:
            os.rename(f, f_name[0]+'.pptx')
        else:
            os.rename(f, f_name[0]+'.zip')
            
    else: print("확장자 오류!")

lfile=["해시함수_SHA256_소스코드_활용_매뉴얼.0",
      "해석학에서.0",
      "팀팀클래스_찐찐찐막.0",
      "키.0",
      "제출용.0",
      "잉리_PPT.0",
      "우리서버강아지는머리3개커버로스.0",
      "시스템_로그_조사.0",
      "미국_연방형사소송규칙_원문본.0",
      "뚱이.0",
      "Ragnar_랜섬웨어_복구도구_사용_매뉴얼.0",
      "Ragnar_Ransomware_Decryption_Tool.0",
      "Mario_Voice.0",
      "Lu.0",
      "Hive_랜섬웨어_통합_복구도구_사용_매뉴얼.0",
      "Hive_Ransomware_Integrated_Decryption_Tool.0",
      "FAT32_20182222박세준.0",
      "20220723_FaS_20192243_이용진.0",
      "[1]_SEED_Algorithm_Specification_korean_M.0"]

D_hex=[]
for i in range(len(lfile)):
    with open(lfile[i], mode='r+b') as file:
        binary=file.read()
        
        for j in range(len(binary)):
            result=Invsie(binary[j], i)
            D_hex.append(result)
            
        file.seek(0)
        file.write(bytes(D_hex))
        
    Invcet(lfile[i], D_hex)
    D_hex=[]