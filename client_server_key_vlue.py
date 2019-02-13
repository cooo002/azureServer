from flask import Flask, render_template, request,jsonify
import json
import sys
import requests
import shutil
sys.path.append('../../METADATA')
import METADATA
import os, uuid, sys # 이건 storage를 라
from bs4 import BeautifulSoup
from werkzeug import secure_filename
from azure.storage.blob import BlockBlobService, PublicAccess
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("ajax.html")
 

@app.route('/request_disaster', methods = ['POST', 'GET']) # request disaster route

def request_disaster_send():
	if request.method == 'POST':
		area_name = request.form['fileAjax']
		disaster_msg = request_disaster(area_name)
		return disaster_msg

def request_disaster(area):
	area_name = area   # 클라이언트한테 받는 값
	area_num_real = ""
	area_number_dic = {  
                     "서울":"109",
                    "부산":"159",
                    "대구":"143",
                    "광주":"156",
                    "전주":"146",
                    "대전":"133",
                    "청주":"131",
                    "강릉":"105",
                    "제주":"184"   }

	for area_num in area_number_dic:
		if area_num == area_name:
			area_num_real = area_number_dic[area_num]

	url = 'http://newsky2.kma.go.kr/service/WetherSpcnwsInfoService/WeatherPrepareWarning'
	queryParams = '?' + 'serviceKey=' + METADATA.DISASTER_KEY \
                     + '&fromTmFc=' + '20190201' \
                     + '&toTmFc=' + '20190210' \
                     + '&numOfRows=' + '1' \
                     + '&pageNo=' + '1' \
                     + '&stnId=' + area_num_real

	url_weather_news = url + queryParams

	result = requests.get(url_weather_news)  #원하는 웹 페이지에 request를 보내 결과를 html을 받는.	bs_obj = BeautifulSoup(result.content, "html.parser")
	body = bs_obj.find("body") # 12 막 넘어서 하니까 예보 할 것이 없어
	rem = body.find("pwn") # 내용이 빈다.
	result_msg = ""
	restart_location = "위치가 입력되지 않았습니다. 위치를 다시 입력해주세요"
	

	if rem is not  None and area_name is "":
		print(type(area_name))
		print(area_name)
		result_msg = restart_location
	elif rem is not None and area_name is not None:
		result_msg = rem.text
	else:
    		result_msg = "현재 발표된 재난 특보가 없습니다."

	return result_msg





@app.route('/file_upload', methods = ['POST', 'GET']) 
def fileUpload():
    if request.method == 'POST':
        f = request.files['fileAjax']
        #저장할 경로 + 파일명
        containerForImage = 'imagestorage'
        fileName = 'firstEx.jpeg'
        f.save('/home/nesta_test/BlobStorage/'+fileName)
        success_result = run_sample(fileName, containerForImage)
        success_json = {"success" : success_result}
        success = app.response_class(
                 response=json.dumps(success_json),
                  status=200,
                 mimetype='application/json'
        )        
        print(success_result)
        print(success)
        return success

def run_sample(localFileName, container):
        try:
            # Create the BlockBlockService that is used to call the Blob service for the storage account
            block_blob_service = BlockBlobService(account_name='projectimage', account_key='JRchgJJAHjSzDMHMe73/9p65tTQTY7R9v/flqDfZagSTj00JiPXlAqi44B3P4Dkr3htQL3Eq2DAG81DXS7GdTw==')

            # Create a container called 'quickstartblobs'.
            container_name = container # 저장소 이름을 대문자 사용하지말자
            # 대문자는 쓸 수 없는 문자라고 에러를 뱉는다.
            block_blob_service.create_container(container_name)
            # Set the permission so the blobsd are public.
            block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)
            # # Create a file in Documents to test the upload and download.
            local_path=os.path.expanduser("~/BlobStorage")
            local_file_name = localFileName
            storage_url = METADATA.storage_url
            blob_url = storage_url + local_file_name # 이미지 분석에 사용

            full_path_to_file =os.path.join(local_path, local_file_name)

            block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)

            result_image_analyze = use_describe_image_api(blob_url)
            result_tran = translate_ko(result_image_analyze)
            return result_tran

        except Exception as e:
            print(e)

def use_describe_image_api(blob_url_des):
        params = {  #또 다른 정보
        'visualFeatures': 'Description, Categories, Color, Tags, Faces, ImageType, Color',
        'langage': 'en',
        }

        headers = { #우리가 보내는 데이터 타입
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': METADATA.VISION_KEY # 메타 데이터엣 있는 것을 임포트 하여 사용함
        }

        data = {
        'url': blob_url_des
        }

        res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v2.0/analyze',
                        params=params, headers=headers, json=data)

        res_dit = json.loads(res.text)
        subscribed_text = res_dit["description"]["captions"][0]["text"]
        return subscribed_text

def translate_ko(result_en):
        api_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Naver-Client-Id': METADATA.ID,
            'X-Naver-Client-Secret': METADATA.SECRET
        }
        data = "source=en&target=ko&text=" + result_en
        data = data.encode("UTF-8")

        try:
            resp = requests.post(api_url, headers=headers, data=data)
            resp.raise_for_status()
            return json.loads(resp.text)['message']['result']['translatedText']
        except Exception as e:
            print(str(e))
            return '번역 에러'


@app.route('/dust_state', methods = ['POST', 'GET'])

def dust_state():
    if request.method == 'POST':
        area_name = request.form['fileAjax'] # check
        success = dust_state_api()
        print(success)
        return success

def dust_state_api():
	now = datetime.datetime.now()
	nowDate = now.strftime('%Y-%m-%d')

	base_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth'
	queryParams = '?' + 'ServiceKey=' + METADATA.DUST_KEY \
			 + '&numOfRows=' + '1' \
			 + '&pageNo=' + '1' \
			 + '&searchDate=' + nowDate \
                         + '&InformCode=' + 'PM10'

	url = base_url + queryParams

	response = requests.get(url)
	bs_obj = BeautifulSoup(response.content, "html.parser")
	body = bs_obj.find("body")
	msg = body.find("informoverall")
	result = msg.text
	return result







if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 8080, debug=True)
