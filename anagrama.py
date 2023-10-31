# Реализовать проверку фразы на «анаграмму».
def iSanagram(str1,str2)->str:
    def findAndCount(str1, str2):
        myList1 = [char for char in str1]
        myList2 = [char for char in str2]
        for char in myList1:
            if char not in myList2:
                return False
        return True
    if len(str1)==len(str2):
        return findAndCount(str1,str2)
    return False
print(iSanagram("oop","ppo"))
