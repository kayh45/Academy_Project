
public class Test {
	
	 protected void testMethod(){
		 System.out.println("testMethod");
	 }
	 
	 public int testMethod2(){
		 Test a = new Test();
		 a.testMethod();
		 System.out.println("testMethod2");
		 int b = 10;
		 
		 return b;
		 
		 
	 }

	 public static void main(String[] args){
		 Test Candy = new Test();
		 
		 Candy.testMethod();
		 System.out.println(Candy.testMethod2());
	 }
}
