import random
import time
import pickle

purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
biriuz = '\033[96m'
gray = '\033[1;30m'


white = '\033[0m'
black = '\033[30m'

fat = '\033[1m'
podck = '\033[4m'
fon = '\033[3m'
induss = '\033[11m'

redfon = '\033[41m'
greenfon = '\033[42m'
yellowfon = '\033[43m'
bluefon = '\033[44m'
purplefon = '\033[45m'
biriuzfon = '\033[46m'
grayfon = '\033[47m'


text1 = red+'[1]'+white
text2 = green+'[2]'+white
text3 = yellow+'[3]'+white
text4 = blue+'[4]'+white
text5 = purple+'[5]'+white
text6 = biriuz+'[6]'+white
text7 = white+'[7]'+white
text8 = gray+'[8]'+white

money = 700

def vop():
    global money
    global num
    global st
    num = input('На кого ставим? ')
    print("Сколько ставим? Всего", money, "$")
    st = input()
    if (int(st) > money) or (int(st) < 50):
        print("Минимальная ставка - 50$\nМаксимальная -", money, "$")
        vop()
    else:
        money -= int(st)
def vop2():
    print("Введите кол-во игроков")
    col = int(input())
    if 7 > col > 1:
        if col == 2:
            print("На кого ставит игрок 1?")
            num1 = int(input())
            print("Сколько ставит игрок 1?")
            st1 = int(input())
            print("На кого ставит игрок 2?")
            num2 = int(input())
            print("Сколько ставит игрок 2?")
            st2 = int(input())
