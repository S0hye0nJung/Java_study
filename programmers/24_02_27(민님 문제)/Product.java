package ezen;
class Product{

//private 변수 선언
//상품번호, 상품명, 회사명, 가격, 출고상품 횟수
//변수명은 자유롭게
	private int mNum = 0, mPrice = 0;
	private String mName = null, mWhere;

private static int count = 0;

//생성자
public Product(String product, String com, int price) {
	this.mName =product;
	this.mWhere =com;
	this.mPrice =price;
	
	}



public int getmNum() {
	return mNum;
}



public int getmPrice() {
	return mPrice;
}



public String getmName() {
	return mName;
}



public String getmWhere() {
	return mWhere;
}



public static int getCount() {
	return count;
}



public static int getCount(int count) {
		
		return count;
		
	}



}
