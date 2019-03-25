import requests
if __name__ == '__main__':
    data={"username":"admin","password":"123456"}
    response=requests.post(url='http://192.168.60.132:8080/admin/login',json=data)
    text_body=response.text
    print(type(text_body))
    print(text_body)

    json_body=response.json()
    print(type(json_body))
    print(json_body)

    # 加断言
    # 在响应状态码内加断言
    assert 200==response.status_code
    # 响应报文内加断言
    assert '成功' in json_body['message']
    # 断言code
    assert 200==json_body['code']

data_dict=json_body['data']
token_head=data_dict['tokenHead']
token =data_dict['token']
head={'Authorization':token_head+' '+token}
get_info=requests.get(url='http://192.168.60.132:8080/admin/info',headers=head)
print(get_info.text)

requests_get=requests.get('http://192.168.60.132:8080/brand/list?pageNum=1&pageSize=100',headers=head)
param={'pageNum':1,'pageSize':3}
get=requests.get('http://192.168.60.132:8080/brand/list',params=param,headers=head)
print(get.text)
json=get.json()
json_data_=json ['data']
list=json_data_ ['list']
for i in list:
    print(i)

# 查询订单列表
requests_get=requests.get('http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10',headers=head)
param={'pageNum':1,'pageSize':10}
get=requests.get('http://192.168.60.132:8080/order/list',params=param,headers=head)
print(get.text)
json=get.json()
json_data_=json ['data']
list=json_data_ ['list']
for i in list:
    print(i)
#     删除订单
requests_post=requests.post('http://192.168.60.132:8080/order/delete?ids=12',headers=head)
post=requests.post('http://192.168.60.132:8080/order/delete',params=param,headers=head)
print(post.text)
json=post.json()
list=json_data_ ['list']
for i in list:
    print(i)

#     关闭订单

