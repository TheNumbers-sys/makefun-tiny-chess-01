import json,os,sys,urllib.request as u
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("x")
I=30000;L=90000
V=(0,100,320,330,500,900,0);a=(31,33,14,18,-31,-33,-14,-18);b=(1,-1,16,-16,15,17,-15,-17);c=(15,17,-15,-17);d=(1,-1,16,-16);O=((),(),a,c,d,c+d,b)
m={0:13,4:12,7:14,112:7,116:3,119:11}
p=("","PPPPUZZ<UKFPPPPdUUZiZZdn~~~~PPPP"," (22(<PU2UZ_2P_d2U_d2PZ_(<PP (22","<FFFFUPPFZZZFPZZFUUZFPUZFPPP<FFF","PPPUKPPPKPPPKPPPKPPPKPPPUZZZPPPP","<FFKFPUPFUUUPPUUKPUUFPUUFPPP<FFK","dnZPddPPF<<<<22(2(( 2(( 2(( 2(( "," 22222PP2Fdn2Fnx2Fnx2Fdn2<FP (2<")
f=(0,1,2,3,3,2,1,0);n=[0]
class X(Exception):pass
def P(o):
 f2=o.split();b=[0]*128;r=7;x=0
 for ch in f2[0]:
  if ch=="/":r-=1;x=0
  elif ch.isdigit():x+=int(ch)
  else:b[r*16+x]="PNBRQK".index(ch.upper())+1+(0 if ch.isupper() else 8);x+=1
 C=sum(v for k,v in(("K",1),("Q",2),("k",4),("q",8))if k in f2[2]);g=-1 if f2[3]=="-" else(int(f2[3][1])-1)*16+ord(f2[3][0])-97;w=k=-1;v=0
 for q,j in enumerate(b):
  if j==6:w=q
  elif j==14:k=q
  elif j and(j&7)not in(1,6):v+=V[j&7]
 return(b,1 if f2[1]=="b" else 0,C,g,w,k,v)
def A(b,s,w):
 o=0 if w else 8
 for x in((s-15,s-17)if w else(s+15,s+17)):
  if not(x&136)and b[x]==1+o:return 1
 for q in a+b:
  if not((s+q)&136)and b[s+q]==(2+o if q in a else 6+o):return 1
 for ds,pc in((c,3),(d,4)):
  for q in ds:
   x=s+q
   while not(x&136)and not b[x]:x+=q
   if not(x&136)and b[x]in(pc+o,5+o):return 1
 return 0
def G(s,cp=0):
 b,r,C,g,w,k,v=s;h=8 if r else 0;o=[];A2=o.append
 for q in range(128):
  if q&136:continue
  j=b[q]
  if not j or(j&8)!=h:continue
  T2=j&7
  if T2==1:
   D=16 if r==0 else-16;la=7 if r==0 else 0;T=q+D
   if not(T&136)and b[T]==0:
    for pr in((5,4,3,2)if(T>>4)==la else(0,)):A2(q|(T<<7)|(pr<<14))
    if not cp and(q>>4)==(1 if r==0 else 6)and b[q+2*D]==0:A2(q|((q+2*D)<<7))
   for dd in(D-1,D+1):
    T=q+dd
    if T&136:continue
    v2=b[T]
    if v2 and(v2&8)!=h:
     for pr in((5,4,3,2)if(T>>4)==la else(0,)):A2(q|(T<<7)|(pr<<14))
    elif T==g:A2(q|(T<<7))
  else:
   for dd in O[T2]:
    T=q+dd
    while not(T&136):
     v2=b[T]
     if v2:
      if(v2&8)!=h:A2(q|(T<<7))
      break
     if not cp:A2(q|(T<<7))
     if T2 not in(3,4,5):break
     T+=dd
   if T2==6 and not cp and q==(4 if r==0 else 116):
    kf=q
    for dd,bit in((2,1 if r==0 else 4),(-2,2 if r==0 else 8)):
     T=kf+dd
     if C&bit and all(b[x]==0 for x in((kf+1,kf+2)if dd>0 else(kf-1,kf-2,kf-3)))and all(not A(b,x,r==1)for x in((kf,kf+1,kf+2)if dd>0 else(kf,kf-1,kf-2))):A2(kf|(T<<7))
 return o