def game():
    global money
    global st
    
    h1 = 1
    h2 = 1
    h3 = 1
    h4 = 1
    h5 = 1
    h6 = 1
    h7 = 1
    h8 = 1

    
    b = 0

    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0
    r7 = 0
    r8 = 0
    
    speed1 = random.randint(85, 100)
    speed2 = random.randint(85, 100)
    speed3 = random.randint(85, 100)
    speed4 = random.randint(85, 100)
    speed5 = random.randint(85, 100)
    speed6 = random.randint(85, 100)
    speed7 = random.randint(25, 55)
    speed8 = random.randint(25, 55)

    while True:
        r1 += h1
        r2 += h2
        r3 += h3
        r4 += h4
        r5 += h5
        r6 += h6
        r7 += h7
        r8 += h8
        
        os1 = '•--{'+num+'}---------------------------------•'
        os2 = '\n|                                      |'
        os3 = '\n|                                      |'
        os4 = '\n|                                      |'
        os5 = '\n|                                      |'
        os6 = '\n|                                      |'
        os7 = '\n|                                      |'
        os8 = '\n|                                      |'
        os9 = '\n|                                      |'
        os10 = '\n•--------------------------------------•'
        s1 = os1
        s2 = os2
        s3 = os3
        s4 = os4
        s5 = os5
        s6 = os6
        s7 = os7
        s8 = os8
        s9 = os9
        s10 = os10
        
        if 1 <= r1 <= 1*speed1:
            s2 = os2[:1]+text1+os2[4:]
        if 1*speed1 < r1 <= 2*speed1:
            s2 = os2[:2]+text1+os2[5:]        
        if 2*speed1 < r1 <= 3*speed1:
            s2 = os2[:3]+text1+os2[6:]        
        if 3*speed1 < r1 <= 4*speed1:
            s2 = os2[:4]+text1+os2[7:]            
        if 4*speed1 < r1 <= 5*speed1:
            s2 = os2[:5]+text1+os2[8:]        
        if 5*speed1 < r1 <= 6*speed1:
            s2 = os2[:6]+text1+os2[9:]  
            h1 = random.randint(1, 3)             
        if 6*speed1 < r1 <= 7*speed1:
            s2 = os2[:7]+text1+os2[10:]            
        if 7*speed1 < r1 <= 8*speed1:
            s2 = os2[:8]+text1+os2[11:]        
        if 8*speed1 < r1 <= 9*speed1:
            s2 = os2[:9]+text1+os2[12:]        
        if 9*speed1 < r1 <= 10*speed1:
            s2 = os2[:10]+text1+os2[13:]            
        if 10*speed1 < r1 <= 11*speed1:
            s2 = os2[:11]+text1+os2[14:] 
            h1 = random.randint(1, 3)
        if 11*speed1 < r1 <= 12*speed1:
            s2 = os2[:12]+text1+os2[15:]        
        if 12*speed1 < r1 <= 13*speed1:
            s2 = os2[:13]+text1+os2[16:]        
        if 13*speed1 < r1 <= 14*speed1:
            s2 = os2[:14]+text1+os2[17:]        
        if 14*speed1 < r1 <= 15*speed1:
            s2 = os2[:15]+text1+os2[18:]            
        if 15*speed1 < r1 <= 16*speed1:
            s2 = os2[:16]+text1+os2[19:]
            h1 = random.randint(1, 3)
        if 16*speed1 < r1 <= 17*speed1:
            s2 = os2[:17]+text1+os2[20:]        
        if 17*speed1 < r1 <= 18*speed1:
            s2 = os2[:18]+text1+os2[21:]            
        if 18*speed1 < r1 <= 19*speed1:
            s2 = os2[:19]+text1+os2[22:]        
        if 19*speed1 < r1 <= 20*speed1:
            s2 = os2[:20]+text1+os2[23:]        
        if 20*speed1 < r1 <= 21*speed1:
            s2 = os2[:21]+text1+os2[24:]  
            h1 = random.randint(1, 3)
        if 21*speed1 < r1 <= 22*speed1:
            s2 = os2[:22]+text1+os2[25:]        
        if 22*speed1 < r1 <= 23*speed1:
            s2 = os2[:23]+text1+os2[26:]
        if 23*speed1 < r1 <= 24*speed1:
            s2 = os2[:24]+text1+os2[27:]        
        if 24*speed1 < r1 <= 25*speed1:
            s2 = os2[:25]+text1+os2[28:]        
        if 25*speed1 < r1 <= 26*speed1:
            s2 = os2[:26]+text1+os2[29:]
            h1 = random.randint(1, 3)
        if 26*speed1 < r1 <= 27*speed1:
            s2 = os2[:27]+text1+os2[30:]        
        if 27*speed1 < r1 <= 28*speed1:
            s2 = os2[:28]+text1+os2[31:]        
        if 28*speed1 < r1 <= 29*speed1:
            s2 = os2[:29]+text1+os2[32:]            
        if 29*speed1 < r1 <= 30*speed1:
            s2 = os2[:30]+text1+os2[33:]        
        if 30*speed1 < r1 <= 31*speed1:
            s2 = os2[:31]+text1+os2[34:]
            h1 = random.randint(1, 3)
        if 31*speed1 < r1 <= 32*speed1:
            s2 = os2[:32]+text1+os2[35:]            
        if 32*speed1 < r1 <= 33*speed1:
            s2 = os2[:33]+text1+os2[36:]        
        if 33*speed1 < r1 <= 34*speed1:
            s2 = os2[:34]+text1+os2[37:]        
        if 34*speed1 < r1 <= 35*speed1:
            s2 = os2[:35]+text1+os2[38:]  
            h1 = random.randint(1, 3)
        if 35*speed1 < r1 <= 36*speed1:
            s2 = os2[:36]+text1+os2[39:]        
        if 36*speed1 < r1 <= 37*speed1:
            s2 = os2[:37]+text1+os2[40:] 
            b = 1       
            vin = 1    
    
        if 1 <= r2 <= 1*speed2:
            s3 = os3[:1]+text2+os3[4:]
        if 1*speed2 < r2 <= 2*speed2:
            s3 = os3[:2]+text2+os3[5:]        
        if 2*speed2 < r2 <= 3*speed2:
            s3 = os3[:3]+text2+os3[6:]        
        if 3*speed2 < r2 <= 4*speed2:
            s3 = os3[:4]+text2+os3[7:]            
        if 4*speed2 < r2 <= 5*speed2:
            s3 = os3[:5]+text2+os3[8:]        
        if 5*speed2 < r2 <= 6*speed2:
            s3 = os3[:6]+text2+os3[9:]  
            h2 = random.randint(1, 3)
        if 6*speed2 < r2 <= 7*speed2:
            s3 = os3[:7]+text2+os3[10:]            
        if 7*speed2 < r2 <= 8*speed2:
            s3 = os3[:8]+text2+os3[11:]        
        if 8*speed2 < r2 <= 9*speed2:
            s3 = os3[:9]+text2+os3[12:]        
        if 9*speed2 < r2 <= 10*speed2:
            s3 = os3[:10]+text2+os3[13:]            
        if 10*speed2 < r2 <= 11*speed2:
            s3 = os3[:11]+text2+os3[14:]
            h2 = random.randint(1, 3)
        if 11*speed2 < r2 <= 12*speed2:
            s3 = os3[:12]+text2+os3[15:]        
        if 12*speed2 < r2 <= 13*speed2:
            s3 = os3[:13]+text2+os3[16:]        
        if 13*speed2 < r2 <= 14*speed2:
            s3 = os3[:14]+text2+os3[17:]        
        if 14*speed2 < r2 <= 15*speed2:
            s3 = os3[:15]+text2+os3[18:]            
        if 15*speed2 < r2 <= 16*speed2:
            s3 = os3[:16]+text2+os3[19:]
            h2 = random.randint(1, 3)      
        if 16*speed2 < r2 <= 17*speed2:
            s3 = os3[:17]+text2+os3[20:]        
        if 17*speed2 < r2 <= 18*speed2:
            s3 = os3[:18]+text2+os3[21:]            
        if 18*speed2 < r2 <= 19*speed2:
            s3 = os3[:19]+text2+os3[22:]        
        if 19*speed2 < r2 <= 20*speed2:
            s3 = os3[:20]+text2+os3[23:]        
        if 20*speed2 < r2 <= 21*speed2:
            s3 = os3[:21]+text2+os3[24:]
            h2 = random.randint(1, 3)
        if 21*speed2 < r2 <= 22*speed2:
            s3 = os3[:22]+text2+os3[25:]        
        if 22*speed2 < r2 <= 23*speed2:
            s3 = os3[:23]+text2+os3[26:]
        if 23*speed2 < r2 <= 24*speed2:
            s3 = os3[:24]+text2+os3[27:]        
        if 24*speed2 < r2 <= 25*speed2:
            s3 = os3[:25]+text2+os3[28:]        
        if 25*speed2 < r2 <= 26*speed2:
            s3 = os3[:26]+text2+os3[29:]   
            h2 = random.randint(1, 3)        
        if 26*speed2 < r2 <= 27*speed2:
            s3 = os3[:27]+text2+os3[30:]        
        if 27*speed2 < r2 <= 28*speed2:
            s3 = os3[:28]+text2+os3[31:]        
        if 28*speed2 < r2 <= 29*speed2:
            s3 = os3[:29]+text2+os3[32:]            
        if 29*speed2 < r2 <= 30*speed2:
            s3 = os3[:30]+text2+os3[33:]        
        if 30*speed2 < r2 <= 31*speed2:
            s3 = os3[:31]+text2+os3[34:] 
            h2 = random.randint(1, 3)     
        if 31*speed2 < r2 <= 32*speed2:
            s3 = os3[:32]+text2+os3[35:]            
        if 32*speed2 < r2 <= 33*speed2:
            s3 = os3[:33]+text2+os3[36:]        
        if 33*speed2 < r2 <= 34*speed2:
            s3 = os3[:34]+text2+os3[37:]        
        if 34*speed2 < r2 <= 35*speed2:
            s3 = os3[:35]+text2+os3[38:] 
            h2 = random.randint(1, 3)      
        if 35*speed2 < r2 <= 36*speed2:
            s3 = os3[:36]+text2+os3[39:]        
        if 36*speed2 < r2 <= 37*speed2:
            s3 = os3[:37]+text2+os3[40:] 
            b = 1    
            vin = 2   
        
        if 1 <= r3 <= 1*speed3:
            s4 = os4[:1]+text3+os4[4:]
        if 1*speed3 < r3 <= 2*speed3:
            s4 = os4[:2]+text3+os4[5:]        
        if 2*speed3 < r3 <= 3*speed3:
            s4 = os4[:3]+text3+os4[6:]        
        if 3*speed3 < r3 <= 4*speed3:
            s4 = os4[:4]+text3+os4[7:]            
        if 4*speed3 < r3 <= 5*speed3:
            s4 = os4[:5]+text3+os4[8:]        
        if 5*speed3 < r3 <= 6*speed3:
            s4 = os4[:6]+text3+os4[9:]  
            h3 = random.randint(1, 3)             
        if 6*speed3 < r3 <= 7*speed3:
            s4 = os4[:7]+text3+os4[10:]            
        if 7*speed3 < r3 <= 8*speed3:
            s4 = os4[:8]+text3+os4[11:]        
        if 8*speed3 < r3 <= 9*speed3:
            s4 = os4[:9]+text3+os4[12:]        
        if 9*speed3 < r3 <= 10*speed3:
            s4 = os4[:10]+text3+os4[13:]            
        if 10*speed3 < r3 <= 11*speed3:
            s4 = os4[:11]+text3+os4[14:] 
            h3 = random.randint(1, 3)
        if 11*speed3 < r3 <= 12*speed3:
            s4 = os4[:12]+text3+os4[15:]        
        if 12*speed3 < r3 <= 13*speed3:
            s4 = os4[:13]+text3+os4[16:]        
        if 13*speed3 < r3 <= 14*speed3:
            s4 = os4[:14]+text3+os4[17:]        
        if 14*speed3 < r3 <= 15*speed3:
            s4 = os4[:15]+text3+os4[18:]            
        if 15*speed3 < r3 <= 16*speed3:
            s4 = os4[:16]+text3+os4[19:]
            h3 = random.randint(1, 3)
        if 16*speed3 < r3 <= 17*speed3:
            s4 = os4[:17]+text3+os4[20:]        
        if 17*speed3 < r3 <= 18*speed3:
            s4 = os4[:18]+text3+os4[21:]            
        if 18*speed3 < r3 <= 19*speed3:
            s4 = os4[:19]+text3+os4[22:]        
        if 19*speed3 < r3 <= 20*speed3:
            s4 = os4[:20]+text3+os4[23:]        
        if 20*speed3 < r3 <= 21*speed3:
            s4 = os4[:21]+text3+os4[24:]  
            h3 = random.randint(1, 3)
        if 21*speed3 < r3 <= 22*speed3:
            s4 = os4[:22]+text3+os4[25:]        
        if 22*speed3 < r3 <= 23*speed3:
            s4 = os4[:23]+text3+os4[26:]
        if 23*speed3 < r3 <= 24*speed3:
            s4 = os4[:24]+text3+os4[27:]        
        if 24*speed3 < r3 <= 25*speed3:
            s4 = os4[:25]+text3+os4[28:]        
        if 25*speed3 < r3 <= 26*speed3:
            s4 = os4[:26]+text3+os4[29:]
            h3 = random.randint(1, 3)
        if 26*speed3 < r3 <= 27*speed3:
            s4 = os4[:27]+text3+os4[30:]        
        if 27*speed3 < r3 <= 28*speed3:
            s4 = os4[:28]+text3+os4[31:]        
        if 28*speed3 < r3 <= 29*speed3:
            s4 = os4[:29]+text3+os4[32:]            
        if 29*speed3 < r3 <= 30*speed3:
            s4 = os4[:30]+text3+os4[33:]        
        if 30*speed3 < r3 <= 31*speed3:
            s4 = os4[:31]+text3+os4[34:]
            h3 = random.randint(1, 3)
        if 31*speed3 < r3 <= 32*speed3:
            s4 = os4[:32]+text3+os4[35:]            
        if 32*speed3 < r3 <= 33*speed3:
            s4 = os4[:33]+text3+os4[36:]        
        if 33*speed3 < r3 <= 34*speed3:
            s4 = os4[:34]+text3+os4[37:]        
        if 34*speed3 < r3 <= 35*speed3:
            s4 = os4[:35]+text3+os4[38:]  
            h3 = random.randint(1, 3)
        if 35*speed3 < r3 <= 36*speed3:
            s4 = os4[:36]+text3+os4[39:]        
        if 36*speed3 < r3 <= 37*speed3:
            s4 = os4[:37]+text3+os4[40:] 
            b = 1       
            vin = 3  
        
        if 1 <= r4 <= 1*speed4:
            s5 = os5[:1]+text4+os5[4:]
        if 1*speed4 < r4 <= 2*speed4:
            s5 = os5[:2]+text4+os5[5:]        
        if 2*speed4 < r4 <= 3*speed4:
            s5 = os5[:3]+text4+os5[6:]        
        if 3*speed4 < r4 <= 4*speed4:
            s5 = os5[:4]+text4+os5[7:]            
        if 4*speed4 < r4 <= 5*speed4:
            s5 = os5[:5]+text4+os5[8:]        
        if 5*speed4 < r4 <= 6*speed4:
            s5 = os5[:6]+text4+os5[9:]  
            h4 = random.randint(1, 3)             
        if 6*speed4 < r4 <= 7*speed4:
            s5 = os5[:7]+text4+os5[10:]            
        if 7*speed4 < r4 <= 8*speed4:
            s5 = os5[:8]+text4+os5[11:]        
        if 8*speed4 < r4 <= 9*speed4:
            s5 = os5[:9]+text4+os5[12:]        
        if 9*speed4 < r4 <= 10*speed4:
            s5 = os5[:10]+text4+os5[13:]            
        if 10*speed4 < r4 <= 11*speed4:
            s5 = os5[:11]+text4+os5[14:] 
            h4 = random.randint(1, 3)
        if 11*speed4 < r4 <= 12*speed4:
            s5 = os5[:12]+text4+os5[15:]        
        if 12*speed4 < r4 <= 13*speed4:
            s5 = os5[:13]+text4+os5[16:]        
        if 13*speed4 < r4 <= 14*speed4:
            s5 = os5[:14]+text4+os5[17:]        
        if 14*speed4 < r4 <= 15*speed4:
            s5 = os5[:15]+text4+os5[18:]            
        if 15*speed4 < r4 <= 16*speed4:
            s5 = os5[:16]+text4+os5[19:]
            h4 = random.randint(1, 3)
        if 16*speed4 < r4 <= 17*speed4:
            s5 = os5[:17]+text4+os5[20:]        
        if 17*speed4 < r4 <= 18*speed4:
            s5 = os5[:18]+text4+os5[21:]            
        if 18*speed4 < r4 <= 19*speed4:
            s5 = os5[:19]+text4+os5[22:]        
        if 19*speed4 < r4 <= 20*speed4:
            s5 = os5[:20]+text4+os5[23:]        
        if 20*speed4 < r4 <= 21*speed4:
            s5 = os5[:21]+text4+os5[24:]  
            h4 = random.randint(1, 3)
        if 21*speed4 < r4 <= 22*speed4:
            s5 = os5[:22]+text4+os5[25:]        
        if 22*speed4 < r4 <= 23*speed4:
            s5 = os5[:23]+text4+os5[26:]
        if 23*speed4 < r4 <= 24*speed4:
            s5 = os5[:24]+text4+os5[27:]        
        if 24*speed4 < r4 <= 25*speed4:
            s5 = os5[:25]+text4+os5[28:]        
        if 25*speed4 < r4 <= 26*speed4:
            s5 = os5[:26]+text4+os5[29:]
            h4 = random.randint(1, 3)
        if 26*speed4 < r4 <= 27*speed4:
            s5 = os5[:27]+text4+os5[30:]        
        if 27*speed4 < r4 <= 28*speed4:
            s5 = os5[:28]+text4+os5[31:]        
        if 28*speed4 < r4 <= 29*speed4:
            s5 = os5[:29]+text4+os5[32:]            
        if 29*speed4 < r4 <= 30*speed4:
            s5 = os5[:30]+text4+os5[33:]        
        if 30*speed4 < r4 <= 31*speed4:
            s5 = os5[:31]+text4+os5[34:]
            h4 = random.randint(1, 3)
        if 31*speed4 < r4 <= 32*speed4:
            s5 = os5[:32]+text4+os5[35:]            
        if 32*speed4 < r4 <= 33*speed4:
            s5 = os5[:33]+text4+os5[36:]        
        if 33*speed4 < r4 <= 34*speed4:
            s5 = os5[:34]+text4+os5[37:]        
        if 34*speed4 < r4 <= 35*speed4:
            s5 = os5[:35]+text4+os5[38:]  
            h4 = random.randint(1, 3)
        if 35*speed4 < r4 <= 36*speed4:
            s5 = os5[:36]+text4+os5[39:]        
        if 36*speed4 < r4 <= 37*speed4:
            s5 = os5[:37]+text4+os5[40:] 
            b = 1       
            vin = 4  
    
        if 1 <= r5 <= 1*speed5:
            s6 = os6[:1]+text5+os6[4:]
        if 1*speed5 < r5 <= 2*speed5:
            s6 = os6[:2]+text5+os6[5:]        
        if 2*speed5 < r5 <= 3*speed5:
            s6 = os6[:3]+text5+os6[6:]        
        if 3*speed5 < r5 <= 4*speed5:
            s6 = os6[:4]+text5+os6[7:]            
        if 4*speed5 < r5 <= 5*speed5:
            s6 = os6[:5]+text5+os6[8:]        
        if 5*speed5 < r5 <= 6*speed5:
            s6 = os6[:6]+text5+os6[9:]  
            h5 = random.randint(1, 3)             
        if 6*speed5 < r5 <= 7*speed5:
            s6 = os6[:7]+text5+os6[10:]            
        if 7*speed5 < r5 <= 8*speed5:
            s6 = os6[:8]+text5+os6[11:]        
        if 8*speed5 < r5 <= 9*speed5:
            s6 = os6[:9]+text5+os6[12:]        
        if 9*speed5 < r5 <= 10*speed5:
            s6 = os6[:10]+text5+os6[13:]            
        if 10*speed5 < r5 <= 11*speed5:
            s6 = os6[:11]+text5+os6[14:] 
            h5 = random.randint(1, 3)
        if 11*speed5 < r5 <= 12*speed5:
            s6 = os6[:12]+text5+os6[15:]        
        if 12*speed5 < r5 <= 13*speed5:
            s6 = os6[:13]+text5+os6[16:]        
        if 13*speed5 < r5 <= 14*speed5:
            s6 = os6[:14]+text5+os6[17:]        
        if 14*speed5 < r5 <= 15*speed5:
            s6 = os6[:15]+text5+os6[18:]            
        if 15*speed5 < r5 <= 16*speed5:
            s6 = os6[:16]+text5+os6[19:]
            h5 = random.randint(1, 3)
        if 16*speed5 < r5 <= 17*speed5:
            s6 = os6[:17]+text5+os6[20:]        
        if 17*speed5 < r5 <= 18*speed5:
            s6 = os6[:18]+text5+os6[21:]            
        if 18*speed5 < r5 <= 19*speed5:
            s6 = os6[:19]+text5+os6[22:]        
        if 19*speed5 < r5 <= 20*speed5:
            s6 = os6[:20]+text5+os6[23:]        
        if 20*speed5 < r5 <= 21*speed5:
            s6 = os6[:21]+text5+os6[24:]  
            h5 = random.randint(1, 3)
        if 21*speed5 < r5 <= 22*speed5:
            s6 = os6[:22]+text5+os6[25:]        
        if 22*speed5 < r5 <= 23*speed5:
            s6 = os6[:23]+text5+os6[26:]
        if 23*speed5 < r5 <= 24*speed5:
            s6 = os6[:24]+text5+os6[27:]        
        if 24*speed5 < r5 <= 25*speed5:
            s6 = os6[:25]+text5+os6[28:]        
        if 25*speed5 < r5 <= 26*speed5:
            s6 = os6[:26]+text5+os6[29:]
            h5 = random.randint(1, 3)
        if 26*speed5 < r5 <= 27*speed5:
            s6 = os6[:27]+text5+os6[30:]        
        if 27*speed5 < r5 <= 28*speed5:
            s6 = os6[:28]+text5+os6[31:]        
        if 28*speed5 < r5 <= 29*speed5:
            s6 = os6[:29]+text5+os6[32:]            
        if 29*speed5 < r5 <= 30*speed5:
            s6 = os6[:30]+text5+os6[33:]        
        if 30*speed5 < r5 <= 31*speed5:
            s6 = os6[:31]+text5+os6[34:]
            h5 = random.randint(1, 3)
        if 31*speed5 < r5 <= 32*speed5:
            s6 = os6[:32]+text5+os6[35:]            
        if 32*speed5 < r5 <= 33*speed5:
            s6 = os6[:33]+text5+os6[36:]        
        if 33*speed5 < r5 <= 34*speed5:
            s6 = os6[:34]+text5+os6[37:]        
        if 34*speed5 < r5 <= 35*speed5:
            s6 = os6[:35]+text5+os6[38:]  
            h5 = random.randint(1, 3)
        if 35*speed5 < r5 <= 36*speed5:
            s6 = os6[:36]+text5+os6[39:]        
        if 36*speed5 < r5 <= 37*speed5:
            s6 = os6[:37]+text5+os6[40:] 
            b = 1       
            vin = 5  
            
        if 1 <= r6 <= 1*speed6:
            s7 = os7[:1]+text6+os7[4:]
        if 1*speed6 < r6 <= 2*speed6:
            s7 = os7[:2]+text6+os7[5:]        
        if 2*speed6 < r6 <= 3*speed6:
            s7 = os7[:3]+text6+os7[6:]        
        if 3*speed6 < r6 <= 4*speed6:
            s7 = os7[:4]+text6+os7[7:]            
        if 4*speed6 < r6 <= 5*speed6:
            s7 = os7[:5]+text6+os7[8:]        
        if 5*speed6 < r6 <= 6*speed6:
            s7 = os7[:6]+text6+os7[9:]  
            h6 = random.randint(1, 3)             
        if 6*speed6 < r6 <= 7*speed6:
            s7 = os7[:7]+text6+os7[10:]            
        if 7*speed6 < r6 <= 8*speed6:
            s7 = os7[:8]+text6+os7[11:]        
        if 8*speed6 < r6 <= 9*speed6:
            s7 = os7[:9]+text6+os7[12:]        
        if 9*speed6 < r6 <= 10*speed6:
            s7 = os7[:10]+text6+os7[13:]            
        if 10*speed6 < r6 <= 11*speed6:
            s7 = os7[:11]+text6+os7[14:] 
            h6 = random.randint(1, 3)
        if 11*speed6 < r6 <= 12*speed6:
            s7 = os7[:12]+text6+os7[15:]        
        if 12*speed6 < r6 <= 13*speed6:
            s7 = os7[:13]+text6+os7[16:]        
        if 13*speed6 < r6 <= 14*speed6:
            s7 = os7[:14]+text6+os7[17:]        
        if 14*speed6 < r6 <= 15*speed6:
            s7 = os7[:15]+text6+os7[18:]            
        if 15*speed6 < r6 <= 16*speed6:
            s7 = os7[:16]+text6+os7[19:]
            h6 = random.randint(1, 3)
        if 16*speed6 < r6 <= 17*speed6:
            s7 = os7[:17]+text6+os7[20:]        
        if 17*speed6 < r6 <= 18*speed6:
            s7 = os7[:18]+text6+os7[21:]            
        if 18*speed6 < r6 <= 19*speed6:
            s7 = os7[:19]+text6+os7[22:]        
        if 19*speed6 < r6 <= 20*speed6:
            s7 = os7[:20]+text6+os7[23:]        
        if 20*speed6 < r6 <= 21*speed6:
            s7 = os7[:21]+text6+os7[24:]  
            h6 = random.randint(1, 3)
        if 21*speed6 < r6 <= 22*speed6:
            s7 = os7[:22]+text6+os7[25:]        
        if 22*speed6 < r6 <= 23*speed6:
            s7 = os7[:23]+text6+os7[26:]
        if 23*speed6 < r6 <= 24*speed6:
            s7 = os7[:24]+text6+os7[27:]        
        if 24*speed6 < r6 <= 25*speed6:
            s7 = os7[:25]+text6+os7[28:]        
        if 25*speed6 < r6 <= 26*speed6:
            s7 = os7[:26]+text6+os7[29:]
            h6 = random.randint(1, 3)
        if 26*speed6 < r6 <= 27*speed6:
            s7 = os7[:27]+text6+os7[30:]        
        if 27*speed6 < r6 <= 28*speed6:
            s7 = os7[:28]+text6+os7[31:]        
        if 28*speed6 < r6 <= 29*speed6:
            s7 = os7[:29]+text6+os7[32:]            
        if 29*speed6 < r6 <= 30*speed6:
            s7 = os7[:30]+text6+os7[33:]        
        if 30*speed6 < r6 <= 31*speed6:
            s7 = os7[:31]+text6+os7[34:]
            h6 = random.randint(1, 3)
        if 31*speed6 < r6 <= 32*speed6:
            s7 = os7[:32]+text6+os7[35:]            
        if 32*speed6 < r6 <= 33*speed6:
            s7 = os7[:33]+text6+os7[36:]        
        if 33*speed6 < r6 <= 34*speed6:
            s7 = os7[:34]+text6+os7[37:]        
        if 34*speed6 < r6 <= 35*speed6:
            s7 = os7[:35]+text6+os7[38:]  
            h6 = random.randint(1, 3)
        if 35*speed6 < r6 <= 36*speed6:
            s7 = os7[:36]+text6+os7[39:]        
        if 36*speed6 < r6 <= 37*speed6:
            s7 = os7[:37]+text6+os7[40:] 
            b = 1       
            vin = 6 
        
        print("\n\n\n\n\n\n\n\n\n\n"+s1+s2+s3+s4+s5+s6+s7+s8+s9+s10)   
        if b == 1: 
            if int(num) == vin:
                print("Победа")
                money += int(st)*5
            else:
                print("Вы проиграли")
            print("У вас", money, "$")
            i = input("Играть Еще?")
            if i == '1':
                vop()
                game()
            else:
                break
        time.sleep(0.01)
    
print("1.Одиночка\n2.Кооператив")
riz = input()
if riz == '1':
    vop()
    game()

if riz == '2':
    vop2()
    game2()