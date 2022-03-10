import pandas as pd 
df=pd.read_csv(r'C:\Users\Phuoc Phe Phon\Desktop\pYTHON\data final\dataxechototfinal.csv',delimiter=';')
#bỏ chữ đ,bỏ dấu chấm bỏ 6 số 0 biến thành số int
df['Giá']=df['Giá'].apply(lambda x : float(x.replace('.','').split(' ')[0].replace('đ',"0"))/1000000)
# tạo biên trên biên dưới loại bỏ điểm ngoại lai >10tr 
df=df[(df['Giá']>=10) & (df['Giá']<=30000)] 


# chuyển đổi mới thành 1 cũ thành không
df['Tình Trạng']=df['Tình Trạng'].apply(lambda x : 1 if x =='Mới' else 0)

# loại bỏ nan
df = df[(df['Dòng xe'].notna()) & (df['Hãng'].notna()) & (df['Giá'].notna())]
##### số lượng dòng xe trên 20 và trả kết quả
# df = df[df['Dòng xe'].map(df['Dòng xe'].value_counts()) >= 20 ]

df['Năm sản Xuất']=df['Năm sản Xuất'].apply(lambda x : 2022 - int(x.replace("trước năm ",'')))
df = df[df['Hãng'] != 'Hãng khác']
#drop các biến không cần thiết
df['Hãng']=df["Hãng"]+' '+df['Dòng xe']
df.drop(['Dòng xe'],inplace=True,axis = 1 )
df=df[df['Số Chỗ'] != 'Khác']
#ĐIỀN NAN BẰNG SỐ XUẤT HIỆN NHIỀU NHẤT TRONG GROUP ĐÓ
groups = df.groupby("Hãng")

all_na = groups['Số Chỗ'].transform(lambda x: x.isna().all())
df.loc[all_na, 'Số Chỗ'] = df['Số Chỗ'].mode()[0]
mode_by_group = groups['Số Chỗ'].transform(lambda x: x.mode()[0])
df['Số Chỗ'] = df['Số Chỗ'].fillna(mode_by_group).apply(lambda x : int(x))


all_na = groups['Hộp số'].transform(lambda x: x.isna().all())
df.loc[all_na, 'Hộp số'] = df['Hộp số'].mode()[0]
mode_by_group = groups['Hộp số'].transform(lambda x: x.mode()[0])
df['Hộp số'] = df['Hộp số'].fillna(mode_by_group)

all_na = groups['Nhiên liệu'].transform(lambda x: x.isna().all())
df.loc[all_na, 'Nhiên liệu'] = df['Nhiên liệu'].mode()[0]
mode_by_group = groups['Nhiên liệu'].transform(lambda x: x.mode()[0])
df['Nhiên liệu'] = df['Nhiên liệu'].fillna(mode_by_group)


all_na = groups['Xuất sứ'].transform(lambda x: x.isna().all())
df.loc[all_na, 'Xuất sứ'] = df['Xuất sứ'].mode()[0]
mode_by_group = groups['Xuất sứ'].transform(lambda x: x.mode()[0])
df['Xuất sứ'] = df['Xuất sứ'].fillna(mode_by_group)


all_na = groups['Kiểu Dáng'].transform(lambda x: x.isna().all())
df.loc[all_na, 'Kiểu Dáng'] = df['Kiểu Dáng'].mode()[0]
mode_by_group = groups['Kiểu Dáng'].transform(lambda x: x.mode()[0])
df['Kiểu Dáng'] = df['Kiểu Dáng'].fillna(mode_by_group)

##### số lượng dòng xe trên 20 và trả kết quả
df = df[df['Hãng'].map(df['Hãng'].value_counts()) >= 20 ]
print(df['Hãng'].value_counts())
df.to_csv(r'C:\Users\Phuoc Phe Phon\Desktop\pYTHON\data final\dataxeMODEL.csv',index= False,encoding = 'utf-8')

