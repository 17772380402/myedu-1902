import requests
if __name__ == '__main__':
    # 声明login_data变量名 用来存 登录的请求数据
    login_data={"username":"admin","password":"123456"}
    login_resp=requests.post(url='http://192.168.60.132:8080/admin/login',json=login_data)
    print(type(login_resp))
    login_resp_text=login_resp.text
    print(login_resp_text)

    login_resp_json = login_resp.json()
    print(login_resp_json['massage'])
