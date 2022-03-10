## KARSALES_Data-collection-and-Analysis.

* Created a tool that estimates car sale price to help customers buy car at the price the car should be paid.
* Scraped over 30.000 price and information using python and selenium.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask (upcoming).
## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
*	Hãng
*	Dòng xe
*	Giá
*	Số Chỗ
*	số Km đã chạy
*	Tình Trạng
*	Năm sản Xuất
*	Hộp số
*	Nhiên liệu
*	Xuất sứ
*	Kiểu Dáng
*	Links
# Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
* Remove all out-lier that have price less than 10.000.000đ and more than 30.000.000.000đ (cause what i have seen that less than 10m is all meterial and more than 30b is not a real car)
* Decode 'Tình Trạng' 1 mean 'Mới' and 0 mean 'Đã sử dụng'
* Eliminate all Null variable form columns 
  * Dòng xe
  * Hãng
  * Giá  
* Replace null by mode of clolumns  
  * Số Chỗ
  * Tình Trạng 
  * Hộp số
  * Nhiên liệu 
  * Xuất sứ 
  * Kiểu Dáng 
  * and also get rid of `Khác` variable from `Số Chỗ` 
* Eliminate all string variable of `Năm sản xuất` and convert it to int for further Exploretory Analysis.
* Replace column 'Năm sản xuất' by `Số Tuổi`. `Số tuổi` = `2022 - 'Năm sản xuất`
# Data Visualization
I created a data visualization base on customer need and have these scenerio.

![image](https://user-images.githubusercontent.com/98181828/157670277-1b23ad49-b6a8-401e-a664-9c30f9652e05.png)

* This is one of the result.

![image](https://user-images.githubusercontent.com/98181828/157670584-2b91fb85-1e57-482b-b552-17c12c236931.png)

* Colusion : 
 * It's provide us the total of data have been analized
 * The range of price that the car are selling in the market
 * the price the data suggest you should paid for that car

# Model Building
This model is have some issue about the data .

![image](https://user-images.githubusercontent.com/98181828/157665811-2a244cd1-7c6f-4450-b900-264ba7807fb9.png)

# GIÁ
* The first thing is eliminate all price outlier as you can see it have significant amount of out-lier so in order to use have to remove all of this non useable variable out of the model.

![image](https://user-images.githubusercontent.com/98181828/157663266-f3188a9a-e5d5-4eb2-895a-e049d59e89c7.png).

* The data from the partition shows that Price following an exponential trend rather than a Normal Distribution from that model we build will not be determined precisely because the line model will follow that outlier path, creating out biased variants.

![image](https://user-images.githubusercontent.com/98181828/157663380-52b14b61-be39-49f9-9829-9999abd0dd04.png).

* After transform the data to Normal Distribution using log-semi method.

![image](https://user-images.githubusercontent.com/98181828/157663936-c6cdf27b-affa-44a9-a6fd-d93a2d9ca39c.png).
# Số Km đã chạy

![image](https://user-images.githubusercontent.com/98181828/157666215-9c6c9882-3954-43df-a4d5-b164cb20517d.png)

* I used the same mehod with số km đã chạy as you can see it have too much new variable and other number cant be use to put into the model 

![image](https://user-images.githubusercontent.com/98181828/157665954-0bce0763-b2d8-4350-a18d-0015789ed337.png)

## RELAX ASSUMPSION
* NO AUTOCORELATION

![image](https://user-images.githubusercontent.com/98181828/157666337-69c13628-2478-4b78-8094-83c77712a74d.png)

* No MULTICOLLINEARITY

![image](https://user-images.githubusercontent.com/98181828/157666540-e3cc7345-ea7e-4413-9219-3c4e2957104a.png)

# Model into production
Using sk-learn module to automate analyze the data
* split into two data set :
 * Train set  
 * test set
![image](https://user-images.githubusercontent.com/98181828/157666835-640c1e1b-447f-46cd-b089-14f008ba1efb.png)

have MAPE 
neg_mean_absolute_error : 162.32 (cant be use)
