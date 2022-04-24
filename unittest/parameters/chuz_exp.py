class exp():
    course_path="/html/body/div/section/main[2]/div/div/div[5]/div/div[1]/div"
    exp_info = [
        {
            'name': 'Arduino-led',
            'chapter': '//*[@id="components-layout-demo-top"]/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div',
            'exp': '/html/body/div/section/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': 'Arduino-serial',
            'chapter': '/html/body/div/section/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div',
            'exp': '/html/body/div/section/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        {
            'name': 'Arduino-clock',
            'chapter': '/html/body/div/section/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div',
            'exp': '/html/body/div/section/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[3]/div/div[2]/button[2]',
        },
        {
            'name': 'Arduino-temperature',
            'chapter': '/html/body/div/section/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div',
            'exp': '/html/body/div/section/main[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[4]/div/div[2]/button[2]',
        },
        {
            'name': 'stm32-serial',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': 'stm32-led',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        {
            'name': 'stm32-timer',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[3]/div/div[2]/button[2]',
        },
        {
            'name': 'stm32-bandwith',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[4]/div/div[2]/button[2]',
        },
        {
            'name': 'stm32-capture',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[5]/div/div[2]/button[2]',
        },
        {
            'name': 'MQTT',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': 'LORA',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        {
            'name': 'bluetooth',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[3]/div/div[2]/button[2]',
        },
        {
            'name': 'ZIGBEE',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[4]/div/div[2]/button[2]',
        },
        {
            'name': 'AliOS-serial',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': 'AliOS-temperature',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        {
            'name': 'AliOS-monitor',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[3]/div/div[2]/button[2]',
        },
        {
            'name': 'AliOS-led',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[4]/div/div[2]/button[2]',
        },
        {
            'name': 'Tinylink-serial',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': 'Tinylink-temperature',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        {
            'name': 'Tinylink-SD',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[3]/div/div[2]/button[2]',
        },
        {
            'name': 'Tinylink-IoT studio',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[5]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[4]/div/div[2]/button[2]',
        },
        {
            'name': 'Contiki-construction',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[6]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[6]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': 'Contiki-UDP',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[6]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[6]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        {
            'name': '数字识别',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[7]/div[1]',
            'exp': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[7]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': '图像人脸识别',
            'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[7]/div[1]',
            'exp': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[7]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        # {
        #     'name': '相机人脸识别',
        #     'chapter': '/html/body/div/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[7]/div[1]',
        #     'exp': '',
        # },
        {
            'name': '边缘计算-ifttt智能灯',
            'chapter': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[1]',
            'exp': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[1]/div/div[2]/button[2]',
        },
        {
            'name': '边缘计算-边缘图像识别',
            'chapter': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[1]',
            'exp': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[2]/div/div[2]/button[2]',
        },
        {
            'name': '边缘计算-influx数据库存储',
            'chapter': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[1]',
            'exp': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[3]/div/div[2]/button[2]',
        },
        {
            'name': '边缘计算-边缘MQTT设备接入',
            'chapter': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[1]',
            'exp': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[4]/div/div[2]/button[2]',
        },
        {
            'name': '边缘计算-函数计算',
            'chapter': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[1]',
            'exp': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[5]/div/div[2]/button[2]',
        },
        {
            'name': '边缘计算-边缘Modbus设备接入',
            'chapter': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[1]',
            'exp': '/html/body/div[1]/section/main[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/div[8]/div[2]/div/div[3]/div[1]/div/div/div/ul/li[6]/div/div[2]/button[2]',
        },
    ]
