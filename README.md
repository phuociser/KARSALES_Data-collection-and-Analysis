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
## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
* Remove all out-lier that have price less than 10.000.000đ and more than 30.000.000.000đ (cause what i have seen that less than 10m is all meterial and more than 30b is not a real car)
* Decode 'Tình Trạng' 1 mean 'Mới' and 0 mean 'Đã sử dụng'
* Eliminate all Null variable form columns 
  * 'Dòng xe', 
  * 'Hãng'
  * 'Giá'  
* Replace null by mode of clolumns  
  * 'Số Chỗ', 
  * 'Tình Trạng', 
  * 'Hộp số', 
  * 'Nhiên liệu', 
  * 'Xuất sứ', 
  * 'Kiểu Dáng' 
  * and also get rid of 'Khác' variable from 'Số Chỗ' 
* Eliminate all string variable of 'Năm sản xuất' and convert it to int for further Exploretory Analysis
* Replace column 'Năm sản xuất' by "Số Tuổi'. 'Số tuổi' = 2022 - 'Năm sản xuất'
## Data Visualization
