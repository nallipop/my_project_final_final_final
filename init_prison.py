from pymongo import MongoClient

client = MongoClient('mongodb://test:test@3.35.251.121', 27017)
# client = MongoClient("localhost", 27017)
db = client.dbproject

data = [
    {
        "menu": "크로마유돈코츠전골",
        "price": 15900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "밀푀유 나베 ",
        "price": 15900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "차돌얼큰 해물짬뽕",
        "price": 12900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "갱생 부대찌개",
        "price": 10900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "C1 북어계란탕",
        "price": 9900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "바지락 짬뽕 순두부",
        "price": 9900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "내입에 딱 새우라면",
        "price": 7900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "너가 생각하는 오뎅탕",
        "price": 6900,
        "img": ".jpg",
        "tab": 1,
    },
    {
        "menu": "순살 후라이드와 치즈볼",
        "price": 11900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "순살 마늘파닭",
        "price": 11900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "베이컨 치즈 대만감자",
        "price": 9900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "체다 시즈닝 모듬감자",
        "price": 5900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "트러플 리얼 감자칩",
        "price": 5900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "닭껍질 튀김",
        "price": 6900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "똥집 후라이드",
        "price": 6900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "딸기잼에 빠진 꽃빵",
        "price": 6900,
        "img": ".jpg",
        "tab": 2,
    },
    {
        "menu": "감바스 with 스파게티",
        "price": 12900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "프리즌 수제피자(치즈or페퍼로니)",
        "price": 10900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "빠네 시카고 피자",
        "price": 10900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "빠네 크림 파스타",
        "price": 10900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "맥앤치즈",
        "price": 7900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "치킨로제 파스타와 바게트",
        "price": 9900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "에그인헬 with 바게트",
        "price": 10900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "양송이 체다스프와 빠네빵",
        "price": 7900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "멕시칸 치즈나쵸",
        "price": 7900,
        "img": ".jpg",
        "tab": 3,
    },
    {
        "menu": "골뱅이무침과 파스타",
        "price": 12900,
        "img": ".jpg",
        "tab": 4,
    },
    {
        "menu": "벽돌 계란말이",
        "price": 9900,
        "img": ".jpg",
        "tab": 4,
    },
    {
        "menu": "벽돌 계란말이 with 치즈",
        "price": 11900,
        "img": ".jpg",
        "tab": 4,
    },

    {
        "menu": "출소 제윢두부김치",
        "price": 9900,
        "img": ".jpg",
        "tab": 4,
    },
    {
        "menu": "까르보나라 떡볶이",
        "price": 9900,
        "img": ".jpg",
        "tab": 4,
    },
    {
        "menu": "호로록 치즈라볶이",
        "price": 9900,
        "img": ".jpg",
        "tab": 4,
    },
    {
        "menu": "타코 와사비",
        "price": 8900,
        "img": ".jpg",
        "tab": 4,
    },

    {
        "menu": "우삼겹 숙주볶음",
        "price": 9900,
        "img": ".jpg",
        "tab": 5,
    },
    {
        "menu": "오돌뼈와 주먹밥",
        "price": 9900,
        "img": ".jpg",
        "tab": 5,
    },
    {
        "menu": "암돼지 제육볶음",
        "price": 9900,
        "img": ".jpg",
        "tab": 5,
    },
    {
        "menu": "무뼈닭발 볶음",
        "price": 9900,
        "img": ".jpg",
        "tab": 5,
    },
    {
        "menu": "매콤 인싸동 껍딱볶음",
        "price": 7900,
        "img": ".jpg",
        "tab": 5,
    },
    {
        "menu": "통마늘 닭똥집 볶음",
        "price": 7900,
        "img": ".jpg",
        "tab": 5,
    },
    {
        "menu": "나쵸와 과카몰리 with멕시코",
        "price": 10900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "먹태",
        "price": 10900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "아귀포",
        "price": 9900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "오징어 버터구이",
        "price": 6900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "튀김쥐포",
        "price": 5900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "돈코츠우동",
        "price": 5900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "냄비우동",
        "price": 4900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "트러플 짜게치",
        "price": 4900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "참치 마요밥",
        "price": 4900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "치킨 마요밥",
        "price": 4900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "간장 계란밥",
        "price": 3900,
        "img": ".jpg",
        "tab": 6,
    },
    {
        "menu": "제철과일",
        "price": 15900,
        "img": ".jpg",
        "tab": 7,
    },
    {
        "menu": "과일화채",
        "price": 15900,
        "img": ".jpg",
        "tab": 7,
    },
    {
        "menu": "과일 두종류",
        "price": 9900,
        "img": ".jpg",
        "tab": 7,
    },
    {
        "menu": "오레오 초코빙수",
        "price": 9900,
        "img": ".jpg",
        "tab": 7,
    },
    {
        "menu": "파인샤베트",
        "price": 7900,
        "img": ".jpg",
        "tab": 7,
    },
    {
        "menu": "생귤탱귤 만다린",
        "price": 5900,
        "img": ".jpg",
        "tab": 7,
    },
    {
        "menu": "옛날 팥빙수",
        "price": 6900,
        "img": ".jpg",
        "tab": 7,
    },
    {
        "menu": "바닐라 아이스크림 한접시",
        "price": 5900,
        "img": ".jpg",
        "tab": 7,
    },

    {
        "menu": "",
        "price": 00,
        "img": ".jpg",
        "tab": 6,
    },

]

db.prison.delete_many({})
db.prison.insert_many(data)

exit(1)