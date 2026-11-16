import json,os,urllib.request as u
H=os.environ["MAKEFUN_ENV_URL"]
I=30000;L=9e4
V=(0,100,320,330,500,900,0);c=(15,17,-15,-17);d=(1,-1,16,-16);a=(31,33,14,18,-31,-33,-14,-18);O=(a,c,d,c+d,d+c);Q=(5,4,3,2)
m={0:13,4:12,7:14,112:7,116:3,119:11}
p="PPPPUZZ<UKFPPPPdUUZiZZdn~~~~PPPP (22(<PU2UZ_2P_d2U_d2PZ_(<PP (22<FFFFUPPFZZZFPZZFUUZFPUZFPPP<FFFPPPUKPPPKPPPKPPPKPPPKPPPUZZZPPPP<FFKFPUPFUUUPPUUKPUUFPUUFPPP<FFKdnZPddPPF<<<<22(2(( 2(( 2(( 2(( "
X=Exception
n=[0];T={}
def P(o):
 p2,t,c2,e2=o.split()[:4];b=[0]*128;r=7;x=0
 for ch in p2:
  if ch=="/":r-=1;x=0
  elif ch.isdigit():x+=int(ch)
  else:b[r*16+x]="PNBRQK".index(ch.upper())+1+8*(ch>"Z");x+=1
 C=sum(1<<"KQkq".index(k)for k in c2 if k!="-");g=(int(e2[1])-1)*16+ord(e2[0])-97 if"-"!=e2 else-1;w=k=-1
 for q,j in enumerate(b):
  if j==6:w=q
  elif j==14:k=q
 return(b,1 if t=="b" else 0,C,g,w,k)
def A(B,s,w):
 o=8-8*w;e=16-32*w
 for x in(s+e-1,s+e+1):
  if x&136<1 and B[x]==1+o:return 1
 for q in a+d+c:
  if(s+q)&136<1 and B[s+q]==(2+o if q in a else 6+o):return 1
 for ds,pc in((c,3),(d,4)):
  for q in ds:
   x=s+q
   while x&136<1 and not B[x]:x+=q
   if x&136<1 and B[x]in(pc+o,5+o):return 1
 return 0
def G(s,cp=0):
 b,r,C,g,w,k=s;o=[];A2=o.append
 for q in range(128):
  if q&136:continue
  j=b[q]
  if not j or j>>3!=r:continue
  T2=j&7
  if T2==1:
   D=16-32*r;la=7-7*r;Q2=Q if(q+D>>4)==la else(0,)*(not cp);T=q+D
   if T&136<1 and b[T]==0:
    for pr in Q2:A2(q|(T<<7)|(pr<<14))
    if not cp and(q>>4)==1+5*r and b[T+D]==0:A2(q|((T+D)<<7))
   for T in(q+D-1,q+D+1):
    if T&136:continue
    v2=b[T]
    if v2 and v2>>3!=r:
     for pr in(Q if(T>>4)==la else(0,)):A2(q|(T<<7)|(pr<<14))
    elif T==g:A2(q|(T<<7))
  else:
   for dd in O[T2-2]:
    T=q+dd
    while T&136<1:
     v2=b[T]
     if v2:
      if v2>>3!=r:A2(q|(T<<7))
      break
     if not cp:A2(q|(T<<7))
     if T2 in(2,6):break
     T+=dd
   if T2==6 and not cp and q==4+112*r:
    for dd,bit in((2,1+3*r),(-2,2+6*r)):
     T=q+dd
     if C&bit and all(not b[x]for x in((q+1,q+2)if dd>0 else(q-1,q-2,q-3)))and not A(b,q,r)and not A(b,q+dd//2,r)and not A(b,T,r):A2(q|(T<<7))
 return o
def M(s,mm):
 b,r,C,g,w,k=s;b=b[:];f=mm&127;T=mm>>7&127;pr=mm>>14;j=b[f];b[f]=0
 if j&7==1 and T==g and b[T]==0:b[T-16+32*r]=0
 if j&7==6 and abs(T-f)==2:
  if T>f:b[T-1]=b[T+1];b[T+1]=0
  else:b[T+1]=b[T-2];b[T-2]=0
 b[T]=(pr|8*r)if pr else j
 C&=m.get(f,15)&m.get(T,15)
 if j==6:w=T
 elif j==14:k=T
 return(b,1-r,C,(f+T)//2 if j&7==1 and abs(T-f)==32 else-1,w,k)
def E(s):
 b,r,C,g,w,k=s;S=0
 for q,j in enumerate(b):
  if q&136 or not j:continue
  T2=j&7;sq=q^112*(j>7);S+=(V[T2]+ord(p[T2*32-32+(sq>>2&28)+min(sq&7,7-(sq&7))])-80)*(2*(j<8)-1)
 return 10+S*(1-2*r)
def Z(s,ms,t):
 b=s[0]
 return sorted(ms,key=lambda mm:-(1e5*(mm==t)+V[b[mm>>7&127]&7]+900*(mm>>14)))
def S(s,dp,al,be,z):
 n[0]+=1
 if n[0]>L:raise X
 b,r,C,g,w,k=s;ch=A(b,(w,k)[r],r)
 if dp<=0 and not ch:
  al=max(al,E(s))
  if al>=be:return be
 if z*dp>2 and not ch:
  sc=-S((b,1-r,C,0,w,k),dp-3,-be,-be+1,0)
  if sc>=be:return be
 y=bytes(b);t=T.get(y,0);be2=-I;bm=0
 for mm in Z(s,G(s,dp<1 and 1-ch),t):
  ns=M(s,mm)
  if A(ns[0],ns[4+r],r):continue
  sc=-S(ns,max(dp-1,0),-be,-al,1)
  if sc>be2:be2=sc;bm=mm
  al=max(al,sc)
  if al>=be:T[y]=bm;return be2
 if be2==-I:
  if ch:return-I
  return al*(dp<=0)
 T[y]=bm
 return(be2,al)[dp<=0]
def U(mm):
 f=mm&127;T=mm>>7&127;q=mm>>14;return"%c%d%c%d%s"%(97+(f&7),(f>>4)+1,97+(T&7),(T>>4)+1,"nbrq"[q-2]if q else"")
def F(u2):
 f,T=[(int(u2[i])-1)<<4|ord(u2[i-1])-97 for i in(1,3)];pr=0
 if u2[4:]:pr="nbrq".find(u2[4])+2
 return f|(T<<7)|(pr<<14)
def C(o,lg):
 s=P(o);mv=[F(u2)for u2 in lg];n[0]=0;T.clear();od=mv;be=mv[0]
 for d in range(9):
  try:
   sc=sorted((S(M(s,mm),d,-I,I,1),mm)for mm in od);be=sc[0][1];od=[x[1]for x in sc]
  except X:break
 return U(be)
def R(pa,bo):
 return json.load(u.urlopen(H+pa,json.dumps(bo).encode()))
def main():
 while 1:
  g=R("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":g=R("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])})
if __name__[0]=="_":main()
