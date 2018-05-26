dict={}
dict["id"]='101','102','104'
dict["grade"]='A','C','E'
dict["name"]='vishal','rohit','kapil'
dict["section"]='D','E','F'
print("enter the choice ")
print("1.enter the key to see its value 2.display the whole dictionary") 
ch=int(input())
if(ch==1):
	print("enter the key")
	val=input()
	print("value is {}".format(dict[val]))
elif(ch==2) :
	print("whole dictionary is")
	print(dict)

else :
        print("wrong choice")
