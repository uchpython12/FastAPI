# FastAPI集成SQLAlchemy增刪改查



## Getting Started
### Clone Project
你可以在本機直接使用 git 指令 clone 此專案並執行。

```
git clone https://github.com/uchpython12/FastAPI
```

```
python /main.py
```

mysql -uroot -p12345

-- 新建一个数据库，名字是 db
```
create database db charset utf8;
```
-- 使用 db 
```
use db;
```

-- 在db中新建一张 users表 

```
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1 ;
```

running locally! Your app should now be running on [localhost:8888](http://localhost:8888/) .


dosc (http://localhost:8888/docs#/).



![image](https://github.com/uchpython12/FastAPI/blob/main/APIRouter%E9%9B%86%E6%88%90%E5%88%B0Blog_app%E9%A1%B9%E7%9B%AE/Fastapi_router_img.png)
