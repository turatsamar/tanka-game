data_dict={"田中":60,"鈴木":80,"山田":90,"高田":50,"大阪":70}

#きーの表示
print("\n キーの表示", data_dict.keys(),"\n")
#点数の修正　山田　：９０　ー＞　山田：８５
print("最初の点数　", data_dict)
data_dict["山田"] = 85
print("変更後の点数", data_dict, "\n")
#for の活用
for key in data_dict:
    value=data_dict[key]
    print(key+"="+str(value))

#点数の大きい順にキーを表示
key_list=list(data_dict.keys())
data=[]
for i in range(len(key_list)):
    data.append(data_dict[key_list[i]])

print("\n きーと点数の分離")
print("    ", key_list)
print("   ",data)
for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if data [i]<data[j]:
            temp1=data[i]
            data[i]=data[j]
            temp2=key_list[i]
            key_list[i]=key_list[j]
            key_list[j]=temp2

print("大きい順")
for i in range(len(data)):
    print("    " + key_list[i]+"-"+str(data[i]))

#辞書型変数の活用２
id_number = {"1001": "田中", "1002": "鈴木", "1003":"山田", "1011":"高田", "1012":"大阪"}

#変数の点数を入力
print("\n 学生証番号に合う点数を入力")
math_score={}
for i in range(len(id_number)):
    try:
        key=input("学生証番号=")
        if key =="":break
        x=id_number[key]
        value = input("学生証番号はありません\n")
        if value =="":break
        value=int(value)
        math_score[key]=value
    except KeyError:
        print("\n 提出された学生証番号はありません\n")
        continue


#入力されたデータ
print(math_score)
