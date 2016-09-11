fuwu=["xx_s1","xx_s2","xx_s3","xx_s4","xx_s5","xx_s6","xx_s7","xx_s8","xx_s9","xx_s10"]
sum=len(fuwu)
lenth=len(fuwu)
while not lenth==0:
	j = -1
	i=0
	while (i < lenth - 2 or lenth%2==0):
			 if sum <= 2 or i>=len(fuwu)-1:
				break
			 else:
				j =j + 1
				fuwu[j]=fuwu[i][0:4]+"0"+fuwu[i][4:]
				print("%d %s"%(j,fuwu[j]))
				i=i+2
				sum =sum - 1
	if sum <= 2:
		fuwu[0]=fuwu[0][0:4]+"0"+fuwu[0][4:]
		print(fuwu[0])
		sum=0
	lenth = sum
	print(lenth)