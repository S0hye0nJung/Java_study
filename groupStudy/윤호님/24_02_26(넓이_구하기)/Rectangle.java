package java_24_02_26;

public class Rectangle implements Shape{

	
	
	// 접근 제어자 private를 활용한 변수선언
	private double height;
	private double length;
	
	
	//생성자
	public Rectangle(double height, double length) {
		this.height = height;
		this.length = length;
	}
	
	//인터페이스 구현
	@Override
	public double area() {
		
		double rectangle_area = height*length;
		
		return rectangle_area;
	}
	
	//일반메서드(반환값 double)
	public double circumference() {
		double circum = 2*(height+length);
		return circum;
	}

}

