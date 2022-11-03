public class Lesson2 {
    public static void main(String[] args) {
        for_loop_yes();
        car();
        day();
        error();
    }

    public static void for_loop_yes(){
        for (int i = 0; i<5; i++) {
            System.out.println("Yes");
        }
    }

    public static void car(){
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String el : cars) {
            System.out.println(el);
        }
    }

    public static void day(){
        int day = 4;
        if (day == 6) {
            System.out.println("today is Saturday");
        } else if (day == 7) {
            System.out.println("today is Sunday");
        } else {
            System.out.println("looking forward to the weekend");
        }

        switch (day) {
            case 6:
                System.out.println("today is Saturday");
                break;
            case 7:
                System.out.println("today is Sunday");
                break;
            default:
                System.out.println("looking forward to the weekend");
        }
    }

    public static void error(){
        int[] myNumbers = {1, 2, 3};

        try {
            System.out.println(myNumbers[10]);
        } catch (ArrayIndexOutOfBoundsException message) {
            System.out.println(message);
        }
    }
}
