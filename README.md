# MJU_2022_spring_capstone
<hr>

### 1. 서비스 소개

* 선호하는 향, 원하는 브랜드의 가치, 원하는 지속성, 원하는 계절감 총 4개의 질문을 사용자에게 하고
* 이를 기반으로 사용자에게 적합한 향수를 추천해주는 서비스입니다.

<img width="655" alt="스크린샷 2022-08-25 오후 5 24 49" src="https://user-images.githubusercontent.com/95601414/186616320-fc501eb1-31b0-4c63-9337-f1a904f8a54b.png">
<img width="982" alt="스크린샷 2022-08-25 오후 5 30 17" src="https://user-images.githubusercontent.com/95601414/186616314-ba377d44-0987-49d2-afa3-4b2ba6ac729d.png">
<img width="973" alt="스크린샷 2022-08-25 오후 5 30 26" src="https://user-images.githubusercontent.com/95601414/186616295-0af7ab5f-141b-4696-baa6-ee3fa03c2c80.png">

<br>
<br>
<br>

### 2. 세부 기능 설명

> 2 - 1 메인 페이지
<img width="1440" alt="스크린샷 2022-08-25 오후 5 54 08" src="https://user-images.githubusercontent.com/95601414/186621130-ef3e9a00-aee8-44ef-94f6-c958b065dea3.png">

> 2 -2 향수 관련 용어 사전
<img width="980" alt="스크린샷 2022-08-25 오후 5 14 45" src="https://user-images.githubusercontent.com/95601414/186612614-e2ab5d5c-5aec-426b-ae85-fd9b07db9191.png">

> 2- 3 특정 향수와 비슷한 향수 찾기
<img width="553" alt="스크린샷 2022-08-25 오후 5 14 58" src="https://user-images.githubusercontent.com/95601414/186612679-00c03c80-2f42-429d-88ab-20ecb0f8c6f8.png">

<img width="455" alt="스크린샷 2022-08-25 오후 5 15 02" src="https://user-images.githubusercontent.com/95601414/186612709-88916d1e-997f-484a-a12f-d2fef09cc660.png">

> 2 - 4 향수 검색하기
<img width="456" alt="스크린샷 2022-08-25 오후 5 15 05" src="https://user-images.githubusercontent.com/95601414/186612741-3a9dcfe1-5400-45cc-8ac7-b67da6ddd6ae.png">

> 2 - 5 질문으로 향수 추천받기
<img width="317" alt="스크린샷 2022-08-25 오후 5 55 18" src="https://user-images.githubusercontent.com/95601414/186621306-24e62322-3885-4750-848c-1ec3c0537314.png">
<img width="1028" alt="스크린샷 2022-08-25 오후 5 19 09" src="https://user-images.githubusercontent.com/95601414/186614300-f8448d45-e014-48c7-a543-a658f00024ed.png">
<img width="1023" alt="스크린샷 2022-08-25 오후 5 19 46" src="https://user-images.githubusercontent.com/95601414/186614335-a6ebb4de-f478-4bd5-b7c3-55bbdf898c54.png">
<img width="1024" alt="스크린샷 2022-08-25 오후 5 19 59" src="https://user-images.githubusercontent.com/95601414/186614339-551e6a40-76bf-4b23-aa9c-22b382e6b237.png">
<img width="974" alt="스크린샷 2022-08-25 오후 5 20 09" src="https://user-images.githubusercontent.com/95601414/186614343-030adec1-8e18-4ecc-916d-9f8a5ad7e60f.png">
<img width="1024" alt="스크린샷 2022-08-25 오후 5 20 22" src="https://user-images.githubusercontent.com/95601414/186614347-e7b74e68-80cc-4270-bfe1-28b08a71e8ac.png">
<img width="1023" alt="스크린샷 2022-08-25 오후 5 20 46" src="https://user-images.githubusercontent.com/95601414/186614350-1949ab29-ba36-4a6a-af56-aa1b2c2050a4.png">
<img width="1025" alt="스크린샷 2022-08-25 오후 5 20 53" src="https://user-images.githubusercontent.com/95601414/186614354-4f4ea0f9-565d-4429-8bfe-80e9901c0304.png">
<img width="952" alt="스크린샷 2022-08-25 오후 5 21 04" src="https://user-images.githubusercontent.com/95601414/186614356-edf0849f-c447-41aa-ae37-529aadfb77d7.png">
<img width="1384" alt="KakaoTalk_Photo_2022-08-25-17-17-35" src="https://user-images.githubusercontent.com/95601414/186614486-b0700827-e6f4-4e74-ade6-7495a5122f3d.png">

> 2 - 5 동작 흐름
![image](https://user-images.githubusercontent.com/95601414/186613924-29492e03-a975-4722-a06a-cc7c03cdf1a0.png)

<br>
<br>
<br>

### 3. 아키텍처

![image](https://user-images.githubusercontent.com/95601414/186613878-5111f1e5-50d6-425f-861c-1480b86b6211.png)

<br>
<br>
<br>

### 4. 향수 소스 데이터

> 셀레니움 라이브러리를 이용한 크롤링
> 대략 25000개의 향수 데이터를 확보함
![image](https://user-images.githubusercontent.com/95601414/186613992-2875e498-3b87-45df-9ff9-396a1677e463.png)
![image](https://user-images.githubusercontent.com/95601414/186614027-9ccb836a-910b-493f-9f6b-68cf27c730ad.png)

<br>
<br>
<br>

### 5. 알고리즘

![image](https://user-images.githubusercontent.com/95601414/186614105-4334edf1-6ff5-41eb-9353-edebefe8d55d.png)

> 코사인 유사도에 기반한 cbf 알고리즘
> 벡터 간의 거리 차에 기반하여 Features로 이루어진 벡터들 간의 유사도를 구할 수 있다
