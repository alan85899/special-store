print ("hello world")
import requests
# url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
# headers = {"accept":"application/json"}
# response=requests.get(url,headers=headers)
# res = response.json()
# print(type(res)) 
import streamlit as st
def getAllBookstore():
	# url = '' 
	# headers = {"accept": "application/json"}
	# response = requests.get(url, headers=headers)
	url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
	headers = {"accept":"application/json"}
	response=requests.get(url,headers=headers)
	res = response.json()
	return res

def getCountyOption(items):
	optionlist=[]
	for item in items:
		# 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
		# hint: 想辦法處理 item['cityName'] 的內容
		name=item['cityName'][0:3]
		if name not in optionlist:
			optionlist.append(name)
		# 如果 name 不在 optionList 之中，便把它放入 optionList
		# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
	return optionlist


def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county in name:
            specificBookstoreList.append(item)
    return specificBookstoreList

def app():
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    specificBookstore = getSpecificBookstore(bookstoreList, county)
    num = len(specificBookstore)  # 新增
    st.write(f'總共有{num}間書店') # 新增

if __name__ == '__main__':
    app()


	