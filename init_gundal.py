from pymongo import MongoClient

client = MongoClient('mongodb://test:test@3.35.251.121', 27017)
# client = MongoClient("localhost", 27017)
db = client.dbproject

data = [
    {
        "menu": "추천_건달통골뱅이탕",
        "price": 24900,
        "img": "https://imgur.com/Z7twlNe.jpg",
        "tab": 1,
    },
    {
        "menu": "추천_꼬막무침과비빔밥小",
        "price": 9900,
        "img": "https://imgur.com/2trzhTv.jpg",
        "tab": 1,
    },
    {
        "menu": "추천_훈제삼겹두부김치",
        "price": 14900,
        "img": "https://imgur.com/3Pnl94I.jpg",
        "tab": 1,
    },
    {
        "menu": "추천_스팸치즈계란말이",
        "price": 9900,
        "img": "https://imgur.com/WPMBnud.jpg",
        "tab": 1,
    },
    {
        "menu": "추천_차돌박이순두부",
        "price": 13900,
        "img": "https://imgur.com/By0tmOe.jpg",
        "tab": 1,
    },
    {
        "menu": "추천_무뼈국물닭발",
        "price": 14900,
        "img": "https://imgur.com/O4sfnZz.jpg",
        "tab": 1,
    },
    {
        "menu": "추천_훈제삼겹야채볶음",
        "price": 11900,
        "img": "https://imgur.com/0wm7ut5.jpg",
        "tab": 1,
    },
    {
        "menu": "추천_고구마치즈맛탕",
        "price": 9900,
        "img": "https://imgur.com/cmythig.jpg",
        "tab": 1,
    },
    {
        "menu": "건달통골뱅이탕",
        "price": 24900,
        "tab": 2,
    },
    {
        "menu": "곱창전골",
        "price": 16900,
        "tab": 2,
    },
    {
        "menu": "사천차돌짬뽕탕",
        "price": 14900,
        "tab": 2,
    },
    {
        "menu": "사천해물짬뽕탕",
        "price": 14900,
        "tab": 2,
    },
    {
        "menu": "해물나가사키짬뽕탕",
        "price": 14900,
        "tab": 2,
    },
    {
        "menu": "차돌나가사키짬뽕탕",
        "price": 14900,
        "tab": 2,
    },
    {
        "menu": "얼큰해물알탕",
        "price": 14900,
        "tab": 2,
    },
    {
        "menu": "통돼지김치찌개",
        "price": 13900,
        "tab": 2,
    },
    {
        "menu": "간사이오뎅탕",
        "price": 13900,
        "tab": 2,
    },
    {
        "menu": "차돌박이순두부찌개",
        "price": 13900,
        "tab": 2,
    },
    {
        "menu": "참치김치찌개",
        "price": 10900,
        "tab": 2,
    },
    {
        "menu": "매콤어묵탕",
        "price": 9900,
        "tab": 2,
    },
    {
        "menu": "마약골뱅이무침",
        "price": 14900,
        "tab": 3,
    },
    {
        "menu": "로제떡볶이",
        "price": 14900,
        "tab": 3,
    },
    {
        "menu": "로제치즈치킨",
        "price": 14900,
        "tab": 3,
    },
    {
        "menu": "무뼈국물닭발",
        "price": 14900,
        "tab": 3,
    },
    {
        "menu": "까르보나라떡볶이",
        "price": 12900,
        "tab": 3,
    },
    {
        "menu": "훈제삼겹야채볶음",
        "price": 11900,
        "tab": 3,
    },
    {
        "menu": "스팸치즈계란말이",
        "price": 9900,
        "tab": 3,
    },
    {
        "menu": "꼬막무침과비빔밥小",
        "price": 9900,
        "tab": 3,
    },
    {
        "menu": "꼬막무침과비빔밥大",
        "price": 24900,
        "tab": 3,
    },
    {
        "menu": "오징어순대와명태회무침",
        "price": 15900,
        "tab": 3,
    },
    {
        "menu": "치킨치즈포테이토",
        "price": 13900,
        "tab": 4,
    },
    {
        "menu": "치즈모듬소시지",
        "price": 13900,
        "tab": 4,
    },
    {
        "menu": "양념순살치킨",
        "price": 13900,
        "tab": 4,
    },
    {
        "menu": "양념순살치킨",
        "price": 13900,
        "tab": 4,
    },
    {
        "menu": "과일화채",
        "price": 13900,
        "tab": 4,
    },
    {
        "menu": "과일빙수",
        "price": 13900,
        "tab": 4,
    },
    {
        "menu": "마른안주세트",
        "price": 12900,
        "tab": 4,
    },
    {
        "menu": "고구마치즈맛탕",
        "price": 9900,
        "tab": 4,
    },
    {
        "menu": "건달비빔만두",
        "price": 7900,
        "tab": 4,
    },
    {
        "menu": "반건조오징어튀김",
        "price": 7900,
        "tab": 4,
    },
    {
        "menu": "케이준양념감자",
        "price": 6900,
        "tab": 4,
    },
    {
        "menu": "제육볶음두부김치",
        "price": 14900,
        "tab": 5,
    },
    {
        "menu": "훈제삼겹두부김치",
        "price": 14900,
        "tab": 5,
    },
    {
        "menu": "차돌박이숙주볶음",
        "price": 13900,
        "tab": 5,
    },
    {
        "menu": "닭똥집볶음",
        "price": 13900,
        "tab": 5,
    },
    {
        "menu": "오돌뼈와주먹밥",
        "price": 13900,
        "tab": 5,
    },
    {
        "menu": "숯부무뼈닭발",
        "price": 13900,
        "tab": 5,
    },
    {
        "menu": "탕수육(부먹)",
        "price": 14900,
        "tab": 5,
    },
    {
        "menu": "떠먹는치즈김치전",
        "price": 7900,
        "tab": 5,
    },
    {
        "menu": "매콤떡볶이",
        "price": 6900,
        "tab": 6,
    },
    {
        "menu": "짜장떡볶이",
        "price": 6900,
        "tab": 6,
    },
    {
        "menu": "감자튀김과나초",
        "price": 3900,
        "tab": 6,
    },
    {
        "menu": "고구마치즈스틱",
        "price": 3900,
        "tab": 6,
    },
    {
        "menu": "치즈스틱",
        "price": 3900,
        "tab": 6,
    },
    {
        "menu": "아이스황도",
        "price": 3900,
        "tab": 6,
    },
    {
        "menu": "앙념떡꼬치",
        "price": 3900,
        "tab": 6,
    },
    {
        "menu": "감자튀김",
        "price": 2900,
        "tab": 6,
    },
    {
        "menu": "즉석콘치즈",
        "price": 2900,
        "tab": 6,
    },
    {
        "menu": "쥐포구이",
        "price": 2900,
        "tab": 6,
    },
    {
        "menu": "공기밥",
        "price": 1500,
        "tab": 7,
    },
    {
        "menu": "라면 우동 당면 쫄면사리",
        "price": 2000,
        "tab": 7,
    },
    {
        "menu": "골뱅이무침용 쫄면사리",
        "price": 3000,
        "tab": 7,
    },
    {
        "menu": "비빔만두용 만두사리",
        "price": 3000,
        "tab": 7,
    },
    {
        "menu": "볶음용 밥",
        "price": 3000,
        "tab": 7,
    },
    {
        "menu": "마요주먹밥",
        "price": 4000,
        "tab": 7,
    },
    {
        "menu": "참치마요주먹밥",
        "price": 4500,
        "tab": 7,
    },
    {
        "menu": "스팸마요 주멉밥",
        "price": 4900,
        "tab": 7,
    },
    {
        "menu": "Self 계란라면",
        "price": 3900,
        "tab": 7,
    },
    {
        "menu": "건달우동",
        "price": 4900,
        "tab": 7,
    },
    {
        "menu": "예거마이스터",
        "price": 79000,
        "img": "https://imgur.com/pOpsAyV.jpg",
        "tab": 8,
    },
    {
        "menu": "앱솔루트 보드카",
        "price": 69000,
        "img": "https://imgur.com/rFSLHZv.jpg",
        "tab": 8,
    },
    {
        "menu": "앱솔루트 애플",
        "price": 69000,
        "img": "https://imgur.com/5P7fBBm.jpg",
        "tab": 8,
    },
    {
        "menu": "앱솔루트 어피치",
        "price": 69000,
        "img": "https://imgur.com/LhEpu2l.jpg",
        "tab": 8,
    },
    {
        "menu": "처음처럼",
        "price": 5000,
        "img": "https://imgur.com/XZAmIxt.jpg",
        "tab": 8,
    },
    {
        "menu": "처음처럼 플렉스",
        "price": 5000,
        "img": "https://imgur.com/Wfbr8R1.jpg",
        "tab": 8,
    },
    {
        "menu": "生클라우드 병",
        "price": 4500,
        "img": "https://imgur.com/7S24BTD.jpg",
        "tab": 8,
    },
    {
        "menu": "클라우드 병",
        "price": 6000,
        "img": "https://imgur.com/2Btptge.jpg",
        "tab": 8,
    },
    {
        "menu": "칭따오 병",
        "price": 6000,
        "img": "https://imgur.com/6gLXw2u.jpg",
        "tab": 8,
    },
    {
        "menu": "테라 병",
        "price": 6000,
        "img": "https://imgur.com/kt2sib4.jpg",
        "tab": 8,
    },
    {
        "menu": "심술 택1",
        "price": 6000,
        "img": "https://imgur.com/lA3a4ys.jpg",
        "tab": 8,
    },
    {
        "menu": "생맥주 500cc",
        "price": 4500,
        "img": "https://imgur.com/hWKaajo.jpg",
        "tab": 8,
    },
    {
        "menu": "생맥주 1700cc",
        "price": 14500,
        "img": "https://imgur.com/sz0vEym.jpg",
        "tab": 8,
    },
    {
        "menu": "생맥주 2700cc",
        "price": 18500,
        "img": "https://imgur.com/2a8dDtw.jpg",
        "tab": 8,
    },
    {
        "menu": "칵테일소주 망고",
        "price": 6000,
        "img": "https://imgur.com/J3BRS5q.jpg",
        "tab": 8,
    },
    {
        "menu": "칵테일소주 청포도",
        "price": 6000,
        "img": "https://imgur.com/PutcEyt.jpg",
        "tab": 8,
    },
    {
        "menu": "칵테일소주 요구르트",
        "price": 6000,
        "img": "https://imgur.com/Jg5wnxB.jpg",
        "tab": 8,
    },
    {
        "menu": "청하",
        "price": 5000,
        "img": "https://imgur.com/sThLygi.jpg",
        "tab": 8,
    },
    {
        "menu": "매화수",
        "price": 5000,
        "img": "https://imgur.com/lA3a4ys.jpg",
        "tab": 8,
    },
    {
        "menu": "알밤막걸리",
        "price": 5000,
        "img": "https://imgur.com/K9jg8DP.jpg",
        "tab": 8,
    },
    {
        "menu": "초코에몽",
        "price": 1500,
        "img": "https://imgur.com/5KaODbi.jpg",
        "tab": 9,
    },
    {
        "menu": "펩시 500ml",
        "price": 2500,
        "img": "https://imgur.com/ptY4kST.jpg",
        "tab": 9,
    },
    {
        "menu": "칠성사이다 500ml",
        "price": 2500,
        "img": "https://imgur.com/E9gvrnJ.jpg",
        "tab": 9,
    },
    {
        "menu": "핫식스 250ml",
        "price": 3000,
        "img": "https://imgur.com/kOLIbXQ.jpg",
        "tab": 9,
    },
    {
        "menu": "토닉워터 300ml",
        "price": 3000,
        "img": "https://imgur.com/ROEriRK.jpg",
        "tab": 9,
    },
    {
        "menu": "레몬슬라이스",
        "price": 2000,
        "img": "https://imgur.com/DorFzLo.jpg",
        "tab": 9,
    },
]

db.gundal.delete_many({})
db.gundal.insert_many(data)

exit(1)