package java_24_02_26;

public class Circle implements Shape{

	// 접근 제어자 private를 활용한 변수선언
	private double radius;
	
	
	
	//생성자
	public Circle(double radius) {
		this.radius = radius;
	}


	//인터페이스 구현
	@Override
	public double area() {
		double circle_area = radius*radius*Math.PI;
		return circle_area;
	}
	
	
	
	//일반메서드(반환값 double)
	public double circumference() {
		double circum = 2*(Math.PI)*radius;
		return circum;
	}
}