def M(s,mm):
 b,r,C,g,w,k,v=s;b=b[:];f=mm&127;T=(mm>>7)&127;pr=mm>>14;j=b[f];b[f]=0
 if(j&7)==1 and T==g and b[T]==0:b[T-16 if r==0 else T+16]=0
 if(j&7)==6 and abs(T-f)==2:
  if T>f:b[T-1]=b[T+1];b[T+1]=0
  else:b[T+1]=b[T-2];b[T-2]=0
 cp=b[T]
 if cp and(cp&7)not in(1,6):v-=V[cp&7]
 b[T]=(pr|(8 if r else 0))if pr else j
 if pr:v+=V[pr]
 C&=m.get(f,15)&m.get(T,15)
 if j==6:w=T
 elif j==14:k=T
 return(b,1-r,C,(f+T)//2 if(j&7)==1 and abs(T-f)==32 else-1,w,k,v)
def E(s):
 b,r,C,g,w,k,v=s;S=0
 for q in range(128):
  if q&136:continue
  j=b[q]
  if not j:continue
  T2=j&7;W=j<8;sq=q if W else q^112;tt=T2 if T2!=6 else(6 if v>2600 else 7);S+=(V[T2]+ord(p[tt][(sq>>4)*4+f[sq&7]])-80)*(1 if W else-1)
 return(S if r==0 else-S)+10
def O(s,ms):
 b=s[0]
 return sorted(ms,key=lambda mm:-(V[b[(mm>>7)&127]&7]*10 if b[(mm>>7)&127]else(1000 if(mm>>7)&127==s[3]else 0))-(900 if mm>>14 else 0))
def S(s,dp,al,be,pl):
 n[0]+=1
 if n[0]>L:raise X
 b,r,C,g,w,k,v=s;ch=A(b,w if r==0 else k,r==1)
 if dp<=0 and not ch:
  S2=E(s)
  if S2>=be:return be
  if S2>al:al=S2
 be2=-I;N=0
 for mm in O(s,G(s,not ch)if dp<=0 else G(s)):
  ns=M(s,mm)
  if A(ns[0],ns[4]if r==0 else ns[5],r==1):continue
  N+=1;sc=-S(ns,dp-1 if dp>0 else 0,-be,-al,pl+1)
  if sc>be2:be2=sc
  if sc>al:al=sc
  if al>=be:return be2
 if N==0:
  if ch:return-I+pl
  return 0 if dp>0 else al
 return be2 if dp>0 else al
def U(mm):
 f=mm&127;T=(mm>>7)&127;return"abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[T&7]+str((T>>4)+1)+("nbrq"[(mm>>14)-2]if mm>>14 else"")
def F(u2):
 f=(int(u2[1])-1)*16+ord(u2[0])-97;T=(int(u2[3])-1)*16+ord(u2[2])-97;pr=0
 if len(u2)==5:pr="nbrq".index(u2[4])+2
 return f|(T<<7)|(pr<<14)
def C(o,lg):
 s=P(o);mv=[F(u2)for u2 in lg];n[0]=0;od=mv[:];be=mv[0]
 for d in range(1,16):
  try:
   sc=[]
   for mm in od:sc.append((S(M(s,mm),d-1,-I,I,1),mm))
   sc.sort();be=sc[0][1];od=[mm for _,mm in sc]
  except X:break
 return U(be)
def R(pa,bo):
 q=u.Request(E+pa,data=json.dumps(bo).encode(),headers={"content-type":"application/json"})
 with u.urlopen(q)as r:return json.load(r)
def main():
 while 1:
  g=R("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":g=R("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])})
if __name__=="__main__":main()
