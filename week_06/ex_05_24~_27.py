##------------------------------------------------------------------
##컴퓨터 시스템과 1학년 B반 202345050 차혜진 5장 과제물
##------------------------------------------------------------------
print("-"*160)
print("컴퓨터 시스템과 1학년 B반 202345050 차혜진 5장 과제물")
a=[101,102,['One','Two','Three'],103,104,105]
print("="*160)
print("리스트 a=[101,102,['One','Two','Three'],103,104,105]일 때 a[1:4]의 결과 값 : ",a[1:4])
a=[88,35,97,35,88]
print(" ")
print("리스트 [88,35,97,35,88]에서 a.remove(35) 했을 때 결과 값 : ",a[1:4])
tp=(101,102,'one','two')
print(" ")
print("튜플 tp=(101,102,'one','two')에서 tp[2:]의 결과 값 : ",tp[2:])
a={101:'smart'}
a[201]='graphic'
print(" ")
print("딕셔너리 a={101:'smart'}에 '201:graphic'을 추가한 후 결과 값 : ",a)
b={101:'coding','id':'python'}
del b['id']
print(" ")
print("딕셔너리 b={101:'coding','id':'python'}일 경우 'id':'python'을 삭제 후 결과 값 : ",b)
c={'id':'hjin','pw':345050,'email':'202345050@itc.ac.kr'}
print(" ")
print("딕셔너리 c={'id':'hjin','pw':345050,'email':'202345050@itc.ac.kr'}일 경우 key:value 쌍으로 출력 : ",c.items())
s3=set('running')
print(" ")
print("s3=set('running')일 경우 s3의 결과 값 : ",s3)
sd=set([101,102,103])
sd.add(105)
print(" ")
print("s3=set([101,102,103])에서 add()함수로 105를 추가하고 그 결과 값 : ",sd)