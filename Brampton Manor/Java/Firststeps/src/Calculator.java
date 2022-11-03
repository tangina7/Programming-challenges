public class Calculator {

    private static int addition (int a, int b) {
        int answer = a + b;
        return answer;
    }

    private static int subtraction (int a, int b){
        int answer = a - b;
        return answer;
    }

    private static int multiplication (int a, int b){
        int answer = a * b;
        return answer;
    }

    private static int division (int a, int b) {
        int answer = a / b;
        return answer;
    }

    private static Double square (int a) {
        Double answer = Math.pow(a, 2);
        return answer;
    }

    private static Double cube (int a) {
        Double answer = Math.pow(a, 2);
        return answer;
    }

    private static Double power (int a, int b) {
        Double answer = Math.pow(a, b);
        return answer;
    }

    private static int factorial (int a) {
        int answer = 1;
        for (int i = 1; i < a+1; i++) {
            answer = answer * i;
        }
        return answer;
    }

    public static void main(String[] args){
        String choice = args[0];
        int firstValue = Integer.parseInt(args[1]);
        int secondValue = Integer.parseInt(args[2]);

        switch(choice) {
            case "addition":
                int answerA = addition(firstValue, secondValue);
                System.out.println(answerA);
                break;
            case "subtraction":
                int answerS = subtraction(firstValue, secondValue);
                System.out.println(answerS);
                break;
            case "multiplication":
                int answerM = multiplication(firstValue, secondValue);
                System.out.println(answerM);
                break;
            case "division":
                int answerD = division(firstValue, secondValue);
                System.out.println(answerD);
                break;
            case "square":
                Double answerM2 = square(firstValue);
                System.out.println(answerM2);
                break;
            case "cube":
                Double answerM3 = cube(firstValue);
                System.out.println(answerM3);
                break;
            case "power":
                Double answerM4 = power(firstValue, secondValue);
                System.out.println(answerM4);
                break;
            case "factorial":
                int answerM5 = factorial(firstValue);
                System.out.println(answerM5);
        }



    }
}
