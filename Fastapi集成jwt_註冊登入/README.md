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

-- 在db中新建一张 jwt_users表 

```
CREATE TABLE `jwt_users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1 ;

```

running locally! Your app should now be running on [localhost:8888](http://localhost:8888/) .


dosc (http://localhost:8888/docs#/).



![image](https://github.com/uchpython12/FastAPI/blob/main/Fastapi%E9%9B%86%E6%88%90jwt_%E8%A8%BB%E5%86%8A%E7%99%BB%E5%85%A5/FastAPI_Login_register.png)
