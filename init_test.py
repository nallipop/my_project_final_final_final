from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbproject

data = [
    {
        "menu": "스팸후라이",
        "price": 11000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT-NdvLYYTkHwhZyaGGDkcZ4CnUQQ91b-JJgA&usqp=CAU",
        "tab": 1,
    },
    {
        "menu": "닭똥집",
        "price": 13000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRJFUoLk8Lqra3FSFOFa8jT7aXqK7iRTNJwog&usqp=CAU",
        "tab": 1,
    },
    {
        "menu": "오징어무침",
        "price": 15000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQeWslEY80U2hhI0Om7zLuVcDrtaAeVE4LqBA&usqp=CAU",
        "tab": 1,
    },
    {
        "menu": "녹두 빈대떡",
        "price": 10000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTxJjlsoVbIjzJ0XHBBUhzyw6GIy7ujuMaQg&usqp=CAU",
        "tab": 1,
    },
    {
        "menu": "감자튀김",
        "price": 11000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTrN15JWtwgOJ6Iyv-6lvn8CsOGktqVkNGT3w&usqp=CAU",
        "tab": 1,
    },
    {
        "menu": "명란마요구이",
        "price": 13000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTmThxRPyMTl_poE5F5OScv6lRyVgTI5nrc7g&usqp=CAU",
        "tab": 1,
    },
    {
        "menu": "고추장찌게",
        "price": 15000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS-nC466Pdx-GxxTaJNOiPLww3oJELKgPamBg&usqp=CAU",
        "tab": 1,
    },
    {
        "menu": "소세지야채볶음",
        "price": 10000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ29tE7cAZbHUw7BU3-3se8SmgJDgD0xUc4-w&usqp=CAU",
        "tab": 2,
    },
    {
        "menu": "차돌숙주볶음",
        "price": 11000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTXTa1SoBjWmcuUga377lc09oeE3z1BjZlgmg&usqp=CAU",
        "tab": 2,
    },
    {
        "menu": "과일화채",
        "price": 13000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ0YdE_J-5GhEGHqnqfvFnvcRiUfgUgpKJ1Hw&usqp=CAU",
        "tab": 2,
    },
    {
        "menu": "고등어구이",
        "price": 15000,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ61XJ7UFEgQIx8-7bxBbOMH9sDCfwuG8r3-A&usqp=CAU",
        "tab": 2,
    },
    {
        "menu": "처음처럼",
        "price": 4000,
        "tab": 4,
    },

    {
        "menu": "진로이즈백",
        "price": 4000,
        "tab": 4,
    },
    {
        "menu": "참이슬",
        "price": 4000,
        "tab": 4,
    },
    {
        "menu": "청하",
        "price": 5000,
        "tab": 4,
    },
    {
        "menu": "클라우드",
        "price": 4000,
        "tab": 4,
    },
    {
        "menu": "테라",
        "price": 4000,
        "tab": 4,
    },

]

db.HwangPo.delete_many({})
db.HwangPo.insert_many(data)

exit(1)
